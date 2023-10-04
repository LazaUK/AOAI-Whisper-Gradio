import gradio as gr
import os
import openai
from dotenv import load_dotenv

load_dotenv("azure.env")
# Setting Azure OpenAI endpoint parameters
openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_key = os.getenv('OPENAI_API_KEY')     
openai.api_version = os.getenv('OPENAI_API_VERSION')
openai.api_type = os.getenv('OPENAI_API_TYPE')
deployment_id = os.getenv('OPENAI_DEPLOYMENT_ID')
model = os.getenv('OPENAI_MODEL')

# Transcription function
def transcribe(audio):
    with open(audio, "rb") as audio_file:
        transcription = openai.Audio.transcribe(
            file=audio_file,
            deployment_id=deployment_id,
            model=model
        )
    # print(transcription["text"])
    return transcription["text"]

# Gradio interface
demo = gr.Interface(
    transcribe, gr.Audio(source="microphone", type="filepath", label="Audio Recording"), "textbox",
    title="Demo App 1: Whisper model through Azure OpenAI endpoint",
    description="Record your speech via microphone and press the Submit button to transcribe it into text."
)

if __name__ == "__main__":
    demo.launch()