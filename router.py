from tools.system import open_app
from tools.browser import open_website


def handle_command(command):
    command = command.lower().strip()

    print("Command:", command)

    if command.startswith("open "):
        thing = command.replace("open ", "", 1).strip()

        print("Thing:", thing)

        response = open_website(thing)

        print("Website response:", response)

        if response:
            return response

        return open_app(thing)

    return None