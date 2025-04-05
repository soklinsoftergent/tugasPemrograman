import joblib
from normalize import normalisasi
from sklearn.metrics.pairwise import cosine_similarity

# Load data
data = joblib.load("dump/tfidf_data.joblib")
documents = data["documents"]
filenames = data["filenames"]
tfidf_matrix = data["tfidf_matrix"]
tfidf_vectorizer = data["tfidf_vectorizer"]

# Input kueri
query = input("Masukkan kueri pencarian: ")
norm_query = " ".join(normalisasi(query))
query_vec = tfidf_vectorizer.transform([norm_query])

# Hitung kemiripan
similarity_scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
sorted_indices = similarity_scores.argsort()[::-1]

# Tampilkan hasil
print("\nDokumen paling relevan:")
for idx in sorted_indices:
    print(f"{filenames[idx]} (Skor: {similarity_scores[idx]:.4f})")
