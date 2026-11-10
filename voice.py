from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY

import sounddevice as sd
import soundfile as sf
import io

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)


def speak(text):
    print(f"Jarvis: {text}")

    audio_stream = client.text_to_speech.convert(
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        text=text
    )

    audio_bytes = b"".join(audio_stream)

    data, samplerate = sf.read(io.BytesIO(audio_bytes))

    sd.play(data, samplerate)
    sd.wait()