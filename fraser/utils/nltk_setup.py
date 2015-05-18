'''
nltk_setup.py

Designed to be run once at installation time. This util setups up the env or
venv for nltk -> downloads the appropriate extra data, sets up the paths.

Note that the paths will still need to be set in the model's functions for
runtime. 
'''

import os
import nltk
import urllib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NLTK_DATA = os.path.join(BASE_DIR, 'nltk_data') 
STOPWORDS = os.path.join(NLTK_DATA, 'corpora/stopwords')

if not os.path.exists(NLTK_DATA):
    os.makedirs(NLTK_DATA)

nltk.download('stopwords', download_dir=NLTK_DATA)

nltk.download('punkt', download_dir=NLTK_DATA)

if not os.path.exists(STOPWORDS):
    os.makedirs(STOPWORDS)

JUSTEXT = os.path.join(STOPWORDS, 'justext_english')

justext_stopwords = urllib.URLopener()
justext_stopwords.retrieve("https://raw.githubusercontent.com/endredy/jusText/master/stoplists/English.txt", JUSTEXT)


