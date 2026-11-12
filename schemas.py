from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class PaymentAnalysisRequest(BaseModel):
    customer_id: str = Field(min_length=1, max_length=80)
    receiver_id: str = Field(min_length=1, max_length=80)
    amount: float = Field(gt=0, le=10_000_000)
    # These are simulated signals supplied to this prototype, not phone-level detection.
    remote_access_active: bool = False
    screen_sharing_active: bool = False
    remote_control_active: bool = False
    unknown_app_detected: bool = False
    unusual_device: bool = False
    rapid_transactions: bool = False

class AnalysisResult(BaseModel):
    transaction_id: int
    customer_id: str
    receiver_id: str
    amount: float
    risk_score: int
    risk_level: str
    recommendation: str
    reasons: list[str]
    prototype_notice: str = "Simulated security signals only; not connected to SBI or a live payment rail."

class TransactionHistoryItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    customer_id: str
    receiver_id: str
    amount: float
    risk_score: int
    risk_level: str
    recommendation: str
    reasons: str
    created_at: datetime
