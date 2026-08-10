from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus


# ============================================================
# CONFIGURATION
# ============================================================

DB_USER = "postgres"
DB_PASSWORD = quote_plus("Siri@22032004")
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "investment_banking_risk"

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"


# ============================================================
# DATABASE CONNECTION
# ============================================================

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/"
    f"{DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


# ============================================================
# LOAD CONFIGURATION
# ============================================================

TABLES = [
    ("branches.csv", "branches"),
    ("employees.csv", "employees"),
    ("customers.csv", "customers"),
    ("accounts.csv", "accounts"),
    ("transactions.csv", "transactions"),
    ("loans.csv", "loans"),
    ("loan_payments.csv", "loan_payments"),
    ("credit_cards.csv", "credit_cards"),
    ("mortgages.csv", "mortgages"),
    ("investments.csv", "investments"),
    ("market_data.csv", "market_data"),
    ("digital_banking.csv", "digital_banking"),
    ("atm_transactions.csv", "atm_transactions"),
    ("fraud_alerts.csv", "fraud_alerts"),
    ("complaints.csv", "complaints"),
]


# ============================================================
# TEST CONNECTION
# ============================================================

print("=" * 70)
print("POSTGRESQL CONNECTION TEST")
print("=" * 70)

try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database(), current_user;")
        )

        database, user = result.fetchone()

        print(f"Database : {database}")
        print(f"User     : {user}")
        print("Connection successful.")

except Exception as error:
    print("Database connection failed.")
    print(error)
    raise SystemExit(1)


# ============================================================
# LOAD DATA
# ============================================================

print("\n" + "=" * 70)
print("LOADING CSV DATA INTO POSTGRESQL")
print("=" * 70)

for filename, table_name in TABLES:

    file_path = DATA_DIR / filename

    if not file_path.exists():
        print(f"[ERROR] File not found: {filename}")
        continue

    print(f"\nLoading {filename} → core.{table_name}")

    try:

        df = pd.read_csv(file_path)

        # Convert date columns appropriately
        for column in df.columns:

            if (
                "date" in column.lower()
                or column.lower().endswith("_date")
            ):
                df[column] = pd.to_datetime(
                    df[column],
                    errors="coerce"
                )

        # PostgreSQL cannot use NaN for nullable values
        df = df.where(
            pd.notnull(df),
            None
        )

        # Transactions and other large tables
        # are loaded in chunks.
        chunk_size = 50_000

        first_chunk = True

        for start in range(
            0,
            len(df),
            chunk_size
        ):

            chunk = df.iloc[
                start:start + chunk_size
            ]

            chunk.to_sql(
                table_name,
                engine,
                schema="core",
                if_exists="append",
                index=False,
                method="multi"
            )

            print(
                f"   Loaded rows "
                f"{start + 1:,} - "
                f"{min(start + chunk_size, len(df)):,}"
            )

        print(
            f"[SUCCESS] {table_name}: "
            f"{len(df):,} rows loaded"
        )

    except Exception as error:

        print(
            f"[ERROR] Failed loading "
            f"{table_name}"
        )

        print(error)

        raise


# ============================================================
# FINAL ROW COUNTS
# ============================================================

print("\n" + "=" * 70)
print("POSTGRESQL LOAD SUMMARY")
print("=" * 70)

with engine.connect() as connection:

    for _, table_name in TABLES:

        result = connection.execute(
            text(
                f"""
                SELECT COUNT(*)
                FROM core.{table_name};
                """
            )
        )

        count = result.scalar()

        print(
            f"core.{table_name:<25} "
            f"{count:>12,} rows"
        )


print("\n" + "=" * 70)
print("DATA LOAD COMPLETE")
print("=" * 70)