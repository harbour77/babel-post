from babel.tests.utils import consts

from babel.models import Language
from babel.models import Message

class fixture_languages:

    __inited = False

    @classmethod
    def init_languages(fixture_languages):

        if fixture_languages.__inited:
            return

        fixture_languages.__inited = True

        fixture_languages.SOURCE_LANGUAGE = Language(
            lang_native = consts.SOURCE_LANGUAGE_NAT,
            lang_english = consts.SOURCE_LANGUAGE_EN,
            lang_iso = consts.SOURCE_LANGUAGE_ISO
        )
        fixture_languages.SOURCE_LANGUAGE.save()

        fixture_languages.TARGET_LANGUAGE = Language(
            lang_native = consts.TARGET_LANGUAGE_NAT,
            lang_english = consts.TARGET_LANGUAGE_EN,
            lang_iso = consts.TARGET_LANGUAGE_ISO
        )
        fixture_languages.TARGET_LANGUAGE.save()


from django.utils import timezone

class fixture_messages:

    @classmethod
    def init_messages(fixture_messages):
    
        fixture_languages.init_languages()
    
        fixture_messages.MESSAGE = Message(
            timestamp = timezone.now(),
            text_native = consts.NATIVE_TEXT,
            lang_native = fixture_languages.SOURCE_LANGUAGE
            
            #  Language.objects.get_or_create(
            #     lang_native = consts.TARGET_LANGUAGE_NAT,
            #     lang_english = consts.TARGET_LANGUAGE_EN,
            #     lang_iso = consts.TARGET_LANGUAGE_ISO
            # )
            # 
        )
        fixture_messages.MESSAGE.save()
    
