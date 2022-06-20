import json
from matplotlib.ft2font import ITALIC
import requests
from color import *

class Utilities:
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_domains_monolingual(self, source_lang: str):
        '''
        Lists available domains in a monolingual dataset
        :param source_land: string
        :return: list of domains as strings
        '''

        url = 'https://od-api.oxforddictionaries.com/api/v2/domains/' + source_lang.lower()
        headers = {'app_id': self.app_id, 'app_key': self.app_key}
        r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
        obj = json.loads(r.text)

        results = []
        for word in obj['results'].keys():
            for entry in obj['results'][word]:
                results.append(obj['results'][word][entry])

        return results

    def get_domains_bilingual(self, source_lang: str, target_lang: str):
        url = 'https://od-api.oxforddictionaries.com/api/v2/domains/' + source_lang.lower() + '/' + target_lang.lower()
        headers = {'app_id': self.app_id, 'app_key': self.app_key}
        r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
        obj = json.loads(r.text)

        results = []
        for word in obj['results'].keys():
            for entry in obj['results'][word]:
                results.append(obj['results'][word][entry])

        return results

    def get_all_languages(self, source_lang: str = None, target_lang: str = None):
        '''
        Lists all available languages
        :param source_lang: string (default: None)
        :param target_lang: string (default: None)
        :return: dictionary of languages
        '''
        url = 'https://od-api.oxforddictionaries.com/api/v2/languages'
        if source_lang is not None:
            url += '?sourceLanguage=' + source_lang.lower()
        if target_lang is not None:
            url += '&targetLanguage=' + target_lang.lower()

        headers = {'app_id': self.app_id, 'app_key': self.app_key}
        r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
        obj = json.loads(r.text)

        return obj['results'][0]

