from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Read API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Check that the keys exist
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY not found in .env file")