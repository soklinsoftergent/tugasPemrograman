from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np

def hitung_frekuensi(documents):
    vectorizer = CountVectorizer()
    tf_matrix = vectorizer.fit_transform(documents)
    tf = tf_matrix.toarray()
    df = np.sum(tf_matrix.toarray() > 0, axis=0)
    return tf, df, vectorizer.get_feature_names_out()

def hitung_tfidf(documents):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    return tfidf_matrix, tfidf_vectorizer
