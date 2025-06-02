from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.recommender import StockRecommender
import json

app = FastAPI(title="Stock Recommendation API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecommendationRequest(BaseModel):
    budget: float
    risk_level: str
    sectors: list[str]

@app.post("/recommend")
async def generate_recommendations(request: RecommendationRequest):
    try:
        recommender = StockRecommender(
            budget=request.budget,
            risk_profile=request.risk_level,
            sectors=request.sectors
        )
        
        return {
            "top_stocks": recommender.top_stocks,
            "allocation_chart": recommender.chart_json,
            "metrics": recommender.metrics_df,
            "report_csv": recommender.csv_report
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Recommendation failed: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
