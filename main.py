from listen import listen
from brain import ask_jarvis
from voice import speak
from router import handle_command


def main():
    print("=" * 50)
    print("🤖 JARVIS ONLINE")
    print("=" * 50)

    speak("Jarvis online. How can I help you, sir?")

    while True:
        try:
            text = listen()

            # Ignore empty recordings
            if not text:
                continue

            print(f"You: {text}")

            # Exit command
            if text.lower() in ["exit", "quit", "goodbye", "bye"]:
                speak("Goodbye, sir.")
                break

            # Try local commands first
            local_response = handle_command(text)

            if local_response is not None:
                speak(local_response)
                continue

            # Otherwise ask the AI
            response = ask_jarvis(text)
            speak(response)

        except KeyboardInterrupt:
            print("\nShutting down...")
            speak("Shutting down. Goodbye, sir.")
            break

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()