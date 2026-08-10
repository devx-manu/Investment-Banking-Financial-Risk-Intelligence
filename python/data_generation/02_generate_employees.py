from pathlib import Path
import pandas as pd
import numpy as np
from faker import Faker

SEED = 42
NUM_EMPLOYEES = 1500

np.random.seed(SEED)
fake = Faker("en_IN")
Faker.seed(SEED)

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "raw"

branches = pd.read_csv(DATA_DIR / "branches.csv")

roles = [
    "Relationship Manager",
    "Loan Officer",
    "Credit Analyst",
    "Branch Manager",
    "Teller",
    "Customer Service Officer",
    "Operations Officer",
    "Investment Advisor",
    "Risk Analyst",
    "Fraud Analyst",
]

rows = []

for employee_id in range(1, NUM_EMPLOYEES + 1):
    branch_id = np.random.choice(branches["branch_id"])

    rows.append({
        "employee_id": employee_id,
        "branch_id": branch_id,
        "employee_name": fake.name(),
        "job_role": np.random.choice(roles),
        "hire_date": fake.date_between(start_date="-15y", end_date="-30d"),
        "salary": round(np.random.lognormal(mean=11.0, sigma=0.35), 2),
        "employment_status": np.random.choice(
            ["Active", "Leave", "Resigned"],
            p=[0.92, 0.03, 0.05]
        ),
    })

employees = pd.DataFrame(rows)

employees.to_csv(DATA_DIR / "employees.csv", index=False)

print(f"Employees generated: {len(employees):,}")