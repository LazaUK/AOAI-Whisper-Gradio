import gradio as gr
import os
import openai

# Setting Azure OpenAI endpoint parameters
openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_key = os.getenv('OPENAI_API_KEY')     
openai.api_version = '2023-09-01-preview'
openai.api_type = 'azure'

# Transcription function
def transcribe(audio):
    with open(audio, "rb") as audio_file:
        transcription = openai.Audio.transcribe(
            file=audio_file,
            deployment_id="laziz_whisper_we",
            model="laziz_whisper_we"
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