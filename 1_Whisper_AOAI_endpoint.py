import gradio as gr
import os
import openai
from dotenv import load_dotenv

load_dotenv("azure.env")
# Setting Azure OpenAI endpoint parameters
openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_key = os.getenv('OPENAI_API_KEY')     
<<<<<<< HEAD
openai.api_version = os.getenv('OPENAI_API_VERSION')
openai.api_type = os.getenv('OPENAI_API_TYPE')
deployment_id = os.getenv('OPENAI_DEPLOYMENT_ID')
model = os.getenv('OPENAI_MODEL')
=======
openai.api_version = '2023-09-01-preview'
openai.api_type = 'azure'
AOAI_DEPLOYMENT_ID = "<YOUR_AOAI_DEPLOYMENT>" # Please, replace <YOUR_AOAI_DEPLOYMENT> with your deployment ID
>>>>>>> e56314f6bbb3298c9431006facb7390fee264cf8

# Transcription function
def transcribe(audio):
    with open(audio, "rb") as audio_file:
        transcription = openai.Audio.transcribe(
            file=audio_file,
<<<<<<< HEAD
            deployment_id=deployment_id,
            model=model
=======
            deployment_id=AOAI_DEPLOYMENT_ID, model=AOAI_DEPLOYMENT_ID
>>>>>>> e56314f6bbb3298c9431006facb7390fee264cf8
        )
    # print(transcription["text"])
    return transcription["text"]

# Gradio interface
demo = gr.Interface(
    transcribe, gr.Audio(source="microphone", type="filepath", label="Audio Recording"), "textbox",
    title="Demo App 1: Whisper model through Azure OpenAI endpoint",
    description="Record your speech via microphone and press the Submit button to transcribe it into text. Please, note that the size of the audio file should be less than 25 MB."
)

if __name__ == "__main__":
    demo.launch()