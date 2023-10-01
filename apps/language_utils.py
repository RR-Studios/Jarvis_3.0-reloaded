import pyttsx3
from googletrans import Translator



def detect_language(text):
    try:
        translator = Translator()
        result = translator.detect(text)
        return result.lang
    except Exception as e:
        print(f"Error detecting language: {str(e)}")
        return 'en'  # Default to English if there's an error

def translate_text(text, target_lang):
    try:
        translator = Translator()
        translated_text = translator.translate(text, dest=target_lang)
        return translated_text.text
    except Exception as e:
        print(f"Error translating text: {str(e)}")
        return text  # Return the original text if there's an error
