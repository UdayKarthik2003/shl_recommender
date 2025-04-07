import os
import pandas as pd
from sentence_transformers import SentenceTransformer, util

class SHLRecommender:
    def __init__(self, data_file="assessments.csv"):
        # ✅ Use the local path where you cloned the model
        model_path = os.path.join(os.path.dirname(__file__), 'models', 'all-MiniLM-L6-v1')
        self.model = SentenceTransformer(model_path)

        # ✅ Load assessments CSV
        self.df = pd.read_csv(data_file, encoding='latin1', on_bad_lines='skip')
        self.df.rename(columns={"ï»¿name": "name"}, inplace=True)

        # ✅ Encode all assessment names
        self.embeddings = self.model.encode(self.df["name"].astype(str).tolist(), convert_to_tensor=True)

    def recommend(self, query, top_k=5):
        # ✅ Encode the input query
        query_embedding = self.model.encode(query, convert_to_tensor=True)

        # ✅ Compute cosine similarity
        scores = util.cos_sim(query_embedding, self.embeddings)[0]
        top_results = scores.topk(k=top_k)

        results = []
        for score, idx in zip(top_results.values, top_results.indices):
            row = self.df.iloc[int(idx)]
            results.append({
                "name": row.get("name", ""),
                "url": row.get("url", ""),
                "score": float(score),
                "duration": row.get("duration", "N/A"),
                "remote": row.get("remote", "Yes"),
                "adaptive": row.get("adaptive", "Yes"),
                "type": row.get("type", "N/A")
            })
        return results
