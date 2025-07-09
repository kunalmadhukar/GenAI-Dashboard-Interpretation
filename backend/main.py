from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI(
    title="GenAI Dashboard Backend",
    description="API for GenAI-powered insights and dashboard interpretations",
    version="0.1.0",
)

# Allow CORS from any origin for development convenience
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ExplanationRequest(BaseModel):
    """Request body for the /explanation endpoint."""

    rule_id: str
    timestamp: str


class ThresholdRecommendationRequest(BaseModel):
    """Request body for the /recommend-threshold endpoint."""

    metric_name: str
    window: str


class RuleHitSummaryRequest(BaseModel):
    """Request body for the /rule-hit-summary endpoint."""

    start_date: str
    end_date: str


@app.get("/")
def root():
    """Basic health check used by the frontend and tests."""

    return {"message": "GenAI Dashboard API is up"}


@app.post("/explanation")
def generate_explanation(req: ExplanationRequest):
    """Return a stub explanation for a rule at a given timestamp."""

    return {"message": f"Stub explanation for rule {req.rule_id}"}


@app.post("/recommend-threshold")
def recommend_threshold(req: ThresholdRecommendationRequest):
    """Return a dummy threshold for the supplied metric/window."""

    # Threshold calculation would happen here. For now return a constant.
    return {"recommended_threshold": 85}


@app.post("/rule-hit-summary")
def rule_hit_summary(req: RuleHitSummaryRequest):
    """Return a dummy summary of rule hits for the supplied date range."""

    return {"summary": f"Hits from {req.start_date} to {req.end_date}"}
