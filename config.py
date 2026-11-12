import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "SBI Smart Remote Access Fraud Protection")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sbi_fraud.db")
RISK_LOW_MAX = int(os.getenv("RISK_LOW_MAX", "29"))
RISK_MEDIUM_MAX = int(os.getenv("RISK_MEDIUM_MAX", "69"))
