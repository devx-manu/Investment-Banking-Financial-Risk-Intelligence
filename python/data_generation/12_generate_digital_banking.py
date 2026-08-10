from pathlib import Path
import pandas as pd
import numpy as np

SEED = 42
NUM_ACTIVITIES = 300_000

np.random.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

customers = pd.read_csv(DATA_DIR / "customers.csv")

dates = pd.to_datetime(
    np.random.randint(
        pd.Timestamp("2022-01-01").value // 10**9,
        pd.Timestamp("2025-12-31").value // 10**9,
        NUM_ACTIVITIES
    ),
    unit="s"
)

digital = pd.DataFrame({
    "digital_activity_id": np.arange(1, NUM_ACTIVITIES + 1),
    "customer_id": np.random.choice(
        customers["customer_id"],
        NUM_ACTIVITIES
    ),
    "activity_date": dates,
    "channel": np.random.choice(
        ["Mobile", "Web", "Tablet"],
        NUM_ACTIVITIES,
        p=[0.60, 0.35, 0.05]
    ),
    "device_type": np.random.choice(
        ["Android", "iOS", "Windows", "Mac"],
        NUM_ACTIVITIES
    ),
    "login_count": np.random.poisson(2, NUM_ACTIVITIES) + 1,
    "transaction_count": np.random.poisson(1.5, NUM_ACTIVITIES),
    "session_minutes": np.random.poisson(12, NUM_ACTIVITIES) + 1,
})

digital.to_csv(
    DATA_DIR / "digital_banking.csv",
    index=False
)

print(f"Digital banking records generated: {len(digital):,}")