import json
from matplotlib.ft2font import ITALIC
import requests
from color import *

class OxfordUser:
    def __init__(self, app_id: str, app_key: str, endpoint: str, language_code: str):
        '''
        Initializes OxfordUser object.
        :param app_id: Oxford API app_id
        :param app_key: Oxford API app_key
        :param endpoint: Oxford API endpoint
        :param language_code: Oxford API language code
        '''

        self.app_id = app_id 
        self.app_key = app_key
        self.endpoint = endpoint
        self.language_code = language_code


    def get_word_from_api(self, word_id: str):
        '''
        Gets word from Oxford API.
        :param word_id: string
        :return: json object
        '''
        
        url = "https://od-api.oxforddictionaries.com/api/v2/" + self.endpoint + "/" + self.language_code + "/" + word_id.lower()
        r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
        obj = json.loads(r.text)

        return obj 

    def get_word_definitions(self, word_id: str):
        '''
        Gets word definitions from Oxford API.
        :param word_id: string
        :return: list of definitions as strings
        '''

        obj = self.get_word_from_api(word_id)
        return obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']

    def get_word_synonyms(self, word_id: str):
        '''
        Gets word synonyms from Oxford API.
        :param word_id: string
        :return: list of synonyms as strings
        '''

        obj = self.get_word_from_api(word_id)
        synonyms = obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
        synonyms_list = []
        for synonym in synonyms:
            synonyms_list.append(synonym['text'])
        return synonyms_list

    def get_word_examples(self, word_id: str):
        '''
        Gets word examples from Oxford API.
        :param word_id: string
        :return: list of examples as strings
        '''
        
        obj = self.get_word_from_api(word_id)
        examples = obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples']
        examples_list = []
        for example in examples:
            examples_list.append(example['text'])
        return examples_list

    def get_word_subsense_definitions(self, word_id: str):
        '''
        Gets word subsense definitions from Oxford API.
        :param word_id: string
        :return: list of definitions as strings
        '''
        obj = self.get_word_from_api(word_id)
        subsenses = obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]
        return subsenses['definitions']

    def get_word_subsenses_examples(self, word_id: str):
        '''
        Gets word subsense examples from Oxford API.
        :param word_id: string
        :return: list of examples as strings
        '''
        
        obj = self.get_word_from_api(word_id)
        subsenses = obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]
        return [example['text'] for example in subsenses['examples']]

    def get_word_etymologies(self, word_id: str):
        '''
        Gets word etymologies from Oxford API.
        :param word_id: string
        :return: string
        '''

        obj = self.get_word_from_api(word_id)
        return obj['results'][0]['lexicalEntries'][0]['entries'][0]['etymologies'][0]

    def get_word_pronunciations(self, word_id:str):
        '''
        Gets word pronunciations from Oxford API.
        :param word_id: string
        :return: list of pronunciations as strings
        '''

        obj = self.get_word_from_api(word_id)
        pronunciations = obj['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations']
        # print(pronunciations)
        pronunciations_list = []
        for pronunciation in pronunciations:
            pronunciations_list.append(pronunciation['phoneticSpelling'])
        return pronunciations_list

    def get_word_short_definition(self, word_id: str):
        '''
        Gets word short definition from Oxford API.
        :param word_id: string
        :return: string
        '''
        obj = self.get_word_from_api(word_id)
        return obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['shortDefinitions'][0]

    def get_word_lexical_category(self, word_id: str):
        obj = self.get_word_from_api(word_id)
        return obj['results'][0]['lexicalEntries'][0]['lexicalCategory']['id']

    def get_basic_word_info(self, word_id: str):
        '''
        Gets basic word info from Oxford API.
        :param word_id: string
        :print: basic word info as string
        '''

        obj = self.get_word_from_api(word_id)
        shortDefinition = self.get_word_short_definition(word_id)
        pronunciation = self.get_word_pronunciations(word_id)[0]
        synonyms = self.get_word_synonyms(word_id)
        lexicalCategories = self.get_word_lexical_category(word_id)

        print(color.BOLD + color.RED + word_id.upper() + color.END + color.ITALICS + ' [' + pronunciation + '] ' + color.END + ': ' + '(' + lexicalCategories + ') ' + shortDefinition + '\n' + color.BOLD + 'Synonyms: ' + color.END, ', '.join([str(elem) for elem in synonyms]) + '.')

    def get_word_phrases(self, word_id: str):
        '''
        Gets word phrases from Oxford API.
        :param word_id: string
        :return: list of phrases as strings
        '''

        obj = self.get_word_from_api(word_id)
        phrases = obj['results'][0]['lexicalEntries'][0]['phrases']
        phrases_list = []
        for phrase in phrases:
            phrases_list.append(phrase['text'])
        return phrases_list

    def testing_function(self, word_id: str):
        '''
        Testing function.
        :param word_id: string
        :return: None
        '''

        obj = self.get_word_from_api(word_id)
        examples = obj['results'][0]['lexicalEntries'][0]['text']
        return examples
#test
# new_user = OxfordUser("095b45f9", "9f1a4d772984fe91944ebd830eb961c4", "entries", "en-us")
# print(new_user.get_word_definitions('dog'))