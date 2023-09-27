import gradio as gr

def transcribe(audio):
    return "Hello World"

demo = gr.Interface(
    transcribe,
    gr.Audio(source="microphone"),
    "textbox",
    title="Demo App 2: Whisper model through Azure AI Speech endpoint",
    description="Record your speech via microphone and press the Submit button to transcribe it into text."
)

if __name__ == "__main__":
    demo.launch()