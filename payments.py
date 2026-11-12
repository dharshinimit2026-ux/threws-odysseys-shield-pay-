from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Transaction
from ..schemas import PaymentAnalysisRequest, AnalysisResult
from ..services.signal_analyzer import analyze_signals
from ..services.risk_engine import calculate_risk
from ..services.decision_engine import build_decision

router = APIRouter(prefix="/payments", tags=["Payment simulation"])

@router.post("/analyze", response_model=AnalysisResult)
def analyze_payment(payment: PaymentAnalysisRequest, db: Session = Depends(get_db)):
    observations = analyze_signals(payment)
    assessment = calculate_risk(payment)
    decision = build_decision(assessment)

    # Include observations as context, without treating them as independently verified facts.
    reasons = observations + decision["reasons"]
    record = Transaction(
        customer_id=payment.customer_id,
        receiver_id=payment.receiver_id,
        amount=payment.amount,
        remote_access_active=payment.remote_access_active,
        screen_sharing_active=payment.screen_sharing_active,
        remote_control_active=payment.remote_control_active,
        unknown_app_detected=payment.unknown_app_detected,
        unusual_device=payment.unusual_device,
        rapid_transactions=payment.rapid_transactions,
        risk_score=decision["risk_score"],
        risk_level=decision["risk_level"],
        recommendation=decision["recommendation"],
        reasons=" | ".join(reasons),
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return AnalysisResult(
        transaction_id=record.id,
        customer_id=record.customer_id,
        receiver_id=record.receiver_id,
        amount=record.amount,
        risk_score=decision["risk_score"],
        risk_level=decision["risk_level"],
        recommendation=decision["recommendation"],
        reasons=reasons,
    )
