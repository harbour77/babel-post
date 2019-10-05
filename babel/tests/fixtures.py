from babel.tests.utils import Consts, RunOnce

from babel.models import Language

class FixtureLanguages:

    @classmethod
    @RunOnce
    def init_languages(cls):

        cls.SOURCE_LANGUAGE = Language(
            lang_native = Consts.SOURCE_LANGUAGE_NAT,
            lang_english = Consts.SOURCE_LANGUAGE_EN,
            lang_iso = Consts.SOURCE_LANGUAGE_ISO
        )
        cls.SOURCE_LANGUAGE.save()

        cls.TARGET_LANGUAGE = Language(
            lang_native = Consts.TARGET_LANGUAGE_NAT,
            lang_english = Consts.TARGET_LANGUAGE_EN,
            lang_iso = Consts.TARGET_LANGUAGE_ISO
        )
        cls.TARGET_LANGUAGE.save()


from babel.models import Message
from django.utils import timezone

class FixtureMessages:

    @classmethod
    @RunOnce
    def init_messages(cls):

        FixtureLanguages.init_languages()
    
        cls.MESSAGE = Message(
            timestamp = timezone.now(),
            text_native = Consts.NATIVE_TEXT,
            lang_native = FixtureLanguages.SOURCE_LANGUAGE
        )
        cls.MESSAGE.save()
    
