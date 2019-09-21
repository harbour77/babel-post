from google.cloud import translate

 
def get_google_translation(source_language, target_language, text):

    if source_language == target_language:
        return text

    # Instantiates a client
    translate_client = translate.Client()

    # Translate text
    try:
        translation = translate_client.translate(
            text,
            source_language=source_language,
            target_language=target_language)['translatedText']
    except:
        translation = 'Transaltion error from {} to {}.'.format(source_language, target_language)
    
    return translation

