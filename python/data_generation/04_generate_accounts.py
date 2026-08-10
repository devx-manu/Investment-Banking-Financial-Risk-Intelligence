from pathlib import Path
import pandas as pd
import numpy as np

SEED = 42
NUM_ACCOUNTS = 40_000

np.random.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

customers = pd.read_csv(DATA_DIR / "customers.csv")
branches = pd.read_csv(DATA_DIR / "branches.csv")

account_types = ["Savings", "Current", "Salary", "Premium", "Business"]

rows = []

for account_id in range(1, NUM_ACCOUNTS + 1):
    customer_id = np.random.choice(customers["customer_id"])

    rows.append({
        "account_id": account_id,
        "customer_id": customer_id,
        "branch_id": np.random.choice(branches["branch_id"]),
        "account_type": np.random.choice(
            account_types,
            p=[0.55, 0.15, 0.15, 0.10, 0.05]
        ),
        "open_date": np.random.choice(customers["customer_since"]),
        "balance": round(np.random.lognormal(9.5, 1.2), 2),
        "currency": "INR",
        "account_status": np.random.choice(
            ["Active", "Dormant", "Closed"],
            p=[0.92, 0.06, 0.02]
        ),
    })

accounts = pd.DataFrame(rows)

accounts.to_csv(DATA_DIR / "accounts.csv", index=False)

print(f"Accounts generated: {len(accounts):,}")