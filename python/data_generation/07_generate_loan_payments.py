from pathlib import Path
import pandas as pd
import numpy as np

SEED = 42
PAYMENTS_PER_LOAN = 10

np.random.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

loans = pd.read_csv(DATA_DIR / "loans.csv")

rows = []
payment_id = 1

for _, loan in loans.iterrows():

    for month in range(PAYMENTS_PER_LOAN):

        due = loan["loan_amount"] / max(loan["tenure_months"], 1)

        late_probability = 0.05 + (
            0.20 if loan["default_flag"] else 0
        )

        days_late = (
            int(np.random.exponential(15))
            if np.random.random() < late_probability
            else 0
        )

        if days_late > 60:
            paid = 0
            status = "Missed"
        elif days_late > 0:
            paid = due * np.random.uniform(0.5, 1.0)
            status = "Late"
        else:
            paid = due * np.random.uniform(0.95, 1.05)
            status = "On Time"

        rows.append({
            "payment_id": payment_id,
            "loan_id": loan["loan_id"],
            "payment_date": pd.Timestamp("2022-01-01") + pd.DateOffset(
                months=month
            ),
            "due_amount": round(due, 2),
            "paid_amount": round(max(paid, 0), 2),
            "days_late": days_late,
            "payment_status": status,
        })

        payment_id += 1

payments = pd.DataFrame(rows)

payments.to_csv(
    DATA_DIR / "loan_payments.csv",
    index=False
)

print(f"Loan payments generated: {len(payments):,}")