from langdetect import detect, DetectorFactory
# Ensure deterministic results from langdetect
DetectorFactory.seed = 0

def detect_language(word):
    """Detect language of a word. Return None if language cannot be detected."""
    try:
        return detect(word)
    except:
        return None  # Likely a conjoined word