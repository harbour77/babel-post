from django.test import TestCase
from unittest.mock import patch

# Create your tests here.

from babel.models import Translation

from babel.tests.fixtures import fixture_languages, fixture_messages
from babel.tests.utils import consts

class test_translation_model(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        fixture_languages.init_languages()
        fixture_messages.init_messages()

      
    @patch('babel.models.get_google_translation')    
    def test_translation_get_translated_message_different_languges(self, mock_translator):

        mock_translator.return_value = consts.TRANSLATED_TEXT
        translation_result_1 = Translation.get_translated_message(fixture_messages.MESSAGE, fixture_languages.TARGET_LANGUAGE)
        translation_result_2 = Translation.get_translated_message(fixture_messages.MESSAGE, fixture_languages.TARGET_LANGUAGE)

        self.assertEqual(translation_result_1, consts.TRANSLATED_TEXT)
        self.assertEqual(translation_result_2, consts.TRANSLATED_TEXT)
        mock_translator.assert_called_once()

    @patch('babel.models.get_google_translation')    
    def test_translation_get_translated_message_same_languge(self, mock_translator):

        mock_translator.return_value = consts.TRANSLATED_TEXT
        translation_result = Translation.get_translated_message(fixture_messages.MESSAGE, fixture_languages.SOURCE_LANGUAGE)

        self.assertEqual(translation_result, fixture_messages.MESSAGE.text_native)
        mock_translator.assert_not_called()
