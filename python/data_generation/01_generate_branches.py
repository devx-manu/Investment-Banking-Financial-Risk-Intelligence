from pathlib import Path
import pandas as pd
import numpy as np
from faker import Faker


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

SEED = 42
NUM_BRANCHES = 100

np.random.seed(SEED)
fake = Faker("en_IN")
Faker.seed(SEED)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_ROOT / "data" / "raw"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------
# Reference data
# ---------------------------------------------------------

INDIAN_LOCATIONS = [
    ("Bengaluru", "Karnataka", "South"),
    ("Mysuru", "Karnataka", "South"),
    ("Mangaluru", "Karnataka", "South"),
    ("Hyderabad", "Telangana", "South"),
    ("Chennai", "Tamil Nadu", "South"),
    ("Coimbatore", "Tamil Nadu", "South"),
    ("Mumbai", "Maharashtra", "West"),
    ("Pune", "Maharashtra", "West"),
    ("Ahmedabad", "Gujarat", "West"),
    ("Surat", "Gujarat", "West"),
    ("Delhi", "Delhi", "North"),
    ("Jaipur", "Rajasthan", "North"),
    ("Lucknow", "Uttar Pradesh", "North"),
    ("Chandigarh", "Chandigarh", "North"),
    ("Kolkata", "West Bengal", "East"),
    ("Bhubaneswar", "Odisha", "East"),
    ("Patna", "Bihar", "East"),
    ("Guwahati", "Assam", "East"),
]

BRANCH_TYPES = [
    "Full Service",
    "Retail",
    "Corporate",
    "Digital Hub",
]


# ---------------------------------------------------------
# Generate branches
# ---------------------------------------------------------

rows = []

for branch_id in range(1, NUM_BRANCHES + 1):

    city, state, region = INDIAN_LOCATIONS[
        np.random.randint(0, len(INDIAN_LOCATIONS))
    ]

    branch_type = np.random.choice(
        BRANCH_TYPES,
        p=[0.55, 0.25, 0.15, 0.05]
    )

    opening_date = fake.date_between(
        start_date="-20y",
        end_date="-1y"
    )

    rows.append(
        {
            "branch_id": branch_id,
            "branch_name": f"{city} {branch_type} Branch {branch_id:03d}",
            "city": city,
            "state": state,
            "region": region,
            "branch_type": branch_type,
            "opening_date": opening_date,
        }
    )


branches = pd.DataFrame(rows)


# ---------------------------------------------------------
# Data validation
# ---------------------------------------------------------

assert len(branches) == NUM_BRANCHES
assert branches["branch_id"].is_unique
assert branches["branch_id"].notna().all()
assert branches["city"].notna().all()
assert branches["state"].notna().all()
assert branches["region"].notna().all()


# ---------------------------------------------------------
# Save
# ---------------------------------------------------------

output_file = OUTPUT_DIR / "branches.csv"

branches.to_csv(output_file, index=False)


# ---------------------------------------------------------
# Output summary
# ---------------------------------------------------------

print("=" * 60)
print("BRANCH DATA GENERATION COMPLETE")
print("=" * 60)

print(f"Records generated : {len(branches):,}")
print(f"Output file       : {output_file}")

print("\nBranch distribution by region:")
print(branches["region"].value_counts())

print("\nBranch distribution by type:")
print(branches["branch_type"].value_counts())

print("\nSample records:")
print(branches.head())