from pathlib import Path
import pandas as pd
import numpy as np

SEED = 42
NUM_COMPLAINTS = 30_000

np.random.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

customers = pd.read_csv(DATA_DIR / "customers.csv")
branches = pd.read_csv(DATA_DIR / "branches.csv")

complaint_types = [
    "Transaction Issue",
    "Loan Service",
    "Credit Card",
    "ATM Issue",
    "Digital Banking",
    "Fraud Concern",
    "Account Service",
    "Investment Service",
]

complaints = pd.DataFrame({
    "complaint_id": np.arange(1, NUM_COMPLAINTS + 1),
    "customer_id": np.random.choice(
        customers["customer_id"],
        NUM_COMPLAINTS
    ),
    "branch_id": np.random.choice(
        branches["branch_id"],
        NUM_COMPLAINTS
    ),
    "complaint_date": pd.to_datetime(
        np.random.randint(
            pd.Timestamp("2022-01-01").value // 10**9,
            pd.Timestamp("2025-12-31").value // 10**9,
            NUM_COMPLAINTS
        ),
        unit="s"
    ),
    "complaint_type": np.random.choice(
        complaint_types,
        NUM_COMPLAINTS
    ),
    "channel": np.random.choice(
        ["Branch", "Phone", "Web", "Mobile"],
        NUM_COMPLAINTS
    ),
    "priority": np.random.choice(
        ["Low", "Medium", "High", "Critical"],
        NUM_COMPLAINTS,
        p=[0.35, 0.45, 0.17, 0.03]
    ),
})

complaints["resolution_status"] = np.random.choice(
    ["Open", "In Progress", "Resolved"],
    NUM_COMPLAINTS,
    p=[0.08, 0.17, 0.75]
)

complaints["resolution_date"] = pd.NaT

resolved = complaints["resolution_status"] == "Resolved"

complaints.loc[resolved, "resolution_date"] = (
    complaints.loc[resolved, "complaint_date"]
    + pd.to_timedelta(
        np.random.randint(
            1,
            31,
            resolved.sum()
        ),
        unit="D"
    )
)

complaints.to_csv(
    DATA_DIR / "complaints.csv",
    index=False
)

print(f"Complaints generated: {len(complaints):,}")