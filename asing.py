# Load Indonesian root words
with open("resource/NLP_bahasa_resources-master/combined_root_words.txt", "r", encoding="utf-8") as f:
    indo_root_words = set(f.read().splitlines())

def is_indonesian_word(word):
    """Check if a word exists in the Indonesian root words list."""
    return word in indo_root_words
