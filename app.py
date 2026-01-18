import gradio as gr
from transformers import pipeline
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

asr_model = pipeline(
    "automatic-speech-recognition",
    model="distil-whisper/distil-large-v3",
    device=device
)
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    device=device
)

def process_audio(audio):
    if audio is None:
        return "No audio provided", ""
    
    print("Transcribing audio...")
    transcription = asr_model(audio)["text"]
    
    print(f"Transcription length: {len(transcription.split())} words")
    
    if len(transcription.split()) < 30:
        summary = "Text too short for summarization. Full transcription shown below."
    else:
        print("Generating summary...")
        summary_result = summarizer(
            transcription,
            max_length=150,
            min_length=40,
            do_sample=False
        )
        summary = summary_result[0]["summary_text"]
    
    return transcription, summary

with gr.Blocks(title="Multilingual Speech Summarizer") as demo:
    gr.Markdown("# Multilingual Speech Summarizer")
    gr.Markdown("**Speak or upload audio in any language** - Auto-detects language and generates summaries")
    
    with gr.Row():
        audio_input = gr.Audio(
            sources=["microphone", "upload"],
            type="filepath",
            label="Record or Upload Audio (MP3, WAV, M4A supported)"
        )
    
    with gr.Row():
        transcribe_btn = gr.Button("Transcribe & Summarize", variant="primary", size="lg")
    
    with gr.Row():
        with gr.Column(scale=2):
            transcription_output = gr.Textbox(
                label="Full Transcription", 
                lines=8,
                max_lines=10
            )
        with gr.Column(scale=1):
            summary_output = gr.Textbox(
                label="AI Summary", 
                lines=5,
                max_lines=8
            )
    
    gr.Examples(
        examples=[],
        inputs=audio_input
    )
    
    transcribe_btn.click(
        fn=process_audio,
        inputs=audio_input,
        outputs=[transcription_output, summary_output]
    )

if __name__ == "__main__":
    demo.launch(
        share=True,  
        debug=True   
    )
