from pathlib import Path
import pandas as pd
import numpy as np

SEED = 42

np.random.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

assets = [
    ("NIFTY 50", "Index"),
    ("SENSEX", "Index"),
    ("Banking ETF", "ETF"),
    ("Technology Fund", "Equity"),
    ("Energy Fund", "Equity"),
    ("Government Bond", "Bond"),
]

dates = pd.date_range(
    "2022-01-01",
    "2025-12-31",
    freq="B"
)

rows = []

for asset_name, asset_type in assets:

    price = np.random.uniform(500, 20_000)

    for date in dates:

        daily_return = np.random.normal(0.0003, 0.015)

        open_price = price
        close_price = price * (1 + daily_return)

        high_price = max(open_price, close_price) * (
            1 + np.random.uniform(0, 0.02)
        )

        low_price = min(open_price, close_price) * (
            1 - np.random.uniform(0, 0.02)
        )

        rows.append({
            "market_date": date,
            "asset_name": asset_name,
            "asset_type": asset_type,
            "open_price": round(open_price, 4),
            "high_price": round(high_price, 4),
            "low_price": round(low_price, 4),
            "close_price": round(close_price, 4),
            "volume": int(np.random.lognormal(15, 1)),
        })

        price = close_price

market_data = pd.DataFrame(rows)

market_data.to_csv(
    DATA_DIR / "market_data.csv",
    index=False
)

print(f"Market records generated: {len(market_data):,}")