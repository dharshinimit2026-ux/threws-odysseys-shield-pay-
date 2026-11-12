from fastapi import APIRouter
from ..schemas import PaymentAnalysisRequest
from ..services.risk_engine import calculate_risk
from ..services.decision_engine import build_decision

router = APIRouter(prefix="/risk", tags=["Risk engine"])

@router.post("/preview")
def preview_risk(payment: PaymentAnalysisRequest):
    """Calculate a risk preview without saving a transaction to the database."""
    assessment = calculate_risk(payment)
    return build_decision(assessment)
