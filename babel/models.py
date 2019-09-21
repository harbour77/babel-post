from django.db import models
from google.cloud import translate
from babel.services import *

class Language(models.Model):
    # the language name in the original language, e.g. 'Magyar'
    lang_native = models.CharField(max_length=30, unique=True)
    # the language name in English, e.g. 'Hungarian'
    lang_english = models.CharField(max_length=30, unique=True)
    # ISO 639-1 code of teh language
    lang_iso = models.CharField(max_length=2, unique=True, default='en')
    
    def __str__(self):
        return 'Language: '+self.lang_english


class Message(models.Model):
    timestamp = models.DateTimeField()
    text_native = models.TextField()
    lang_native = models.ForeignKey(Language, on_delete=models.PROTECT)
    
    def __str__(self):
        return 'Message: '+self.text_native[0:40]+'...'


class Translation(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    lang_target = models.ForeignKey(Language, on_delete=models.PROTECT)
    text_translated = models.TextField()

    class Meta:
        unique_together = ('message', 'lang_target')


    @classmethod
    def get_translated_message (translation, message, target_language):

        if message.lang_native.lang_iso == target_language.lang_iso:
            return message.text_native

        translation, _ = translation.objects.get_or_create(
            message = message,
            lang_target = target_language,
            defaults = {'text_translated': lambda : get_google_translation(
                source_language = message.lang_native.lang_iso,
                target_language = target_language.lang_iso,
                text = message.text_native
            )})
    
        return translation.text_translated

