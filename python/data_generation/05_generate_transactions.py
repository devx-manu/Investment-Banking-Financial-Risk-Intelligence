from pathlib import Path
import pandas as pd
import numpy as np

SEED = 42
NUM_TRANSACTIONS = 1_000_000

np.random.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

accounts = pd.read_csv(DATA_DIR / "accounts.csv")
customers = pd.read_csv(DATA_DIR / "customers.csv")

transaction_types = ["Debit", "Credit", "Transfer"]

categories = [
    "Food",
    "Shopping",
    "Utilities",
    "Salary",
    "Rent",
    "Investment",
    "Loan Payment",
    "Transfer",
    "Healthcare",
    "Travel",
    "ATM",
]

channels = ["ATM", "Branch", "Mobile", "Online", "POS"]

customer_lookup = customers.set_index("customer_id")

account_ids = np.random.choice(
    accounts["account_id"].values,
    size=NUM_TRANSACTIONS
)

account_customer = accounts.set_index("account_id")["customer_id"]

customer_ids = account_customer.loc[account_ids].values

dates = pd.to_datetime(
    np.random.randint(
        pd.Timestamp("2022-01-01").value // 10**9,
        pd.Timestamp("2025-12-31").value // 10**9,
        NUM_TRANSACTIONS
    ),
    unit="s"
)

amounts = np.random.lognormal(mean=7.0, sigma=1.3, size=NUM_TRANSACTIONS)

transactions = pd.DataFrame({
    "transaction_id": np.arange(1, NUM_TRANSACTIONS + 1),
    "account_id": account_ids,
    "customer_id": customer_ids,
    "transaction_date": dates,
    "transaction_type": np.random.choice(
        transaction_types,
        NUM_TRANSACTIONS,
        p=[0.50, 0.35, 0.15]
    ),
    "transaction_category": np.random.choice(
        categories,
        NUM_TRANSACTIONS
    ),
    "amount": np.round(amounts, 2),
    "merchant": np.random.choice(
        ["Amazon", "Flipkart", "Swiggy", "Uber", "DMart", "Hospital", "Utility Provider", "Local Merchant"],
        NUM_TRANSACTIONS
    ),
    "channel": np.random.choice(
        channels,
        NUM_TRANSACTIONS,
        p=[0.15, 0.10, 0.35, 0.25, 0.15]
    ),
    "location": np.random.choice(
        customers["city"].unique(),
        NUM_TRANSACTIONS
    ),
    "status": np.random.choice(
        ["Completed", "Failed", "Reversed"],
        NUM_TRANSACTIONS,
        p=[0.96, 0.03, 0.01]
    ),
})

transactions.to_csv(
    DATA_DIR / "transactions.csv",
    index=False
)

print(f"Transactions generated: {len(transactions):,}")