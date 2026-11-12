from datetime import datetime, timezone
from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    customer_id: Mapped[str] = mapped_column(String(80), index=True)
    receiver_id: Mapped[str] = mapped_column(String(80))
    amount: Mapped[float] = mapped_column(Float)
    remote_access_active: Mapped[bool] = mapped_column(default=False)
    screen_sharing_active: Mapped[bool] = mapped_column(default=False)
    remote_control_active: Mapped[bool] = mapped_column(default=False)
    unknown_app_detected: Mapped[bool] = mapped_column(default=False)
    unusual_device: Mapped[bool] = mapped_column(default=False)
    rapid_transactions: Mapped[bool] = mapped_column(default=False)
    risk_score: Mapped[int] = mapped_column(Integer)
    risk_level: Mapped[str] = mapped_column(String(20))
    recommendation: Mapped[str] = mapped_column(String(40))
    reasons: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
