import unittest
from src.translator import translate_text

class TestTranslator(unittest.TestCase):

    def test_translate_text(self):
        """Test the translation functionality."""
        english_text = "Hello, world!"
        translated_text = translate_text(english_text, dest_lang='es', src_lang='en')
        self.assertEqual(translated_text.lower(), "¡hola mundo!")

    def test_translate_to_arabic(self):
        """Test translation to Arabic."""
        english_text = "Hello"
        arabic_text = translate_text(english_text, dest_lang='ar', src_lang='en')
        self.assertEqual(arabic_text, "مرحبا")

if __name__ == '__main__':
    unittest.main()