from pathlib import Path
import pandas as pd
import numpy as np

SEED = 42
NUM_MORTGAGES = 8_000

np.random.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

customers = pd.read_csv(DATA_DIR / "customers.csv")
branches = pd.read_csv(DATA_DIR / "branches.csv")

rows = []

for mortgage_id in range(1, NUM_MORTGAGES + 1):

    property_value = np.random.lognormal(15, 0.55)
    property_value = np.clip(
        property_value,
        1_000_000,
        100_000_000
    )

    loan_amount = property_value * np.random.uniform(
        0.4,
        0.8
    )

    rows.append({
        "mortgage_id": mortgage_id,
        "customer_id": np.random.choice(customers["customer_id"]),
        "branch_id": np.random.choice(branches["branch_id"]),
        "property_value": round(property_value, 2),
        "loan_amount": round(loan_amount, 2),
        "interest_rate": round(
            np.random.uniform(6.5, 11.5),
            3
        ),
        "term_years": int(
            np.random.choice([10, 15, 20, 25, 30])
        ),
        "start_date": pd.Timestamp(
            np.random.choice(
                pd.date_range("2022-01-01", "2025-01-01")
            )
        ),
        "outstanding_balance": round(
            loan_amount * np.random.uniform(0.3, 0.95),
            2
        ),
        "mortgage_status": np.random.choice(
            ["Active", "Closed", "Defaulted"],
            p=[0.92, 0.06, 0.02]
        ),
    })

mortgages = pd.DataFrame(rows)

mortgages.to_csv(
    DATA_DIR / "mortgages.csv",
    index=False
)

print(f"Mortgages generated: {len(mortgages):,}")