# PyOxfordDictionary

This repository contains the Python Wrapper for the Oxford Dictionary API. The package is currently available for download in TestPyPi, and I will release the package on PyPi as soon as possible. To access the documentation of the package, click on the link below:

```
https://test.pypi.org/project/PyOxfordDictionary/0.0.8/
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
The endpoint **lemma** is used to check whether a word exists in the given dictionary and identify its root. This package only supports one function. For more information, read more at the official [API's main webpage](https://developer.oxforddictionaries.com/documentation#!/Search/get_search_translations_source_lang_search_target_lang_search).
- get_word_inflections(): check a word exists in the dictionary and retrieve its root form

The snippet of code below shows an example use case of the endpoint


```
>>> cat_lemma = user.get_lemma('en', 'cat')
>>> cat_lemma.get_word_inflections()
[]
```

## Search
The endpoint **search** is used to find possible translation and synonyms of a given word in the dictionary. This package supports 3 main functions. For more information, read more at the official [API's webpage](https://developer.oxforddictionaries.com/documentation#!/Search/get_search_translations_source_lang_search_target_lang_search).
- get_headwords(): Find all possible headwords of the given strings
- get_dictionary_match(): Use this to retrieve possible headword matches for a given string of text. The results are calculated using headword matching, fuzzy matching, and lemmatization.
- get_thesaurus_match(): Use this to retrieve possible headword matches for a given string of text. The results are calculated using headword matching, fuzzy matching, and lemmatization.

The snippet of code below shows an example use case of the endpoint


```
>>> from PyOxfordDictionary.user import *
>>> user = OxfordUser('<app_id>', '<app_key>')
>>> cat_search = user.get_search()
>>> cat_search.get_headwords(source_lang = 'en', target_lang = 'ar', word_id='computer', prefix = True, limit = 20)
['computer', 'computer crime', 'computer dating', 'computer engineer', 'computer game', 'computer graphics', 'computer hacker', 'computer program', 'computer programmer', 'computer programming', 'computer science', 'computer scientist', 'computer studies', 'computer-aided design', 'computer-aided learning', 'computer-literate', 'computerize']
```

## Sentences
The endpoint **sentences** is used to retrieve example sentence usage of a given word. This package only support one function. For more information, read more at the official [API's main webpage](https://developer.oxforddictionaries.com/documentation#!/Search/get_search_translations_source_lang_search_target_lang_search).

- get_sentences(): Use this to retrieve sentences extracted from a corpus of real-world language, including news and blog content. This is available for English and Spanish. For English, the sentences are linked to the correct sense of the word in the dictionary. In Spanish, they are linked at the headword level.

The snippet of code below shows an example use case of the endpoint

```
>>> from PyOxfordDictionary.user import *
>>> user = OxfordUser('<app_id>', '<app_key>')
>>> cat_sentence = user.get_sentences(word_id = 'computer', language_code = 'en', strict_match = False)
>>> cat_sentence.get_sentences()
['The laws were designed to prosecute people who hack into computers and steal information.', 'Patients will receive information through their computers on how to manage their disease.', 'The updated carriages also sport power sockets for notebook computers and other devices.', 'Participants scan the barcodes of every product they buy using a hand-held computer at home.', 'The four-page tabloids, little more than newsletters, materialized mainly because the editor used his personal computer at home.', 'I waited until a powerful laptop computer was under $1000 before buying it.', 'Clearly, not too many can afford to buy their own personal computers.', 'Perhaps the most compelling reason to buy a desktop computer is to get your choice of flat-panel displays.', 'Since then, the craft appears to have rebooted its own on-board computer more than 60 times.', 'The three desktop computers are connected to each other using Ethernet with a hub.', "I'd like to be able to access email remotely from the new notebook computer.", 'Such games hint at how best to program a quantum computer.', 'The missile was equipped with an autonomous inertial command structure and an on-board digital computer.', 'The group built the largest quantum computer ever, capable of factoring the number 15.', 'Early in his career, he pushed for the Smithsonian to purchase its first mainframe computer.', "But speed barriers, even in today's fast computers, are already an issue.", "Today's computers process data in the form of voltages representing 1s and 0s.", 'The use of hand-held computers varies widely in clinical practice.', "However, integrated graphics are the mainstay of today's office computers.", 'The worm attempts to copy itself to the Windows folder on networked computers with open shared drives.']
```

## Utilities
The endpoint contains different functionalities that help you to understand the API better. This package contains only 3 functions. For more information, read more at the official [API's main webpage](https://developer.oxforddictionaries.com/documentation#!/Search/get_search_translations_source_lang_search_target_lang_search).

- get_domains_monolingual(): Returns a list of the available domains for a given monolingual language dataset.
- get_domains_bilingual(): Returns a list of the available domains for a given bilingual language dataset.
- get_all_languages(): Returns the names of monolingual and bilingual language datasets available in the API.
