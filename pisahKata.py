# Load Indonesian word dictionary
INDO_DICT_PATH = "resource/NLP_bahasa_resources-master/combined_root_words.txt"
with open(INDO_DICT_PATH, "r", encoding="utf-8") as f:
    indo_words = set(f.read().splitlines())

def split_conjoined(word):
    """Split conjoined words by finding the longest prefix in the dictionary."""
    for i in range(len(word), 0, -1):
        prefix = word[:i]
        suffix = word[i:]

        if prefix in indo_words and suffix in indo_words:
            return [prefix, suffix]
        if prefix in indo_words:
            return [prefix] + split_conjoined(suffix)
    
    return [word]  # Return as is if no split found