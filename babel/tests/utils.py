class Consts:
    SOURCE_LANGUAGE_EN = 'SL'
    TARGET_LANGUAGE_EN = 'TL'
    NATIVE_TEXT = 'native text'
    TRANSLATED_TEXT = 'translated text'
    TRANSLATION_RETURN_VALUE = {'translatedText': TRANSLATED_TEXT}

    SOURCE_LANGUAGE_NAT = 'SLN'
    TARGET_LANGUAGE_NAT = 'TLN'

    SOURCE_LANGUAGE_ISO = 'sl'
    TARGET_LANGUAGE_ISO = 'tl'


class RunOnce:
    def __init__(self, func):
        self.func = func
        self.ran = False

    def __call__(self, *args):
        if not self.ran:
            self.func(*args)
            self.ran = True
