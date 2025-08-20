# pip install git+https://github.com/openai/whisper.git
import whisper
# Load the Whisper model
model = whisper.load_model("base")
# Transcribe the audio file
result = model.transcribe("audio_example.mp3")
# Output the transcription
print(result["text"])


# Advanced Features
# Whisper's versatility allows for customization and optimization based on specific requirements:

# Language models: Whisper comes in various sizes (for example, tiny, base, small, medium, large). Larger models offer higher accuracy but require more computational resources.
# Automatic language detection: Whisper can automatically detect the language of the audio, simplifying the transcription process for multilingual applications.

# Integrating Whisper into Applications
from flask import Flask, request
import whisper
app = Flask(__name__)
model = whisper.load_model("base")
@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    audio_file = request.files["audio"]
    result = model.transcribe(audio_file)
    return {"transcription": result["text"]}
if __name__ == "__main__":
    app.run(debug=True)
