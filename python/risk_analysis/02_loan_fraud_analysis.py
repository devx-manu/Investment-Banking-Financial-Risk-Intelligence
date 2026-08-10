from pathlib import Path

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from urllib.parse import quote_plus


# ============================================================
# CONFIGURATION
# ============================================================

ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = ROOT / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DB_NAME = "investment_banking_risk"
DB_USER = "postgres"
DB_PASSWORD = quote_plus("Siri@22032004")
DB_HOST = "localhost"
DB_PORT = "5432"


# ============================================================
# DATABASE CONNECTION
# ============================================================

connection_string = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(connection_string)


print("=" * 70)
print("LOAN & FRAUD RISK INTELLIGENCE")
print("=" * 70)


# ============================================================
# 1. LOAD LOAN RISK DATA
# ============================================================

loan_query = """
SELECT *
FROM analytics.loan_risk_analysis;
"""

loans = pd.read_sql(
    loan_query,
    engine
)

print(
    f"[LOAD] Loan records: "
    f"{len(loans):,}"
)


# ============================================================
# 2. LOAN RISK METRICS
# ============================================================

loans["loan_amount"] = pd.to_numeric(
    loans["loan_amount"],
    errors="coerce"
).fillna(0)

loans["outstanding_amount"] = pd.to_numeric(
    loans["outstanding_amount"],
    errors="coerce"
).fillna(0)

loans["credit_score"] = pd.to_numeric(
    loans["credit_score"],
    errors="coerce"
).fillna(0)

loans["interest_rate"] = pd.to_numeric(
    loans["interest_rate"],
    errors="coerce"
).fillna(0)

loans["default_flag"] = loans["default_flag"].astype(bool)


# ------------------------------------------------------------
# Loan loss exposure
# ------------------------------------------------------------

loans["npa_exposure"] = np.where(
    loans["default_flag"],
    loans["outstanding_amount"],
    0
)


# ------------------------------------------------------------
# Estimated recovery
# ------------------------------------------------------------

recovery_rate = 0.65

loans["estimated_recovery"] = (
    loans["npa_exposure"]
    * recovery_rate
)


loans["estimated_loss"] = (
    loans["npa_exposure"]
    - loans["estimated_recovery"]
)


# ============================================================
# 3. LOAN RISK SCORE
# ============================================================

loans["credit_risk_score"] = np.select(
    [
        loans["credit_score"] < 580,
        loans["credit_score"] < 650,
        loans["credit_score"] < 700,
        loans["credit_score"] < 750
    ],
    [
        100,
        80,
        60,
        30
    ],
    default=10
)


loans["loan_risk_score"] = (

    loans["credit_risk_score"] * 0.50

    + loans["default_flag"].astype(int) * 35

    + np.clip(
        loans["outstanding_ratio"] * 100,
        0,
        100
    ) * 0.15
)


loans["loan_risk_score"] = (
    loans["loan_risk_score"]
    .clip(0, 100)
    .round(2)
)


# ============================================================
# 4. LOAN RISK CATEGORY
# ============================================================

loans["loan_risk_category"] = pd.cut(
    loans["loan_risk_score"],
    bins=[
        -np.inf,
        25,
        50,
        75,
        np.inf
    ],
    labels=[
        "Low Risk",
        "Moderate Risk",
        "High Risk",
        "Critical Risk"
    ]
)


# ============================================================
# 5. LOAN TYPE SUMMARY
# ============================================================

loan_type_summary = (
    loans
    .groupby("loan_type")
    .agg(
        loan_count=("loan_id", "count"),
        total_loan_amount=("loan_amount", "sum"),
        outstanding_amount=("outstanding_amount", "sum"),
        npa_exposure=("npa_exposure", "sum"),
        estimated_loss=("estimated_loss", "sum"),
        average_credit_score=("credit_score", "mean"),
        default_count=("default_flag", "sum"),
        average_risk_score=("loan_risk_score", "mean")
    )
    .reset_index()
)


loan_type_summary["default_rate"] = (
    loan_type_summary["default_count"]
    / loan_type_summary["loan_count"]
)


# ============================================================
# 6. BRANCH RISK SUMMARY
# ============================================================

branch_risk = (
    loans
    .groupby("branch_id")
    .agg(
        loan_count=("loan_id", "count"),
        total_loan_amount=("loan_amount", "sum"),
        outstanding_amount=("outstanding_amount", "sum"),
        npa_exposure=("npa_exposure", "sum"),
        estimated_loss=("estimated_loss", "sum"),
        default_count=("default_flag", "sum"),
        average_credit_score=("credit_score", "mean"),
        average_risk_score=("loan_risk_score", "mean")
    )
    .reset_index()
)


branch_risk["default_rate"] = (
    branch_risk["default_count"]
    / branch_risk["loan_count"]
)


# ============================================================
# 7. LOAD FRAUD DATA
# ============================================================

fraud_query = """
SELECT *
FROM analytics.fraud_analysis;
"""

fraud = pd.read_sql(
    fraud_query,
    engine
)

print(
    f"[LOAD] Fraud records: "
    f"{len(fraud):,}"
)


fraud["fraud_amount"] = pd.to_numeric(
    fraud["fraud_amount"],
    errors="coerce"
).fillna(0)


fraud["transaction_amount"] = pd.to_numeric(
    fraud["transaction_amount"],
    errors="coerce"
).fillna(0)


# ============================================================
# 8. FRAUD RISK SCORE
# ============================================================

fraud["amount_ratio"] = np.where(
    fraud["transaction_amount"] > 0,
    fraud["fraud_amount"]
    / fraud["transaction_amount"],
    0
)


fraud["fraud_risk_score"] = np.select(
    [
        fraud["risk_level"].astype(str).str.lower().eq("critical"),
        fraud["risk_level"].astype(str).str.lower().eq("high"),
        fraud["risk_level"].astype(str).str.lower().eq("medium"),
        fraud["risk_level"].astype(str).str.lower().eq("low")
    ],
    [
        100,
        75,
        50,
        25
    ],
    default=50
)


fraud["fraud_risk_score"] = (
    fraud["fraud_risk_score"]
    .clip(0, 100)
)


# ============================================================
# 9. FRAUD TYPE SUMMARY
# ============================================================

fraud_type_summary = (
    fraud
    .groupby("fraud_type")
    .agg(
        alert_count=("alert_id", "count"),
        fraud_amount=("fraud_amount", "sum"),
        average_fraud_amount=("fraud_amount", "mean"),
        average_risk_score=("fraud_risk_score", "mean")
    )
    .reset_index()
)


# ============================================================
# 10. FRAUD STATUS SUMMARY
# ============================================================

fraud_status_summary = (
    fraud
    .groupby("fraud_status")
    .agg(
        alert_count=("alert_id", "count"),
        fraud_amount=("fraud_amount", "sum")
    )
    .reset_index()
)


# ============================================================
# 11. CUSTOMER FRAUD SUMMARY
# ============================================================

customer_fraud = (
    fraud
    .groupby("customer_id")
    .agg(
        fraud_alert_count=("alert_id", "count"),
        total_fraud_amount=("fraud_amount", "sum"),
        average_fraud_risk=("fraud_risk_score", "mean")
    )
    .reset_index()
)


# ============================================================
# 12. SAVE OUTPUTS
# ============================================================

loan_output = (
    OUTPUT_DIR
    / "loan_risk_scored.csv"
)

loans.to_csv(
    loan_output,
    index=False
)


loan_type_output = (
    OUTPUT_DIR
    / "loan_type_risk_summary.csv"
)

loan_type_summary.to_csv(
    loan_type_output,
    index=False
)


branch_output = (
    OUTPUT_DIR
    / "branch_risk_summary.csv"
)

branch_risk.to_csv(
    branch_output,
    index=False
)


fraud_output = (
    OUTPUT_DIR
    / "fraud_risk_scored.csv"
)

fraud.to_csv(
    fraud_output,
    index=False
)


fraud_type_output = (
    OUTPUT_DIR
    / "fraud_type_summary.csv"
)

fraud_type_summary.to_csv(
    fraud_type_output,
    index=False
)


fraud_status_output = (
    OUTPUT_DIR
    / "fraud_status_summary.csv"
)

fraud_status_summary.to_csv(
    fraud_status_output,
    index=False
)


customer_fraud_output = (
    OUTPUT_DIR
    / "customer_fraud_summary.csv"
)

customer_fraud.to_csv(
    customer_fraud_output,
    index=False
)


# ============================================================
# 13. SUMMARY
# ============================================================

print()
print("-" * 70)
print("LOAN RISK SUMMARY")
print("-" * 70)

print(
    f"Total loans: "
    f"{len(loans):,}"
)

print(
    f"Defaulted loans: "
    f"{loans['default_flag'].sum():,}"
)

print(
    f"Default rate: "
    f"{loans['default_flag'].mean():.2%}"
)

print(
    f"NPA exposure: "
    f"{loans['npa_exposure'].sum():,.2f}"
)

print(
    f"Estimated loss: "
    f"{loans['estimated_loss'].sum():,.2f}"
)

print()
print("-" * 70)
print("FRAUD SUMMARY")
print("-" * 70)

print(
    f"Fraud alerts: "
    f"{len(fraud):,}"
)

print(
    f"Fraud amount: "
    f"{fraud['fraud_amount'].sum():,.2f}"
)

print(
    f"Affected customers: "
    f"{fraud['customer_id'].nunique():,}"
)

print()
print("[SAVE] Loan risk dataset")
print("[SAVE] Loan type summary")
print("[SAVE] Branch risk summary")
print("[SAVE] Fraud risk dataset")
print("[SAVE] Fraud type summary")
print("[SAVE] Fraud status summary")
print("[SAVE] Customer fraud summary")

print()
print("=" * 70)
print("LOAN & FRAUD ANALYSIS COMPLETE")
print("=" * 70)