from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

EXPECTED = {
    "branches.csv": 100,
    "employees.csv": 1500,
    "customers.csv": 25000,
    "accounts.csv": 40000,
    "transactions.csv": 1_000_000,
    "loans.csv": 15000,
    "loan_payments.csv": 150000,
    "credit_cards.csv": 20000,
    "mortgages.csv": 8000,
    "investments.csv": 30000,
    "market_data.csv": 0,
    "digital_banking.csv": 300000,
    "atm_transactions.csv": 250000,
    "fraud_alerts.csv": 10000,
    "complaints.csv": 30000,
}

print("=" * 70)
print("BANKING DATA VALIDATION")
print("=" * 70)

all_passed = True

for filename, expected_rows in EXPECTED.items():

    path = DATA_DIR / filename

    if not path.exists():
        print(f"[FAIL] {filename} - file missing")
        all_passed = False
        continue

    df = pd.read_csv(path)

    if expected_rows == 0:
        passed = len(df) > 0
    else:
        passed = len(df) == expected_rows

    status = "PASS" if passed else "FAIL"

    print(
        f"[{status}] {filename:<30} "
        f"{len(df):>10,} rows"
    )

    if not passed:
        all_passed = False

print("=" * 70)

if all_passed:
    print("ALL DATASETS PASSED VALIDATION")
else:
    print("ONE OR MORE DATASETS FAILED VALIDATION")