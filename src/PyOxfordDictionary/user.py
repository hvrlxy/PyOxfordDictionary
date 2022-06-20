import json
from matplotlib.ft2font import ITALIC
import requests
from PyOxfordDictionary.color import *
from PyOxfordDictionary.entries import Entry
from PyOxfordDictionary.lemmas import *
from PyOxfordDictionary.sentences import *
from PyOxfordDictionary.search import *

class OxfordUser:
    def __init__(self, app_id: str, app_key: str):
        '''
        Initializes OxfordUser object.
        :param app_id: Oxford API app_id
        :param app_key: Oxford API app_key
        :param endpoint: Oxford API endpoint
        :param language_code: Oxford API language code
        '''

        self.app_id = app_id 
        self.app_key = app_key


    def get_entries(self, word_id: str, language_code: str):
        '''
        Gets entries from Oxford API.
        :param word_id: string
        :return: Entries object
        '''
        return Entry(self.app_id, self.app_key, word_id, language_code)

    def get_lemma(self, word_id: str, language_code: str):
        '''
        Gets lemma from Oxford API.
        :param language_code: string
        :param word_id: string
        :return: Lemma object
        '''
        return Lemma(self.app_id, self.app_key, language_code, word_id)

    def get_sentences(self, word_id: str, language_code: str, strict_match: bool = False):
        '''
        Gets sentences from Oxford API.
        :param language_code: string
        :param word_id: string
        :param strict_match: bool (default = False)
        :return: Sentences object
        '''
        return Sentences(self.app_id, self.app_key, language_code, word_id, strict_match)

    def get_search(self):
        '''
        Gets search from Oxford API.
        :return: Search object
        '''
        return Search(self.app_id, self.app_key)

    def get_utility(self):
        '''
        Gets utility from Oxford API.
        :return: Utility object
        '''
        return Utility(self.app_id, self.app_key)