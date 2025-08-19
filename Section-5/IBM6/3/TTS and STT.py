# git clone https://github.com/ibm-developer-skills-network/bkrva-chatapp-with-voice-and-openai-outline.git
# mv bkrva-chatapp-with-voice-and-openai-outline chatapp-with-voice-and-openai-outline
# cd chatapp-with-voice-and-openai-outline

# in server.py
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# needed commands 
# mkdir /home/project/chatapp-with-voice-and-openai-outline/certs/
# cp /usr/local/share/ca-certificates/rootCA.crt /home/project/chatapp-with-voice-and-openai-outline/certs/

# Starting the application
# docker build . -t voice-chatapp-powered-by-openai
# docker run -p 8000:8000 voice-chatapp-powered-by-openai

# Starting Speech-to-Text
base_url = "https://sn-watson-stt.labs.skills.network"
# Test it by running this query
# curl https://sn-watson-stt.labs.skills.network/speech-to-text/api/v1/models

# output should be :
{
   "models": [
      {
         "name": "en-US_Multimedia",
         "language": "en-US",
         "description": "US English multimedia model for broadband audio (16kHz or more)",
          ...
      },
      {
         "name": "fr-FR_Multimedia",
         "language": "fr-FR",
         "description": "French multimedia model for broadband audio (16kHz or more)",
          ...
      }
   ]
}

# Starting Text-to-Speech
base_url = "https://sn-watson-tts.labs.skills.network"
# Test it by running this 
# curl https://sn-watson-tts.labs.skills.network/text-to-speech/api/v1/voices

# output will be 
{
   "voices": [
      {
         "name": "en-US_EmilyV3Voice",
         "language": "en-US",
         "gender": "female",
         "description": "Emily: American English female voice. Dnn technology.",
         ...
      },
      {
         "name": "en-GB_JamesV3Voice",
         "language": "en-GB",
         "gender": "male",
         "description": "James: British English male voice. Dnn technology.",
         ...
      },
      {
         "name": "en-US_MichaelV3Voice",
         "language": "en-US",
         "gender": "male",
         "description": "Michael: American English male voice. Dnn technology.",
         ...
      },
      {
         "name": "fr-CA_LouiseV3Voice",
         "language": "fr-CA",
         "gender": "female",
         "description": "Louise: French Canadian female voice. Dnn technology.",
         ....
      },
      ...
   ]
}

# Implentation Worker.py
def speech_to_text(audio_binary):

    # Set up Watson Speech-to-Text HTTP Api url
    base_url = '...'
    api_url = base_url+'/speech-to-text/api/v1/recognize'

    # Set up parameters for our HTTP request
    params = {
        'model': 'en-US_Multimedia',
    }

    # Set up the body of our HTTP request
    body = audio_binary

    # Send a HTTP Post request
    response = requests.post(api_url, params=params, data=audio_binary).json()

    # Parse the response to get our transcribed text
    text = 'null'
    while bool(response.get('results')):
        print('speech to text response:', response)
        text = response.get('results').pop().get('alternatives').pop().get('transcript')
        print('recognised text: ', text)
        return text

# this function will pass it to GPT 3
def openai_process_message(user_message):
    # Set the prompt for OpenAI Api
    prompt = "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations."
    # Call the OpenAI Api to process our prompt
    openai_response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ],
        max_tokens=4000
    )
    print("openai response:", openai_response)
    # Parse the response to get the response message for our prompt
    response_text = openai_response.choices[0].message.content
    return response_text
  
# TTS
def text_to_speech(text, voice=""):
    # Set up Watson Text-to-Speech HTTP Api url
    base_url = '...'
    api_url = base_url + '/text-to-speech/api/v1/synthesize?output=output_text.wav'

    # Adding voice parameter in api_url if the user has selected a preferred voice
    if voice != "" and voice != "default":
        api_url += "&voice=" + voice

    # Set the headers for our HTTP request
    headers = {
        'Accept': 'audio/wav',
        'Content-Type': 'application/json',
    }

    # Set the body of our HTTP request
    json_data = {
        'text': text,
    }

    # Send a HTTP Post request to Watson Text-to-Speech Service
    response = requests.post(api_url, headers=headers, json=json_data)
    print('text to speech response:', response)
    return response.content

# The outline has already taken care of the imports for the functions from the worker.py file to the server.py file. This allows the server.py file to access these imported functions from the worker.py file.
from worker import speech_to_text, text_to_speech, openai_process_message

# Speech-to-Text route
@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    print("processing speech-to-text")
    audio_binary = request.data # Get the user's speech from their request
    text = speech_to_text(audio_binary) # Call speech_to_text function to transcribe the speech

    # Return the response back to the user in JSON format
    response = app.response_class(
        response=json.dumps({'text': text}),
        status=200,
        mimetype='application/json'
    )
    print(response)
    print(response.data)
    return response

# Process message route
@app.route('/process-message', methods=['POST'])
def process_message_route():
    user_message = request.json['userMessage'] # Get user's message from their request
    print('user_message', user_message)

    voice = request.json['voice'] # Get user's preferred voice from their request
    print('voice', voice)

    # Call openai_process_message function to process the user's message and get a response back
    openai_response_text = openai_process_message(user_message)

    # Clean the response to remove any emptylines
    openai_response_text = os.linesep.join([s for s in openai_response_text.splitlines() if s])

    # Call our text_to_speech function to convert OpenAI Api's reponse to speech
    openai_response_speech = text_to_speech(openai_response_text, voice)

    # convert openai_response_speech to base64 string so it can be sent back in the JSON response
    openai_response_speech = base64.b64encode(openai_response_speech).decode('utf-8')

    # Send a JSON response back to the user containing their message's response both in text and speech formats
    response = app.response_class(
        response=json.dumps({"openaiResponseText": openai_response_text, "openaiResponseSpeech": openai_response_speech}),
        status=200,
        mimetype='application/json'
    )

    print(response)
    return response

# docker build . -t voice-chatapp-powered-by-openai
# docker run -p 8000:8000 voice-chatapp-powered-by-openai
