import json
from matplotlib.ft2font import ITALIC
import requests
from PyOxfordDictionary.color import *

class Sentences:
    def __init__(self, app_id, app_key, source_lang: str, word_id: str, strict_match = False):
        self.app_id = app_id
        self.app_key = app_key
        self.source_lang = source_lang
        self.word_id = word_id
        self.strict_match = strict_match

    def get_sentences(self):
        '''
        Retrieves sentences from Oxford API.
        :param target_lang: string
        :param limit: int (default = 500)
        :return: list of sentences as strings
        '''
        url = 'https://od-api.oxforddictionaries.com:443/api/v2/sentences/' + self.source_lang + '/' + self.word_id.lower()
        if self.strict_match:
            url += '?strictMatch=true'

        r = requests.get(url, headers = {'app_id': self.app_id, 'app_key': self.app_key})
        obj = json.loads(r.text)

        sentences = []
        for sentence in obj['results'][0]['lexicalEntries'][0]['sentences']:
            sentences.append(sentence['text'])

        return sentences
