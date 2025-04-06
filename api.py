from fastapi import FastAPI
from pydantic import BaseModel
from recommender import SHLRecommender

app = FastAPI()
recommender = SHLRecommender()

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5

@app.post("/recommend")
def get_recommendations(req: QueryRequest):
    results = recommender.recommend(req.query, top_k=req.top_k)
    return {"recommendations": results}
