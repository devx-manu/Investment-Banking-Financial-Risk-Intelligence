from pathlib import Path
import pandas as pd
import numpy as np

SEED = 42
NUM_INVESTMENTS = 30_000

np.random.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

customers = pd.read_csv(DATA_DIR / "customers.csv")

investment_types = [
    "Equity",
    "Bond",
    "Mutual Fund",
    "ETF",
    "Fixed Deposit",
]

risk_levels = ["Low", "Medium", "High"]

asset_names = [
    "NIFTY 50 ETF",
    "SENSEX ETF",
    "Government Bond",
    "Corporate Bond Fund",
    "Large Cap Fund",
    "Mid Cap Fund",
    "Banking ETF",
    "Technology Fund",
    "Energy Fund",
    "Healthcare Fund",
]

rows = []

for investment_id in range(1, NUM_INVESTMENTS + 1):

    investment_type = np.random.choice(investment_types)

    if investment_type in ["Bond", "Fixed Deposit"]:
        risk = "Low"
    elif investment_type in ["Mutual Fund", "ETF"]:
        risk = np.random.choice(["Low", "Medium", "High"])
    else:
        risk = "High"

    quantity = np.random.uniform(1, 1000)
    purchase_price = np.random.uniform(50, 5000)

    purchase_value = quantity * purchase_price

    current_value = purchase_value * np.random.uniform(
        0.75,
        1.35
    )

    rows.append({
        "investment_id": investment_id,
        "customer_id": np.random.choice(customers["customer_id"]),
        "investment_type": investment_type,
        "asset_name": np.random.choice(asset_names),
        "investment_date": pd.Timestamp(
            np.random.choice(
                pd.date_range("2022-01-01", "2025-12-01")
            )
        ),
        "quantity": round(quantity, 6),
        "purchase_price": round(purchase_price, 2),
        "current_value": round(current_value, 2),
        "risk_level": risk,
    })

investments = pd.DataFrame(rows)

investments.to_csv(
    DATA_DIR / "investments.csv",
    index=False
)

print(f"Investments generated: {len(investments):,}")