#import packages
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import word_tokenize
import re
import wordninja
from deteksi_bahasa import detect_language
from pisahKata import split_conjoined

# Load Indonesian word dictionary
INDO_DICT_PATH = "resource/NLP_bahasa_resources-master/combined_root_words.txt"
with open(INDO_DICT_PATH, "r", encoding="utf-8") as f:
    indo_words = set(f.read().splitlines())

# Create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def normalisasi(text):
    # Remove URLs
    text = re.sub(r'http[s]?://\S+', '', text)

    # Lowercase text
    text = text.lower()

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove punctuations
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Tokenize
    tokens = word_tokenize(text)

    # Process tokens
        # Process tokens
    final_tokens = []
    for token in tokens:
        lang = detect_language(token)

        if lang == "id" or token in indo_words:  
            final_tokens.append(stemmer.stem(token))  # Stem immediately if Indonesian
        elif lang != "id":  
            final_tokens.append(token)  # Keep foreign words
        else:  
            split_words = split_conjoined(token)  
            final_tokens.extend(stemmer.stem(w) for w in split_words if w in indo_words)

    return " ".join(final_tokens)
