import torch
import os
import gradio as gr
# from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub
from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
# Watsonx imports left as-is, but not used in this minimal Hugging Face example
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models import Model

#######------------- LLM-------------####

# Uses Hugging Face Inference API (set HUGGINGFACEHUB_API_TOKEN in your env)
# You can swap repo_id for another instruct model you have access to.
llm = HuggingFaceHub(
    repo_id="google/flan-t5-large",                # easy, ungated, text2text model
    model_kwargs={"temperature": 0.2, "max_new_tokens": 256}
)

#######------------- Prompt Template-------------####
# LLAMA2-style system/inst tags will be ignored by some models; it's fine to keep or use the simpler one below.
temp = """
<s><<SYS>>
List the key points with details from the context: 
[INST] The context : {context} [/INST] 
<</SYS>>
"""

# Simple version if you prefer:
# temp = "List the key points with details from the context:\nContext: {context}\n"

pt = PromptTemplate(
    input_variables=["context"],
    template=temp
)
prompt_to_LLAMA2 = LLMChain(llm=llm, prompt=pt)

#######------------- Speech2text-------------####
def transcript_audio(audio_file):
    # Initialize the speech recognition pipeline (runs locally; no API key needed)
    pipe = pipeline(
        task="automatic-speech-recognition",
        model="openai/whisper-small",  # good quality/speed balance; change to tiny/base/medium/large as you like
        chunk_length_s=30,             # split long audio into 30s chunks
    )

    # Transcribe the audio file and return the result
    transcript_txt = pipe(audio_file, batch_size=8)["text"]

    # run the chain to merge transcript text with the template and send it to the LLM
    result = prompt_to_LLAMA2.run(transcript_txt)
    return result

#######------------- Gradio-------------####
audio_input = gr.Audio(sources="upload", type="filepath")
output_text = gr.Textbox(label="Key Points")

iface = gr.Interface(
    fn=transcript_audio,
    inputs=audio_input,
    outputs=output_text,
    title="Audio → Key Points (Whisper + LLM)",
    description="Upload an audio file. We'll transcribe it with Whisper and extract key points via an LLM."
)

iface.launch(server_name="0.0.0.0", server_port=7860)
