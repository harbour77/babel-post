from django.test import SimpleTestCase, TestCase
from unittest.mock import patch

# Create your tests here.

from babel.services import get_google_translation

class test_translation_service(SimpleTestCase):

    SOURCE_LANGUAGE = 'SL'
    TARGET_LANGUAGE = 'TL'
    TRANSLATION_TEXT = 'T'
    TRANSLATION_RESULT = 'OK'
    TRANSLATION_RETURN_VALUE = {'translatedText': TRANSLATION_RESULT}

    @patch('babel.services.translate')
    def test_get_google_translation_with_different_languges(self, mock_translator):
        mock_translator.Client().translate.return_value = self.TRANSLATION_RETURN_VALUE
        val=get_google_translation(self.SOURCE_LANGUAGE, self.TARGET_LANGUAGE, self.TRANSLATION_TEXT)
        
        mock_translator.Client().translate.assert_called_once()
        self.assertEqual(val, self.TRANSLATION_RESULT)
    
    @patch('babel.services.translate')
    def test_get_google_translation_with_same_languge(self, mock_translator):
        val=get_google_translation(self.SOURCE_LANGUAGE, self.SOURCE_LANGUAGE, self.TRANSLATION_TEXT)
        
        mock_translator.Client().translate.assert_not_called()
        mock_translator.Client().translate.assert_not_called()
        self.assertEqual(val, self.TRANSLATION_TEXT)        
