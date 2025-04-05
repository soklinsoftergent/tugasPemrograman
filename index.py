import pandas as pd
import os

def simpan_index(tfidf_matrix, feature_names, filenames, out_file="index.csv"):
    os.makedirs("dump", exist_ok=True)
    df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names, index=filenames)
    df.to_csv(os.path.join("dump", out_file))
