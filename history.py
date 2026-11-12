from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Transaction
from ..schemas import TransactionHistoryItem

router = APIRouter(prefix="/history", tags=["Transaction history"])

@router.get("/", response_model=list[TransactionHistoryItem])
def list_history(limit: int = 50, db: Session = Depends(get_db)):
    if limit < 1 or limit > 200:
        raise HTTPException(status_code=400, detail="limit must be between 1 and 200")
    return db.query(Transaction).order_by(Transaction.id.desc()).limit(limit).all()

@router.get("/{transaction_id}", response_model=TransactionHistoryItem)
def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    record = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if record is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return record
