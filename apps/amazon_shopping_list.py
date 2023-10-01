import pyttsx3

def speak_shopping_list(shopping_list):
    engine = pyttsx3.init('sapi5')
    engine.say("Here is your Amazon shopping list:")
    for item in shopping_list:
        engine.say(item)
    engine.runAndWait()

def get_amazon_shopping_list():

    shopping_list = [
        "Item 1",
        "Item 2",
        "Item 3",
    ]
    return shopping_list
