from pathlib import Path
import pandas as pd


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"


# ---------------------------------------------------------
# Expected files
# ---------------------------------------------------------

EXPECTED_FILES = [
    "branches.csv",
    "employees.csv",
    "customers.csv",
    "accounts.csv",
    "transactions.csv",
    "loans.csv",
    "loan_payments.csv",
    "credit_cards.csv",
    "mortgages.csv",
    "investments.csv",
    "market_data.csv",
    "digital_banking.csv",
    "atm_transactions.csv",
    "fraud_alerts.csv",
    "complaints.csv",
]


# ---------------------------------------------------------
# Helper
# ---------------------------------------------------------

def check(condition, message):
    if condition:
        print(f"[PASS] {message}")
        return True

    print(f"[FAIL] {message}")
    return False


# ---------------------------------------------------------
# Load datasets
# ---------------------------------------------------------

print("=" * 70)
print("RAW BANKING DATA QUALITY VALIDATION")
print("=" * 70)

data = {}

for filename in EXPECTED_FILES:

    path = DATA_DIR / filename

    if not path.exists():
        print(f"[FAIL] Missing file: {filename}")
        continue

    data[filename] = pd.read_csv(path)

    print(
        f"[LOAD] {filename:<30} "
        f"{len(data[filename]):>10,} rows"
    )


# ---------------------------------------------------------
# Primary key checks
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("PRIMARY KEY VALIDATION")
print("=" * 70)

primary_keys = {
    "branches.csv": ["branch_id"],
    "employees.csv": ["employee_id"],
    "customers.csv": ["customer_id"],
    "accounts.csv": ["account_id"],
    "transactions.csv": ["transaction_id"],
    "loans.csv": ["loan_id"],
    "loan_payments.csv": ["payment_id"],
    "credit_cards.csv": ["credit_card_id"],
    "mortgages.csv": ["mortgage_id"],
    "investments.csv": ["investment_id"],
    "market_data.csv": ["market_date", "asset_name"],
    "digital_banking.csv": ["digital_activity_id"],
    "atm_transactions.csv": ["atm_transaction_id"],
    "fraud_alerts.csv": ["alert_id"],
    "complaints.csv": ["complaint_id"],
}

for filename, keys in primary_keys.items():

    if filename not in data:
        continue

    df = data[filename]

    nulls = df[keys].isnull().any().any()
    duplicates = df.duplicated(subset=keys).any()

    check(
        not nulls,
        f"{filename}: primary key has no NULL values"
    )

    check(
        not duplicates,
        f"{filename}: primary key has no duplicates"
    )


# ---------------------------------------------------------
# Foreign key checks
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("FOREIGN KEY VALIDATION")
print("=" * 70)


def validate_fk(
    child_file,
    child_column,
    parent_file,
    parent_column
):

    child = data[child_file]
    parent = data[parent_file]

    child_values = set(child[child_column].dropna())
    parent_values = set(parent[parent_column].dropna())

    invalid = child_values - parent_values

    check(
        len(invalid) == 0,
        f"{child_file}.{child_column} → "
        f"{parent_file}.{parent_column}"
    )

    if invalid:
        print(
            f"       Invalid values: "
            f"{list(invalid)[:10]}"
        )


validate_fk(
    "employees.csv",
    "branch_id",
    "branches.csv",
    "branch_id"
)

validate_fk(
    "accounts.csv",
    "customer_id",
    "customers.csv",
    "customer_id"
)

validate_fk(
    "accounts.csv",
    "branch_id",
    "branches.csv",
    "branch_id"
)

validate_fk(
    "transactions.csv",
    "account_id",
    "accounts.csv",
    "account_id"
)

validate_fk(
    "transactions.csv",
    "customer_id",
    "customers.csv",
    "customer_id"
)

validate_fk(
    "loans.csv",
    "customer_id",
    "customers.csv",
    "customer_id"
)

validate_fk(
    "loans.csv",
    "branch_id",
    "branches.csv",
    "branch_id"
)

validate_fk(
    "loan_payments.csv",
    "loan_id",
    "loans.csv",
    "loan_id"
)

validate_fk(
    "credit_cards.csv",
    "customer_id",
    "customers.csv",
    "customer_id"
)

validate_fk(
    "mortgages.csv",
    "customer_id",
    "customers.csv",
    "customer_id"
)

validate_fk(
    "mortgages.csv",
    "branch_id",
    "branches.csv",
    "branch_id"
)

validate_fk(
    "investments.csv",
    "customer_id",
    "customers.csv",
    "customer_id"
)

validate_fk(
    "digital_banking.csv",
    "customer_id",
    "customers.csv",
    "customer_id"
)

validate_fk(
    "atm_transactions.csv",
    "customer_id",
    "customers.csv",
    "customer_id"
)

validate_fk(
    "atm_transactions.csv",
    "account_id",
    "accounts.csv",
    "account_id"
)

validate_fk(
    "fraud_alerts.csv",
    "transaction_id",
    "transactions.csv",
    "transaction_id"
)

validate_fk(
    "fraud_alerts.csv",
    "customer_id",
    "customers.csv",
    "customer_id"
)

validate_fk(
    "complaints.csv",
    "customer_id",
    "customers.csv",
    "customer_id"
)

validate_fk(
    "complaints.csv",
    "branch_id",
    "branches.csv",
    "branch_id"
)


# ---------------------------------------------------------
# Business rule validation
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("BUSINESS RULE VALIDATION")
print("=" * 70)

customers = data["customers.csv"]
accounts = data["accounts.csv"]
loans = data["loans.csv"]
payments = data["loan_payments.csv"]
cards = data["credit_cards.csv"]
mortgages = data["mortgages.csv"]
investments = data["investments.csv"]
transactions = data["transactions.csv"]
fraud = data["fraud_alerts.csv"]


check(
    (customers["annual_income"] > 0).all(),
    "Customer income is positive"
)

check(
    (accounts["balance"] >= 0).all(),
    "Account balances are non-negative"
)

check(
    (loans["loan_amount"] > 0).all(),
    "Loan amounts are positive"
)

check(
    loans["credit_score"].between(300, 850).all(),
    "Credit scores are between 300 and 850"
)

check(
    (loans["interest_rate"] > 0).all(),
    "Loan interest rates are positive"
)

check(
    (payments["due_amount"] >= 0).all(),
    "Loan payment due amounts are non-negative"
)

check(
    (payments["paid_amount"] >= 0).all(),
    "Loan payment amounts are non-negative"
)

check(
    (cards["credit_limit"] > 0).all(),
    "Credit card limits are positive"
)

check(
    (cards["current_balance"] >= 0).all(),
    "Credit card balances are non-negative"
)

check(
    (cards["current_balance"] <= cards["credit_limit"]).all(),
    "Credit card balances do not exceed limits"
)

check(
    (mortgages["property_value"] > 0).all(),
    "Mortgage property values are positive"
)

check(
    (mortgages["loan_amount"] > 0).all(),
    "Mortgage loan amounts are positive"
)

check(
    (investments["quantity"] > 0).all(),
    "Investment quantities are positive"
)

check(
    (investments["current_value"] >= 0).all(),
    "Investment values are non-negative"
)

check(
    (transactions["amount"] > 0).all(),
    "Transaction amounts are positive"
)

check(
    (fraud["fraud_amount"] >= 0).all(),
    "Fraud amounts are non-negative"
)


# ---------------------------------------------------------
# Category validation
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("CATEGORY VALIDATION")
print("=" * 70)

valid_customer_status = {
    "Active",
    "Inactive",
    "Closed",
}

check(
    set(customers["customer_status"]).issubset(
        valid_customer_status
    ),
    "Customer status values are valid"
)

valid_loan_status = {
    "Active",
    "Defaulted",
}

check(
    set(loans["loan_status"]).issubset(
        valid_loan_status
    ),
    "Loan status values are valid"
)

valid_payment_status = {
    "On Time",
    "Late",
    "Missed",
}

check(
    set(payments["payment_status"]).issubset(
        valid_payment_status
    ),
    "Payment status values are valid"
)


# ---------------------------------------------------------
# Missing value analysis
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("MISSING VALUE ANALYSIS")
print("=" * 70)

for filename, df in data.items():

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    if len(missing) == 0:
        print(f"[PASS] {filename}: no missing values")
    else:
        print(f"[INFO] {filename}: missing values found")

        for column, count in missing.items():
            percentage = count / len(df) * 100

            print(
                f"       {column:<25} "
                f"{count:>8,} "
                f"({percentage:.2f}%)"
            )


# ---------------------------------------------------------
# Final summary
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("VALIDATION COMPLETE")
print("=" * 70)