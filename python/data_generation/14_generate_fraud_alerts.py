from pathlib import Path
import pandas as pd
import numpy as np

SEED = 42
NUM_ALERTS = 10_000

np.random.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

transactions = pd.read_csv(DATA_DIR / "transactions.csv")

selected = transactions.sample(
    NUM_ALERTS,
    random_state=SEED
).copy()

fraud_types = [
    "Unusual Transaction",
    "High Value Transaction",
    "Geographic Anomaly",
    "Velocity Anomaly",
    "Possible Account Takeover",
    "Suspicious Merchant",
]

fraud = pd.DataFrame({
    "alert_id": np.arange(1, NUM_ALERTS + 1),
    "transaction_id": selected["transaction_id"].values,
    "customer_id": selected["customer_id"].values,
    "alert_date": pd.to_datetime(
        selected["transaction_date"]
    ),
    "fraud_type": np.random.choice(
        fraud_types,
        NUM_ALERTS
    ),
    "risk_level": np.random.choice(
        ["Low", "Medium", "High", "Critical"],
        NUM_ALERTS,
        p=[0.25, 0.40, 0.30, 0.05]
    ),
    "fraud_status": np.random.choice(
        [
            "Open",
            "Investigating",
            "Confirmed",
            "False Positive",
            "Closed",
        ],
        NUM_ALERTS,
        p=[0.10, 0.15, 0.25, 0.35, 0.15]
    ),
    "fraud_amount": np.round(
        selected["amount"].values * np.random.uniform(
            0.5,
            1.0,
            NUM_ALERTS
        ),
        2
    ),
})

fraud.to_csv(
    DATA_DIR / "fraud_alerts.csv",
    index=False
)

print(f"Fraud alerts generated: {len(fraud):,}")