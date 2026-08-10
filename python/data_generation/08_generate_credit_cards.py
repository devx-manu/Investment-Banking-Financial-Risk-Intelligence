from pathlib import Path
import pandas as pd
import numpy as np

SEED = 42
NUM_CARDS = 20_000

np.random.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

customers = pd.read_csv(DATA_DIR / "customers.csv")

rows = []

for card_id in range(1, NUM_CARDS + 1):

    customer_id = np.random.choice(customers["customer_id"])

    credit_limit = np.random.choice([
        50_000,
        100_000,
        200_000,
        500_000,
        1_000_000
    ])

    utilization = np.random.beta(2, 5)

    rows.append({
        "credit_card_id": card_id,
        "customer_id": customer_id,
        "issue_date": pd.Timestamp(
            np.random.choice(
                pd.date_range("2022-01-01", "2025-01-01")
            )
        ),
        "credit_limit": credit_limit,
        "current_balance": round(
            credit_limit * utilization,
            2
        ),
        "interest_rate": round(
            np.random.uniform(18, 42),
            3
        ),
        "card_status": np.random.choice(
            ["Active", "Blocked", "Closed"],
            p=[0.92, 0.04, 0.04]
        ),
    })

cards = pd.DataFrame(rows)

cards.to_csv(
    DATA_DIR / "credit_cards.csv",
    index=False
)

print(f"Credit cards generated: {len(cards):,}")