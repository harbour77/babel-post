from django.test import SimpleTestCase
from unittest.mock import patch

# Create your tests here.

from babel.services import get_google_translation
from babel.tests.utils import Consts

class test_translation_service(SimpleTestCase):

    @patch('babel.services.translate')
    def test_get_google_translation_with_different_languges(self, mock_translator):
        mock_translator.Client().translate.return_value = Consts.TRANSLATION_RETURN_VALUE
        val=get_google_translation(Consts.SOURCE_LANGUAGE_EN, Consts.TARGET_LANGUAGE_EN, Consts.NATIVE_TEXT)
        
        mock_translator.Client().translate.assert_called_once()
        self.assertEqual(val, Consts.TRANSLATED_TEXT)
    
    @patch('babel.services.translate')
    def test_get_google_translation_with_same_languge(self, mock_translator):
        val=get_google_translation(Consts.SOURCE_LANGUAGE_EN, Consts.SOURCE_LANGUAGE_EN, Consts.NATIVE_TEXT)
        
        mock_translator.Client().translate.assert_not_called()
        self.assertEqual(val, Consts.NATIVE_TEXT)
