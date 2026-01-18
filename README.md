# Multilingual-Speech-Summarizer
A **multilingual AI-powered speech summarization system** that converts spoken audio into accurate text and generates concise summaries automatically.  
Built using **state-of-the-art speech recognition and NLP models** with an interactive web interface.

---

## Features

- 🎧 Record audio or upload files (MP3, WAV, M4A)
- 🌍 Automatic language detection
- 📝 High-accuracy speech-to-text transcription
- ✂️ Abstractive text summarization
- ⚡ GPU acceleration (CUDA supported)
- 🖥️ Interactive UI built with :contentReference[oaicite:0]{index=0}

---

## Models Used

### Speech Recognition
- **Model:** `distil-whisper/distil-large-v3`  
- A lightweight and efficient variant of :contentReference[oaicite:1]{index=1}  
- Supports multilingual automatic speech recognition

### Text Summarization
- **Model:** `facebook/bart-large-cnn`  
- Transformer-based abstractive summarizer using :contentReference[oaicite:2]{index=2}

All models are loaded using the :contentReference[oaicite:3]{index=3} Transformers library.

---

## System Architecture

Audio Input
↓
Automatic Speech Recognition (Whisper)
↓
Full Transcription
↓
Text Summarization (BART)
↓
AI-Generated Summary

yaml
Copy code

---

## Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/multilingual-speech-summarizer.git
cd multilingual-speech-summarizer
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the application
bash
Copy code
python app.py
🖥️ Usage
Launch the application

Record audio using the microphone or upload an audio file

Click “Transcribe & Summarize”

View:

Full transcription

AI-generated summary

🎧 Supported Audio Formats
.wav

.mp3

.m4a

⚙️ Hardware Support
  CPU

  GPU (CUDA auto-detected if available)

📁 Project Structure
Copy code
├── app.py
├── requirements.txt
├── README.md
└── assets/
📌 Use Cases
Lecture and meeting summarization

Podcast and interview analysis

Multilingual content processing

Accessibility and assistive AI tools

Academic and research transcription

🔮 Future Improvements
Speaker diarization

Timestamped transcripts

Downloadable summaries

Summary length control

Deployment on cloud platforms

📜 License
This project is licensed under the MIT License.
