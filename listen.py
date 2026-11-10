import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
from faster_whisper import WhisperModel

# Load the Whisper model once when the program starts
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

def listen():
    sample_rate = 16000
    seconds = 5

    print("🎤 Listening...")

    recording = sd.rec(
        int(seconds * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(temp.name, sample_rate, recording)

    print("🧠 Processing speech...")

    segments, _ = model.transcribe(temp.name)

    text = ""

    for segment in segments:
        text += segment.text

    text = text.strip()

    print(f"You said: {text}")

    return text