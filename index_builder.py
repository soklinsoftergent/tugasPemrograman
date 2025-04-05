from extract import extract, extractPdfTexts
from normalize import normalisasi
from frequency import hitung_tfidf
from index import simpan_index
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import os

# Step 1–4: Extract & normalize
documents = []
filenames = []
for file in os.listdir("files"):
    path = os.path.join("files", file)
    if file.endswith(".pdf"):
        raw = extractPdfTexts(path)
    else:
        raw = extract(path)
    norm = " ".join(normalisasi(raw))
    documents.append(norm)
    filenames.append(file)

# Step 5–6: Hitung TF-IDF
tfidf_matrix, tfidf_vectorizer = hitung_tfidf(documents)

# Step 7: Simpan index
simpan_index(tfidf_matrix, tfidf_vectorizer.get_feature_names_out(), filenames)

os.makedirs("dump", exist_ok=True)

# Simpan data TF-IDF
joblib.dump({
    "documents": documents,
    "filenames": filenames,
    "tfidf_matrix": tfidf_matrix,
    "tfidf_vectorizer": tfidf_vectorizer
}, "dump/tfidf_data.joblib")
