import numpy as np
import math
from utils import clean_text, tokenize, get_logger, MAX_FEATURES

log = get_logger("Features")

class TFIDFExtractor:
    def __init__(self):
        self.vocab = {}
        self.idf = {}
        self.doc_count = 0
        
    def fit(self, documents):
        """
        Generates the vocabulary and calculates Inverse Document Frequency (IDF).
        """
        self.doc_count = len(documents)
        log.info(f"Fitting TF-IDF on {self.doc_count} documents.")
        
        # Track document frequency for each word
        df = {}
        
        for doc in documents:
            cleaned = clean_text(doc)
            words = tokenize(cleaned)
            # Identify unique words in the current document
            unique_words = set(words)
            
            for w in unique_words:
                if w in df:
                    df[w] += 1
                else:
                    df[w] = 1
                    
        # Sort and limit vocabulary to prevent memory overload
        sorted_df = sorted(df.items(), key=lambda x: x[1], reverse=True)
        sorted_df = sorted_df[:MAX_FEATURES]
        
        # Construct the vocabulary index and compute IDF scores
        for idx, (word, freq) in enumerate(sorted_df):
            self.vocab[word] = idx
            # Standard IDF calculation: log(N / (df + 1))
            self.idf[word] = math.log(self.doc_count / (freq + 1)) + 1
            
        log.debug(f"Final vocabulary size: {len(self.vocab)}")
        
    def transform(self, document):
        """
        Converts the document text into a numerical TF-IDF vector.
        """
        if not self.vocab:
            log.error("Vocabulary is empty. Fit method must be called first.")
            return np.zeros(1)
            
        vec = np.zeros(len(self.vocab))
        
        cleaned = clean_text(document)
        words = tokenize(cleaned)
        
        # Calculate term frequency (TF)
        tf = {}
        total_words = len(words)
        if total_words == 0:
            return vec
            
        for w in words:
            if w in tf:
                tf[w] += 1
            else:
                tf[w] = 1
                
        # Compute final TF-IDF values and populate the vector
        for word, count in tf.items():
            if word in self.vocab:
                idx = self.vocab[word]
                term_freq = count / total_words
                vec[idx] = term_freq * self.idf[word]
                
        return vec
        
    def get_feature_names(self):
        """Returns the ordered list of words in the vocabulary."""
        # Reverse the vocabulary mapping to retrieve word labels
        inv_vocab = {v: k for k, v in self.vocab.items()}
        return [inv_vocab[i] for i in range(len(self.vocab))]
