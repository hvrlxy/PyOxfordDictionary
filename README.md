# PyOxfordDictionary

This repository contains the Python Wrapper for the Oxford Dictionary API. The package is currently available for download in TestPyPi, and I will release the package on PyPi as soon as possible. To access the documentation of the package, click on the link below:

```
https://test.pypi.org/project/PyOxfordDictionary/0.0.2/
```

To download the package, type the line below into your Mac/Linux command line:

```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps PyOxfordDictionary
```

## Getting Started
To use the package, first you need to get an access token to the Oxford Dictionary API. To register for the application's id and key, follow the instruction in the website below:

```
https://developer.oxforddictionaries.com/
```

To start using the package, we need to declare the credentials:
```
>>> from PyOxfordDictionary.user import *
>>> user = OxfordUser('<app_id>', '<app_key>')
```

After that, we can start exploring different functionalities of the API.

## Entries
The first and most common endpoint used is **entries**. We can "use this to retrieve definitions, pronunciations, example sentences, grammatical information and word origins." For more information, you can read it on [the API's main website](https://developer.oxforddictionaries.com/documentation#!/Entries/get_entries_source_lang_word_id).

These are the function supported in this wrapper:
- get_word_definitions(): give a list of all the definitions of the word
- get_word_synonyms(): return a list of possible synonyms of the word
- get_word_examples(): return a list of possible example usage of the word
- get_word_subsense_definitions(): return a list of possible subsenses' definitions of the word
- get_word_subsenses_examples(): return a list of possible subsenses' examples of the word
- get_word_etymologies(): return the etymologies of the word
- get_word_pronunciations(): return possible pronunciations of the word
- get_word_short_definition(): return the short definition of the word
- get_word_lexical_category(): return possible lexical categories of the word (noun, verb, ...)
- get_basic_word_info(): print out basic information of the word
- get_word_phrases(): return common phrases associated with the word

The snippet of code below shows an example use case of the endpoint

```
from PyOxfordDictionary.user import *
>>> user = OxfordUser('<app_id>', '<app_key>')
>>> cat_entry = user.get_entries(word_id = 'cat', language_code = 'en') #initialize the entry object
>>> cat_entry.get_word_definitions()
['a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed.']
>>> cat_entry.get_word_synonyms()
['feline']
>>> cat_entry.get_word_pronunciations()
['kat']
```

## Lemmas
The endpoint **lemma** is used to check whether a word exists in the given dictionary and identify its root. This package only supports one function:
- get_word_inflections(): check a word exists in the dictionary and retrieve its root form

```
>>> cat_lemma = user.get_lemma('en', 'cat')
>>> cat_lemma.get_word_inflections()
[]
```

## Search
The endpoint **search** is used to find possible translation and synonyms of a given word in the dictionary. This package supports 3 main functions:
- get_headwords(): Find all possible headwords of the given strings
- get_dictionary_match(): Use this to retrieve possible headword matches for a given string of text. The results are calculated using headword matching, fuzzy matching, and lemmatization.
- get_thesaurus_match(): Use this to retrieve possible headword matches for a given string of text. The results are calculated using headword matching, fuzzy matching, and lemmatization.

```
>>> from PyOxfordDictionary.user import *
>>> user = OxfordUser('<app_id>', '<app_key>')
>>> cat_search = user.get_search()
>>> cat_search.get_headwords(source_lang = 'en', target_lang = 'ar', word_id='computer', prefix = True, limit = 20)
['computer', 'computer crime', 'computer dating', 'computer engineer', 'computer game', 'computer graphics', 'computer hacker', 'computer program', 'computer programmer', 'computer programming', 'computer science', 'computer scientist', 'computer studies', 'computer-aided design', 'computer-aided learning', 'computer-literate', 'computerize']
```








