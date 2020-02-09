import nltk
from nltk.corpus import stopwords, wordnet
from pymystem3 import Mystem
from string import punctuation


nltk.download("stopwords")

mystem = Mystem()
russian_stopwords = stopwords.words("russian")


def preprocess_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords\
              and token != " " \
              and token.strip() not in punctuation]
    return tokens

