from pathlib import Path
import pandas as pd
import numpy as np
from faker import Faker

SEED = 42
NUM_CUSTOMERS = 25_000

np.random.seed(SEED)
fake = Faker("en_IN")
Faker.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

occupations = [
    "Software Engineer",
    "Business Owner",
    "Teacher",
    "Doctor",
    "Accountant",
    "Government Employee",
    "Sales Professional",
    "Consultant",
    "Bank Employee",
    "Student",
    "Retired",
    "Self Employed",
]

locations = [
    ("Bengaluru", "Karnataka"),
    ("Mysuru", "Karnataka"),
    ("Mangaluru", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Chennai", "Tamil Nadu"),
    ("Mumbai", "Maharashtra"),
    ("Pune", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Jaipur", "Rajasthan"),
    ("Kolkata", "West Bengal"),
]

rows = []

for customer_id in range(1, NUM_CUSTOMERS + 1):
    city, state = locations[np.random.randint(len(locations))]

    income = np.random.lognormal(mean=11.0, sigma=0.65)
    income = min(max(income, 120_000), 20_000_000)

    rows.append({
        "customer_id": customer_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "date_of_birth": fake.date_of_birth(minimum_age=21, maximum_age=75),
        "gender": np.random.choice(["Male", "Female", "Other"], p=[0.48, 0.48, 0.04]),
        "annual_income": round(income, 2),
        "occupation": np.random.choice(occupations),
        "city": city,
        "state": state,
        "customer_since": fake.date_between(start_date="-15y", end_date="-1y"),
        "customer_status": np.random.choice(
            ["Active", "Inactive", "Closed"],
            p=[0.90, 0.08, 0.02]
        ),
    })

customers = pd.DataFrame(rows)

customers.to_csv(DATA_DIR / "customers.csv", index=False)

print(f"Customers generated: {len(customers):,}")