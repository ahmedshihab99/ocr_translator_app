from googletrans import Translator
from utils.config import DESTINATION_LANGUAGE, SOURCE_LANGUAGE

def translate_text(text, dest_lang=DESTINATION_LANGUAGE, src_lang=SOURCE_LANGUAGE):
    """
    Translates text to the destination language.
    """
    if not text:
        return ""
    try:
        translator = Translator()
        translated = translator.translate(text, dest=dest_lang, src=src_lang)
        return translated.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return "Translation Error"