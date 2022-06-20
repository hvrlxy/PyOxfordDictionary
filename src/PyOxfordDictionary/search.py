import json
from matplotlib.ft2font import ITALIC
import requests
from color import *

class Search:
    def __init__(self, app_id, app_key) -> None:
        self.app_id = app_id
        self.app_key = app_key

    def get_headwords(self, source_lang: str, target_lang: str, 
                        word_id: str, prefix = True, limit = 500):
        
        '''
        Retrieves possible headwords with translations
        :param source_lang: string
        :param target_lang: string
        :param word_id: string
        :param prefix: boolean (default: True)
        :param limit: int (default = 500)
        :return: list of headwords as strings
        '''

        url = "https://od-api.oxforddictionaries.com/api/v2/search/translations/" + source_lang.lower() + "/" + target_lang.lower() + "?" + 'q=' + word_id.lower()
        if prefix:
            url += '&prefix=true'
        if limit != 500:
            url += '&limit=' + str(limit)
        r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
        obj = json.loads(r.text)

        headwords = []
        for headword in obj['results']:
            headwords.append(headword['word'])

        return headwords

    def get_dictionary_match(self, source_lang: str, word_id: str, prefix = False, limit=500):
        '''
        Retrieves possible dictionary matches with translations
        :param source_lang: string
        :param word_id: string
        :param prefix: boolean (default: False)
        :param limit: int (default = 500)
        :return: list of dictionary matches as strings
        '''
        
        url = "https://od-api.oxforddictionaries.com/api/v2/search/thesaurus/" + source_lang.lower() + "?" + 'q=' + word_id.lower()
        if prefix:
            url += '&prefix=true'
        if limit != 500:
            url += '&limit=' + str(limit)
        r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
        obj = json.loads(r.text)

        matches = []
        for match in obj['results']:
            matches.append(match['word'])

        return matches

    def get_thesaurus_match(self, source_lang: str, word_id: str, prefix = False, limit = 500):
        '''
        Retrieves possible thesaurus matches with translations
        :param source_lang: string
        :param word_id: string
        :param prefix: boolean (default: False)
        :param limit: int (default = 500)
        :return: list of thesaurus matches as strings
        '''
        
        url = "https://od-api.oxforddictionaries.com/api/v2/search/thesaurus/" + source_lang.lower() + "?" + 'q=' + word_id.lower()
        if prefix:
            url += '&prefix=true'
        if limit != 500:
            url += '&limit=' + str(limit)
        r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
        obj = json.loads(r.text)

        matches = []
        for match in obj['results']:
            matches.append(match['word'])

        return matches
