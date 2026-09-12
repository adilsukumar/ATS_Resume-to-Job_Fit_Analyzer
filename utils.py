import logging
import os
import re

# Configuration parameters
SIMILARITY_THRESHOLD = 0.65 

# Standard English stop words to exclude from text analysis
STOP_WORDS = [
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", 
    "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", 
    "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", 
    "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", 
    "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", 
    "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", 
    "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", 
    "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", 
    "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", 
    "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", 
    "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", 
    "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", 
    "the", "their", "theirs", "them", "themselves", "then", "there", "there's", 
    "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", 
    "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", 
    "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", 
    "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", 
    "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", 
    "you've", "your", "yours", "yourself", "yourselves", "will", "can", "just", "now",
    "will", "shall", "may", "might"
]

MAX_FEATURES = 1000

# Logger configuration
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_FILE = "app_debug.log"

def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(LOG_FILE)
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter(LOG_FORMAT)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger

# Text normalization utilities
def clean_text(raw_text):
    text = raw_text.lower()
    # Remove non-alphabetical characters
    text = re.sub(r'[^a-z\s]', ' ', text)
    # Standardize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize(text):
    # Split text and filter out stop words
    words = text.split(" ")
    cleaned_words = []
    for w in words:
        if w not in STOP_WORDS and len(w) > 1: 
            cleaned_words.append(w)
    return cleaned_words
