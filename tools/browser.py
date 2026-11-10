import webbrowser
import string

def open_website(site):
    # Convert to lowercase and remove punctuation
    site = site.lower().strip()
    site = site.translate(str.maketrans('', '', string.punctuation))

    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "chatgpt": "https://chat.openai.com",
    }

    if site in websites:
        webbrowser.open(websites[site])
        return f"Opening {site}."

    return None