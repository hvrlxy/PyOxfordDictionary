import pytest
from PyOxfordDictionary.user import *

new_user = OxfordUser("<app-id>", ",app-key>")

def test_word_definitions():
    assert new_user.get_word_definitions('dog') == ['a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice.']

def test_word_pronunciations():
    assert new_user.get_word_pronunciations('dog') == ['dôɡ', 'dɔɡ']

def test_word_synonyms():
    assert new_user.get_word_synonyms('dog') == ['canine', 'hound']

def test_word_examples():
    assert new_user.get_word_examples('abase') == ['I watched my colleagues abasing themselves before the board of trustees']

def test_word_subsenses_examples():
    assert new_user.get_word_subsenses_examples('dog') == []

def test_word_subsenses_definitions():
    assert new_user.get_word_subsense_definitions('dog') == ['a wild animal of the dog family.']