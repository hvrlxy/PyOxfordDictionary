import json
from matplotlib.ft2font import ITALIC
import requests
from color import *
from entries import Entry

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
        :return: json object
        '''
        return Entry(self.app_id, self.app_key, word_id, language_code)

