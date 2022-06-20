import json
import requests

class Lemma:
    def __init__(self, app_id, app_key, language_code, word_id):
        self.app_id = app_id
        self.app_key = app_key
        self.language_code = language_code
        self.word_id = word_id

        self.json_obj = self.get_lemma_from_api()

    def get_lemma_from_api(self):
        '''
        Gets lemma from Oxford API.
        :return: json object'''
        url = "https://od-api.oxforddictionaries.com/api/v2/" + 'lemmas' + "/" + self.language_code + "/" + self.word_id.lower()
        r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})

        obj = json.loads(r.text)
        return obj

    def get_word_inflections(self):
        '''
        Gets word inflections from lemma json object.
        :return: list of inflections'''
        inflections = None
        try:
            inflections = self.json_obj['results'][0]['lexicalEntries']
        except:
            return []
        inflections_list = []
        for inflection in inflections:
            if 'inflectionOf' in inflection:
                inflections_list.append(WordLemma(inflection['inflectionOf'][0]['id'], inflection['lexicalCategory']['text']))
        return(inflections_list)

class WordLemma:
    def __init__(self, inflection, lexicalCategory):
        self.inflection = inflection
        self.lexicalCategory = lexicalCategory

    def __str__(self):
        return f'WordLemma({self.inflection},{self.lexicalCategory})'

    __repr__ = __str__