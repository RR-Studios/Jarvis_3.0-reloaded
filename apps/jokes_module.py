import requests

def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/random")
        joke_data = response.json()
        if "setup" in joke_data and "punchline" in joke_data:
            setup = joke_data["setup"]
            punchline = joke_data["punchline"]
            return f"{setup}\n{punchline}"
        else:
            return "Sorry, I couldn't fetch a joke right now."
    except Exception as e:
        print(str(e))
        return "Sorry, I couldn't fetch a joke right now."
