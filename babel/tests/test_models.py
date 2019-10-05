from django.test import TestCase
from unittest.mock import patch

# Create your tests here.

from babel.models import Translation

from babel.tests.fixtures import FixtureLanguages, FixtureMessages
from babel.tests.utils import Consts

class test_translation_model(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        FixtureLanguages.init_languages()
        FixtureMessages.init_messages()

      
    @patch('babel.models.get_google_translation')    
    def test_translation_get_translated_message_different_languges(self, mock_translator):

        mock_translator.return_value = Consts.TRANSLATED_TEXT
        translation_result_1 = Translation.get_translated_message(FixtureMessages.MESSAGE, FixtureLanguages.TARGET_LANGUAGE)
        translation_result_2 = Translation.get_translated_message(FixtureMessages.MESSAGE, FixtureLanguages.TARGET_LANGUAGE)

        self.assertEqual(translation_result_1, Consts.TRANSLATED_TEXT)
        self.assertEqual(translation_result_2, Consts.TRANSLATED_TEXT)
        mock_translator.assert_called_once()

    @patch('babel.models.get_google_translation')    
    def test_translation_get_translated_message_same_languge(self, mock_translator):

        mock_translator.return_value = Consts.TRANSLATED_TEXT
        translation_result = Translation.get_translated_message(FixtureMessages.MESSAGE, FixtureLanguages.SOURCE_LANGUAGE)

        self.assertEqual(translation_result, FixtureMessages.MESSAGE.text_native)
        mock_translator.assert_not_called()
