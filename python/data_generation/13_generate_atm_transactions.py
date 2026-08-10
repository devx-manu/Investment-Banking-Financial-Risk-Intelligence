from pathlib import Path
import pandas as pd
import numpy as np

SEED = 42
NUM_ATM = 250_000

np.random.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

accounts = pd.read_csv(DATA_DIR / "accounts.csv")
customers = pd.read_csv(DATA_DIR / "customers.csv")

account_ids = np.random.choice(
    accounts["account_id"],
    NUM_ATM
)

account_customer = accounts.set_index("account_id")["customer_id"]

atm = pd.DataFrame({
    "atm_transaction_id": np.arange(1, NUM_ATM + 1),
    "customer_id": account_customer.loc[account_ids].values,
    "account_id": account_ids,
    "transaction_date": pd.to_datetime(
        np.random.randint(
            pd.Timestamp("2022-01-01").value // 10**9,
            pd.Timestamp("2025-12-31").value // 10**9,
            NUM_ATM
        ),
        unit="s"
    ),
    "atm_location": np.random.choice(
        customers["city"].unique(),
        NUM_ATM
    ),
    "transaction_type": np.random.choice(
        ["Withdrawal", "Deposit", "Balance Inquiry"],
        NUM_ATM,
        p=[0.70, 0.15, 0.15]
    ),
    "amount": np.round(
        np.random.lognormal(7.0, 1.0, NUM_ATM),
        2
    ),
    "status": np.random.choice(
        ["Completed", "Failed", "Reversed"],
        NUM_ATM,
        p=[0.97, 0.02, 0.01]
    ),
})

atm.to_csv(
    DATA_DIR / "atm_transactions.csv",
    index=False
)

print(f"ATM transactions generated: {len(atm):,}")