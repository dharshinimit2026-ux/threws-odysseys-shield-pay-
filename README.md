# Backend – SBI Smart Remote Access Fraud Protection Layer

Educational bank-side prototype. It is **not** connected to SBI, NPCI, UPI, a phone operating system, or any live payment system. It does not block real transactions.

## Requirements
- Python 3.10+
- VS Code (or another editor)

## Windows setup
Open a terminal in the `backend` folder:

```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

If `py` is unavailable, use `python` instead.

## macOS/Linux setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test the API
- Home: http://127.0.0.1:8000/
- Health: http://127.0.0.1:8000/health
- Interactive API docs: http://127.0.0.1:8000/docs
- Payment analysis: `POST /payments/analyze`
- Risk preview (not saved): `POST /risk/preview`
- History: `GET /history/`

Example request:

```json
{
  "customer_id": "DEMO-C001",
  "receiver_id": "DEMO-R001",
  "amount": 5000,
  "remote_access_active": true,
  "screen_sharing_active": true,
  "remote_control_active": false,
  "unknown_app_detected": true,
  "unusual_device": false,
  "rapid_transactions": false
}
```

## How the score works
The rule-based demo adds points for the supplied simulated flags:
- Remote access: 25
- Screen sharing: 20
- Remote control: 30
- Unknown app: 10
- Unusual device: 10
- Rapid transactions: 15
- Amount >= 100,000: 5

Score is capped at 100:
- 0–29: LOW
- 30–69: MEDIUM
- 70–100: HIGH

These weights are illustrative only. They are not validated fraud indicators or bank policy. Signals are supplied by the API caller for simulation; a normal browser cannot reliably inspect device-wide remote-control or screen-sharing state. A production implementation would require authorised, privacy-reviewed, platform-specific signal sources, bank security review, model validation, audit controls, and regulatory/legal approval.

## Database
SQLite database `sbi_fraud.db` is created automatically in the backend working directory. Do not commit real customer data or secrets.

## GitHub
Commit source code and documentation only. Keep `.env`, virtual environments, database files, API keys, and customer data out of the repository.
