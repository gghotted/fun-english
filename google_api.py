from google.cloud import translate_v2 as translate


client = translate.Client()


def translate(input_text, target_language='en'):
    response = client.translate(
        input_text,
        target_language=target_language
    )
    return response


