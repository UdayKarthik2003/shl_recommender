import pandas as pd
from sentence_transformers import SentenceTransformer, util

class SHLRecommender:
    def __init__(self, data_file="assessments.csv"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.df = pd.read_csv(data_file, encoding='latin1', on_bad_lines='skip')
        self.df.rename(columns={"ï»¿name": "name"}, inplace=True)
        print("Columns:", self.df.columns.tolist())

        self.embeddings = self.model.encode(self.df["name"].tolist(), convert_to_tensor=True)

    


    def recommend(self, query, top_k=5):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_embedding, self.embeddings)[0]
        top_results = scores.topk(k=top_k)

        results = []
        for score, idx in zip(top_results.values, top_results.indices):
            row = self.df.iloc[int(idx)]
            results.append({
                "name": row["name"],
                "url": row["url"],
                "score": float(score),
                "duration": row.get("duration", "N/A"),
                "remote": row.get("remote", "Yes"),
                "adaptive": row.get("adaptive", "Yes"),
                "type": row.get("type", "N/A")
            })
        return results
    

