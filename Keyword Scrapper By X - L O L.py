import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
import spacy
from yake import KeywordExtractor


nlp = spacy.load("en_core_web_sm")

def scrape_keywords(url):
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')

    text = soup.get_text()

    tokens = word_tokenize(text)

    tokens = [token for token in tokens if token.isalpha() and token not in nltk.corpus.stopwords.words('english')]

    text = ' '.join(tokens)

    language = "en"
    max_ngram_size = 3
    numOfKeywords = int(input(f'Number of keywords: '))
    custom_kw_extractor = KeywordExtractor(lan=language, n=max_ngram_size, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    return keywords


url = input(f'Targetted Site: ')
keywords = scrape_keywords(url)

print(url+" Keywords: ")
for keyword, score in keywords:
    print(f"{keyword}")

import time
print(f'\n\n\nProgram Closing in 15 Seconds...')
time.sleep(15)

