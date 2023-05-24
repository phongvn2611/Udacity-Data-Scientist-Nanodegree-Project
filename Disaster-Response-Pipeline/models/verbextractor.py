""" Module with the class StartingVerbExtractor and the function tokenize """

from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import nltk
import re
nltk.download(['punkt', 'wordnet'])
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def tokenize(text):
    """Tokenize the given text

    Arguments:
        text -- Text to tokenize

    Returns:
        List of tokens
    """
    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")
    
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    
    cleaned_tokens = []
    for tok in tokens:
        cleaned_tok = lemmatizer.lemmatize(tok).lower().strip()
        cleaned_tokens.append(cleaned_tok)
    
    return cleaned_tokens

class StartingVerbExtractor(BaseEstimator, TransformerMixin):
    """new estimator class for verb extraction 

    Arguments:
        BaseEstimator -- scikit learn object
        TransformerMixin -- scikitlearn objet
    """

    def starting_verb(self, text):
        sentence_list = nltk.sent_tokenize(text)
        for sentence in sentence_list:
            pos_tags = nltk.pos_tag(tokenize(sentence))
            first_word, first_tag = pos_tags[0]
            if first_tag in ['VB', 'VBP'] or first_word == 'RT':
                return True
        return False

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(self.starting_verb)
        return pd.DataFrame(X_tagged)