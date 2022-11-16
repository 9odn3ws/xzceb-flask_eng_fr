import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

# use .env file as source for API credentials
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create an Instance

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# Call Method list languages
'''
languages = language_translator.list_languages().get_result()
print(json.dumps(languages, indent=2))
'''


# function translation en-fr
def englishtofrench(englishtext=None):

    input_type = type(englishtext)
    type_string = type("String")

    if englishtext == "":
        return "Please enter a text."

    elif input_type == type_string:
        translation = language_translator.translate(
            text=[englishtext],
            model_id='en-fr').get_result()
        frenchtext = json.dumps(translation, indent=2, ensure_ascii=False)
        frenchtext = json.loads(frenchtext)
        frenchtext = frenchtext['translations'][0]['translation']

        return frenchtext

    else:
        return "a string is needed as input."


# function translation fr-en
def frenchtoenglish(frenchtext=None):

    input_type = type(frenchtext)
    type_string = type("String")

    if frenchtext == "":
        return "Please enter a text."

    elif input_type == type_string:
        translation = language_translator.translate(
            text=[frenchtext],
            model_id='fr-en').get_result()
        englishtext = json.dumps(translation, indent=2, ensure_ascii=False)
        englishtext = json.loads(englishtext)
        englishtext = englishtext['translations'][0]['translation']

        return englishtext

    else:
        return "a string is needed as input."


if __name__ == '__main__':
    print(englishtofrench("Hello, how are you today?"))
    print(frenchtoenglish("Bonjour, comment vous êtes aujourd'hui?"))
