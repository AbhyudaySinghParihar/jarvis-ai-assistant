# JARVIS: AI Desktop Voice Assistant

A Python-based desktop voice assistant powered by AI. I first built it with the OpenAI and ElevenLabs APIs during my Robotics Trainer internship at Youngovator (May 2026), then rebuilt it with Faster-Whisper and Groq.

## What it does

- **Listens** to your voice and transcribes it with Faster-Whisper
- **Answers** with AI responses from Groq
- **Speaks** its replies with ElevenLabs text-to-speech
- **Opens** applications by voice command
- **Navigates** to websites by voice command

The code is split into separate modules: `listen.py`, `brain.py`, `router.py`, `voice.py` and `tools/`.

## Technologies

- Python
- Faster-Whisper
- Groq API
- ElevenLabs API
- SoundDevice
- SoundFile

## Setup

1. Clone this repository.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add:

   ```
   GROQ_API_KEY=your_groq_api_key
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   ```

4. Run the assistant:

   ```bash
   python main.py
   ```

## Note

This project is under active development.

## Author

Abhyuday Singh Parihar, The Daly College, Indore
