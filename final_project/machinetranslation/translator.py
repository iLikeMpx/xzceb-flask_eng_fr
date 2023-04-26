"""Module that contains the translation functions"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """function to translate english to french"""

    french_text = ''
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = french_text['translations'][0]['translation']

    return french_text

def frenchToEnglish(french_text):
    """function to tranlate french to english"""
    
    english_text = ''
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = english_text['translations'][0]['translation']

    return english_text
