from pathlib import Path
import pandas as pd
import numpy as np


# ============================================================
# CONFIGURATION
# ============================================================

SEED = 42
NUM_LOANS = 15_000

np.random.seed(SEED)


# ============================================================
# PATHS
# ============================================================

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"


# ============================================================
# LOAD SOURCE DATA
# ============================================================

customers = pd.read_csv(
    DATA_DIR / "customers.csv"
)

branches = pd.read_csv(
    DATA_DIR / "branches.csv"
)


# ============================================================
# LOAN CONFIGURATION
# ============================================================

loan_types = [
    "Personal",
    "Home",
    "Auto",
    "Business",
    "Education"
]


application_start = pd.Timestamp("2022-01-01")
application_end = pd.Timestamp("2025-06-30")


# ============================================================
# GENERATE LOANS
# ============================================================

rows = []


for loan_id in range(1, NUM_LOANS + 1):

    # --------------------------------------------------------
    # Select customer
    # --------------------------------------------------------

    customer = customers.sample(
        1,
        random_state=None
    ).iloc[0]


    # --------------------------------------------------------
    # Credit score
    # --------------------------------------------------------

    credit_score = int(
        np.clip(
            np.random.normal(710, 70),
            300,
            850
        )
    )


    # --------------------------------------------------------
    # Loan amount
    # --------------------------------------------------------

    loan_amount = np.random.lognormal(
        12.0,
        0.8
    )

    loan_amount = min(
        max(loan_amount, 50_000),
        10_000_000
    )


    # --------------------------------------------------------
    # Default probability
    # --------------------------------------------------------

    risk_probability = (
        0.03
        + max(0, 650 - credit_score) / 3000
        + min(
            loan_amount / 50_000_000,
            0.10
        )
    )


    # --------------------------------------------------------
    # Default status
    # --------------------------------------------------------

    default_flag = (
        np.random.random()
        < risk_probability
    )

    status = (
        "Defaulted"
        if default_flag
        else "Active"
    )


    # --------------------------------------------------------
    # Application date
    # --------------------------------------------------------

    application_date = (
        application_start
        + pd.Timedelta(
            days=np.random.randint(
                0,
                (
                    application_end
                    - application_start
                ).days + 1
            )
        )
    )


    # --------------------------------------------------------
    # Approval date
    #
    # Approval is ALWAYS after application.
    # Approval delay = 1 to 30 days.
    # --------------------------------------------------------

    approval_delay = np.random.randint(
        1,
        31
    )

    approval_date = (
        application_date
        + pd.Timedelta(
            days=approval_delay
        )
    )


    # --------------------------------------------------------
    # Interest rate
    # --------------------------------------------------------

    interest_rate = round(
        np.random.uniform(
            7.0,
            18.0
        ),
        3
    )


    # --------------------------------------------------------
    # Tenure
    # --------------------------------------------------------

    tenure_months = int(
        np.random.choice(
            [
                12,
                24,
                36,
                48,
                60,
                84,
                120
            ]
        )
    )


    # --------------------------------------------------------
    # Outstanding amount
    # --------------------------------------------------------

    outstanding_amount = round(
        loan_amount
        * np.random.uniform(
            0.10,
            0.95
        ),
        2
    )


    # --------------------------------------------------------
    # Create record
    # --------------------------------------------------------

    rows.append({

        "loan_id": loan_id,

        "customer_id": customer["customer_id"],

        "branch_id": np.random.choice(
            branches["branch_id"]
        ),

        "loan_type": np.random.choice(
            loan_types
        ),

        "application_date": application_date,

        "approval_date": approval_date,

        "loan_amount": round(
            loan_amount,
            2
        ),

        "interest_rate": interest_rate,

        "tenure_months": tenure_months,

        "credit_score": credit_score,

        "loan_status": status,

        "default_flag": bool(
            default_flag
        ),

        "outstanding_amount": outstanding_amount
    })


# ============================================================
# CREATE DATAFRAME
# ============================================================

loans = pd.DataFrame(rows)


# ============================================================
# DATA QUALITY CHECKS
# ============================================================

invalid_dates = (
    loans["approval_date"]
    < loans["application_date"]
).sum()

if invalid_dates > 0:
    raise ValueError(
        f"Found {invalid_dates:,} loans "
        "where approval_date is earlier "
        "than application_date."
    )


if loans["loan_id"].duplicated().any():
    raise ValueError(
        "Duplicate loan_id values detected."
    )


if loans["customer_id"].isna().any():
    raise ValueError(
        "NULL customer_id values detected."
    )


if loans["branch_id"].isna().any():
    raise ValueError(
        "NULL branch_id values detected."
    )


if not loans["credit_score"].between(
    300,
    850
).all():
    raise ValueError(
        "Invalid credit score detected."
    )


if not (
    loans["loan_amount"] > 0
).all():
    raise ValueError(
        "Invalid loan amount detected."
    )


if not (
    loans["interest_rate"] > 0
).all():
    raise ValueError(
        "Invalid interest rate detected."
    )


# ============================================================
# SAVE
# ============================================================

output_path = DATA_DIR / "loans.csv"

loans.to_csv(
    output_path,
    index=False
)


# ============================================================
# SUMMARY
# ============================================================

print("=" * 60)
print("LOAN DATA GENERATION COMPLETE")
print("=" * 60)

print(
    f"Loans generated : {len(loans):,}"
)

print(
    f"Default rate    : "
    f"{loans['default_flag'].mean():.2%}"
)

print(
    f"Invalid dates   : "
    f"{invalid_dates:,}"
)

print(
    f"Output file     : "
    f"{output_path}"
)

print("=" * 60)