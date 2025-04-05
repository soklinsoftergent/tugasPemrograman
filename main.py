from extract import extract, extractPdfTexts
from normalize import normalisasi
from frequency import hitung_tfidf
from index import simpan_index
from sklearn.metrics.pairwise import cosine_similarity
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

# Step 8: Input query dan hitung kemiripan
query = input("Masukkan kueri pencarian: ")
norm_query = " ".join(normalisasi(query))
query_vec = tfidf_vectorizer.transform([norm_query])

# Step 9: Hitung dan sortir kemiripan
similarity_scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
sorted_indices = similarity_scores.argsort()[::-1]

# Output
print("\nDokumen paling relevan:")
for idx in sorted_indices:
    print(f"{filenames[idx]} (Skor: {similarity_scores[idx]:.4f})")
