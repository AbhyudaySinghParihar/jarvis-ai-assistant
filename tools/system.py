import subprocess
import string


def open_app(app_name):
    # Clean up the app name
    app = app_name.lower().strip()
    app = app.translate(str.maketrans('', '', string.punctuation))

    apps = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "cmd": "cmd.exe",
    }

    if app in apps:
        try:
            subprocess.Popen(apps[app])
            return f"Opening {app}."
        except Exception as e:
            return f"Couldn't open {app}: {e}"

    return f"I don't know how to open {app} yet."