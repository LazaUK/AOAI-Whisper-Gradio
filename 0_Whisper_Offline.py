import gradio as gr
import whisper

paramfp16=False # Set to True if you want to use fp16 precision on GPU
def transcribe(audio):
    model = whisper.load_model("base")
    result = model.transcribe(audio,fp16=paramfp16)
    print(result["text"])
    return result["text"]

demo = gr.Interface(
    transcribe, gr.Audio(source="microphone", type="filepath", label="Audio Recording"), "textbox",
    title="Demo App 0: Whisper model in offline mode",
    description="Record your speech via microphone and press the Submit button to transcribe it into text. Please, note that the size of the audio file should be less than 25 MB."
)

if __name__ == "__main__":
    demo.launch()
