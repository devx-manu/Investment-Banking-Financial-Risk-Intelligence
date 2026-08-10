from pathlib import Path

import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
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


# ============================================================
# LOAD CUSTOMER RISK DATA
# ============================================================

print("=" * 70)
print("CUSTOMER RISK INTELLIGENCE")
print("=" * 70)

customer_query = """
SELECT *
FROM analytics.customer_risk_profile;
"""

df = pd.read_sql(customer_query, engine)

print(f"[LOAD] Customer risk records: {len(df):,}")


# ============================================================
# BASIC DATA VALIDATION
# ============================================================

required_columns = [
    "customer_id",
    "annual_income",
    "total_account_balance",
    "total_outstanding_amount",
    "default_count",
    "default_exposure",
    "average_credit_score",
    "total_credit_limit",
    "total_credit_card_balance",
    "credit_utilization",
    "fraud_alert_count",
    "total_fraud_amount",
    "complaint_count",
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )

print("[PASS] Required columns available")


# ============================================================
# CLEAN NUMERIC FIELDS
# ============================================================

numeric_columns = [
    "annual_income",
    "total_account_balance",
    "total_outstanding_amount",
    "default_count",
    "default_exposure",
    "average_credit_score",
    "total_credit_limit",
    "total_credit_card_balance",
    "credit_utilization",
    "total_investment_value",
    "fraud_alert_count",
    "total_fraud_amount",
    "complaint_count",
    "unresolved_complaint_count",
]

for column in numeric_columns:

    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        ).fillna(0)


# ============================================================
# FEATURE ENGINEERING
# ============================================================

# Debt-to-income proxy
df["debt_to_income"] = np.where(
    df["annual_income"] > 0,
    df["total_outstanding_amount"]
    / df["annual_income"],
    0
)


# Loan exposure relative to account balance
df["loan_to_balance_ratio"] = np.where(
    df["total_account_balance"] > 0,
    df["total_outstanding_amount"]
    / df["total_account_balance"],
    0
)


# Fraud exposure relative to income
df["fraud_to_income_ratio"] = np.where(
    df["annual_income"] > 0,
    df["total_fraud_amount"]
    / df["annual_income"],
    0
)


# ============================================================
# RISK COMPONENTS
# ============================================================

# ------------------------------------------------------------
# Credit Score Risk
# ------------------------------------------------------------

df["credit_score_risk"] = np.select(
    [
        df["average_credit_score"] < 580,
        df["average_credit_score"] < 650,
        df["average_credit_score"] < 700,
        df["average_credit_score"] < 750,
    ],
    [
        100,
        80,
        60,
        30,
    ],
    default=10
)


# ------------------------------------------------------------
# Credit Utilization Risk
# ------------------------------------------------------------

df["utilization_risk"] = np.select(
    [
        df["credit_utilization"] >= 0.90,
        df["credit_utilization"] >= 0.75,
        df["credit_utilization"] >= 0.50,
        df["credit_utilization"] >= 0.30,
    ],
    [
        100,
        80,
        60,
        30,
    ],
    default=10
)


# ------------------------------------------------------------
# Default Risk
# ------------------------------------------------------------

df["default_risk"] = np.select(
    [
        df["default_count"] >= 3,
        df["default_count"] == 2,
        df["default_count"] == 1,
    ],
    [
        100,
        80,
        60,
    ],
    default=10
)


# ------------------------------------------------------------
# Debt Risk
# ------------------------------------------------------------

df["debt_risk"] = np.select(
    [
        df["debt_to_income"] >= 5,
        df["debt_to_income"] >= 3,
        df["debt_to_income"] >= 2,
        df["debt_to_income"] >= 1,
    ],
    [
        100,
        80,
        60,
        30,
    ],
    default=10
)


# ------------------------------------------------------------
# Fraud Risk
# ------------------------------------------------------------

df["fraud_risk"] = np.select(
    [
        df["fraud_alert_count"] >= 5,
        df["fraud_alert_count"] >= 3,
        df["fraud_alert_count"] >= 1,
    ],
    [
        100,
        75,
        50,
    ],
    default=0
)


# ------------------------------------------------------------
# Complaint Risk
# ------------------------------------------------------------

df["complaint_risk"] = np.select(
    [
        df["unresolved_complaint_count"] >= 3,
        df["unresolved_complaint_count"] >= 2,
        df["unresolved_complaint_count"] >= 1,
    ],
    [
        100,
        70,
        40,
    ],
    default=0
)


# ============================================================
# FINAL RISK SCORE
# ============================================================

df["risk_score"] = (

    df["credit_score_risk"] * 0.25

    + df["utilization_risk"] * 0.20

    + df["default_risk"] * 0.20

    + df["debt_risk"] * 0.15

    + df["fraud_risk"] * 0.15

    + df["complaint_risk"] * 0.05
)


df["risk_score"] = df["risk_score"].clip(
    0,
    100
).round(2)


# ============================================================
# RISK CATEGORY
# ============================================================

df["risk_category"] = pd.cut(
    df["risk_score"],
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
# OUTLIER DETECTION
# ============================================================

outlier_features = [
    "annual_income",
    "total_outstanding_amount",
    "credit_utilization",
    "total_investment_value",
]

available_features = [
    column
    for column in outlier_features
    if column in df.columns
]

if len(available_features) >= 2:

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(
        df[available_features]
    )

    z_scores = np.abs(scaled_data)

    df["outlier_flag"] = (
        z_scores.max(axis=1) >= 3
    )

else:

    df["outlier_flag"] = False


# ============================================================
# CUSTOMER SEGMENTATION
# ============================================================

segment_features = [
    "annual_income",
    "total_account_balance",
    "total_outstanding_amount",
    "total_investment_value",
    "transaction_count"
]

segment_features = [
    column
    for column in segment_features
    if column in df.columns
]

if len(segment_features) >= 2:

    segment_data = df[segment_features].copy()

    segment_scaler = StandardScaler()

    scaled_segments = segment_scaler.fit_transform(
        segment_data
    )

    kmeans = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )

    df["customer_segment"] = (
        kmeans.fit_predict(scaled_segments)
        + 1
    )

else:

    df["customer_segment"] = 1


# ============================================================
# SEGMENT LABELS
# ============================================================

segment_summary = (
    df.groupby("customer_segment")
    .agg(
        average_income=("annual_income", "mean"),
        average_balance=("total_account_balance", "mean"),
        average_investment=("total_investment_value", "mean"),
        average_risk_score=("risk_score", "mean"),
        customer_count=("customer_id", "count")
    )
    .reset_index()
)


def classify_segment(row):

    if (
        row["average_income"] > df["annual_income"].median()
        and row["average_investment"]
        > df["total_investment_value"].median()
    ):
        return "High Value"

    if row["average_risk_score"] >= 60:
        return "High Risk"

    if row["average_balance"] > df["total_account_balance"].median():
        return "Mass Affluent"

    return "Standard"


segment_summary["segment_label"] = (
    segment_summary.apply(
        classify_segment,
        axis=1
    )
)


df = df.merge(
    segment_summary[
        [
            "customer_segment",
            "segment_label"
        ]
    ],
    on="customer_segment",
    how="left"
)


# ============================================================
# SAVE OUTPUT
# ============================================================

output_file = (
    OUTPUT_DIR
    / "customer_risk_scored.csv"
)

df.to_csv(
    output_file,
    index=False
)


segment_file = (
    OUTPUT_DIR
    / "customer_segments.csv"
)

segment_summary.to_csv(
    segment_file,
    index=False
)


# ============================================================
# SUMMARY
# ============================================================

print()
print("-" * 70)
print("RISK ANALYSIS SUMMARY")
print("-" * 70)

print(
    f"Customers analyzed: "
    f"{len(df):,}"
)

print(
    f"Average risk score: "
    f"{df['risk_score'].mean():.2f}"
)

print(
    f"High/Critical risk customers: "
    f"{(df['risk_score'] >= 75).sum():,}"
)

print(
    f"Outlier customers: "
    f"{df['outlier_flag'].sum():,}"
)

print()
print("Risk distribution:")

print(
    df["risk_category"]
    .value_counts()
    .sort_index()
)

print()
print(
    f"[SAVE] {output_file}"
)

print(
    f"[SAVE] {segment_file}"
)

print()
print("=" * 70)
print("RISK ANALYSIS COMPLETE")
print("=" * 70)