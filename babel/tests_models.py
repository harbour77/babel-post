from django.test import SimpleTestCase, TestCase
from unittest.mock import patch

# Create your tests here.

from babel.models import Translation, Message, Language

class test_translation_model(TestCase):
    LANG_1 = Language(lang_native = 'LN1', lang_english = 'LE1', lang_iso = 'i1')
    MESSAGE = Message()

    def test_translation_get_translated_message(self):
        pass
