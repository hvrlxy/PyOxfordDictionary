import json
from matplotlib.ft2font import ITALIC
import requests
from color import *

class Entry:
    def __init__(self, app_id, app_key, word_id, language_code: str):
        self.app_id = app_id 
        self.app_key = app_key
        self.word_id = word_id
        self.language_code = language_code
        self.json_obj = self.get_word_from_api()


    def get_word_from_api(self):
        '''
        Gets word from Oxford API.
        :return: json object
        '''
        
        url = "https://od-api.oxforddictionaries.com/api/v2/" + 'entries' + "/" + self.language_code + "/" + self.word_id.lower()
        r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})
        obj = json.loads(r.text)

        return obj 

    def get_word_definitions(self):
        '''
        Gets word definitions from Oxford API.
        :return: list of definitions as strings
        '''
        return self.json_obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']

    def get_word_synonyms(self):
        '''
        Gets word synonyms from Oxford API.
        :return: list of synonyms as strings
        '''

        synonyms = self.json_obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
        synonyms_list = []
        for synonym in synonyms:
            synonyms_list.append(synonym['text'])
        return synonyms_list

    def get_word_examples(self):
        '''
        Gets word examples from Oxford API.
        :return: list of examples as strings
        '''
        
        examples = self.json_obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples']
        examples_list = []
        for example in examples:
            examples_list.append(example['text'])
        return examples_list

    def get_word_subsense_definitions(self):
        '''
        Gets word subsense definitions from Oxford API.
        :return: list of definitions as strings
        '''
        try:
            subsenses = self.json_obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]
            return subsenses['definitions']
        except:
            return []

    def get_word_subsenses_examples(self):
        '''
        Gets word subsense examples from Oxford API.
        :return: list of examples as strings
        '''

        try:
            subsenses = self.json_obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]
            return [example['text'] for example in subsenses[self.word_id]]
        except:
            return []

    def get_word_etymologies(self):
        '''
        Gets word etymologies from Oxford API.
        :return: string
        '''
        return self.json_obj['results'][0]['lexicalEntries'][0]['entries'][0]['etymologies'][0]

    def get_word_pronunciations(self):
        '''
        Gets word pronunciations from Oxford API.
        :return: list of pronunciations as strings
        '''

        pronunciations = self.json_obj['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations']
        # print(pronunciations)
        pronunciations_list = []
        for pronunciation in pronunciations:
            pronunciations_list.append(pronunciation['phoneticSpelling'])
        return pronunciations_list

    def get_word_short_definition(self):
        '''
        Gets word short definition from Oxford API.
        :return: string
        '''
        return self.json_obj['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['shortDefinitions'][0]

    def get_word_lexical_category(self):
        '''
        Gets word lexical category from Oxford API.
        :return: string'''
        return self.json_obj['results'][0]['lexicalEntries'][0]['lexicalCategory']['id']

    def get_basic_word_info(self):
        '''
        Gets basic word info from Oxford API.
        :print: basic word info as string
        '''

        shortDefinition = self.get_word_short_definition()
        pronunciation = self.get_word_pronunciations()[0]
        synonyms = self.get_word_synonyms()
        lexicalCategories = self.get_word_lexical_category()

        print(color.BOLD + color.RED + self.word_id.upper() + color.END + color.ITALICS + ' [' + pronunciation + '] ' + color.END + ': ' + '(' + lexicalCategories + ') ' + shortDefinition + '\n' + color.BOLD + 'Synonyms: ' + color.END, ', '.join([str(elem) for elem in synonyms]) + '.')

    def get_word_phrases(self):
        '''
        Gets word phrases from Oxford API.
        :return: list of phrases as strings
        '''

        phrases = self.json_obj['results'][0]['lexicalEntries'][0]['phrases']
        phrases_list = []
        for phrase in phrases:
            phrases_list.append(phrase['text'])
        return phrases_list

    def testing_function(self):
        '''
        Testing function.
        :return: None
        '''

        examples = self.json_obj['results'][0]['lexicalEntries'][0]['text']
        return examples