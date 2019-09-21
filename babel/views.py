from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.timezone import now

from babel.models import *
from babel import services

enable_translation = True

# Dafault page, redirects to the language page
# Request example: /
def view_index(request):
  return redirect(view_language, label='English')

# Language page, shows recent messages in the selected language
# Request example: /English/
def view_language(request, label):

  try:
    language = Language.objects.get(lang_english=label)
  except Language.DoesNotExist:
    language, _ = Language.objects.get_or_create(lang_english='English', defaults={'lang_native': 'English', 'lang_iso': 'en'})

  languages = Language.objects.all()[:20]

  messages = Message.objects.all().order_by('-timestamp')[:10]

  dmessages = []
  for message in reversed(messages):
    dmessage = {}
    dmessage['timestamp'] = message.timestamp
    if enable_translation:
      dmessage['translated_text'] = Translation.get_translated_message(message, language) 
      dmessage['note'] = "Originally written in "+message.lang_native.lang_english
    else:
      dmessage['translated_text'] = message.text_native
      dmessage['note'] = "Translation disabled"

    dmessages.append(dmessage) 
  return render(
    request,
    'babel/index.html',
    {
      'messages': dmessages,
      'languages': languages,
      'chosen_language': language,
    })

# New message posting, this is triggered when the user clicks the Post button
# Request example: /postmessage/English/
def view_postmessage(request, label):
  try:
    language = Language.objects.get(lang_english=label)
  except Language.DoesNotExist:
    # This can only happen if someone is hacking the app
    return redirect(view_language, label='English')

  message_text_raw = request.POST['message_text']
  message = Message(timestamp=now(), text_native=message_text_raw, lang_native=language)
  message.save()
  return redirect(view_language, label=language.lang_english)

