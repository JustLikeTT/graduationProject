from google.cloud import translate

def translate_text(text, target):
    
    translate_client = translate.Client()
    translation = translate_client.translate(
        text,
        target_language=target)

    return u'Translation: {}'.format(translation['translatedText'])

if __name__ == '__main__':

    print(translate_text("cat.", "zh"))