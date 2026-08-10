# 🏦 Investment Banking & Financial Risk Intelligence Platform

> **An end-to-end financial analytics and risk intelligence platform inspired by modern investment banking environments such as JPMorgan Chase and Goldman Sachs.**

Built to demonstrate how a **Risk Analyst / Financial Data Analyst / Business Intelligence Analyst** can transform raw banking data into actionable financial intelligence using **PostgreSQL, Advanced SQL, Python, and Power BI**.

---

## 🚀 Project Overview

Financial institutions manage massive volumes of customer, transaction, lending, investment, and fraud data.

This project builds a centralized **Investment Banking & Financial Risk Intelligence Platform** to analyze:

- 💳 Credit Risk
- 🏦 Loan Default Risk
- 🚨 Fraud Detection
- 👤 Customer Profitability
- 🏢 Branch Performance
- 📈 Investment Portfolio Risk
- 📱 Digital Banking Adoption
- 💰 Interest Income
- 🎯 Risk Exposure
- 💵 Loan Recovery
- 🏧 ATM Usage
- 📊 Non-Performing Assets (NPA)

The project follows a complete end-to-end analytics workflow:

```text
Raw Banking Data
        ↓
Data Generation
        ↓
Data Quality Validation
        ↓
PostgreSQL Database
        ↓
Advanced SQL Analytics
        ↓
Python Risk Analytics
        ↓
Power BI Data Model
        ↓
Interactive Dashboards
        ↓
Financial Risk Intelligence
```

---

# 🎯 Business Problem

A financial institution wants to reduce financial losses and improve risk management by understanding relationships between customers, accounts, loans, transactions, fraud, investments, branches, and digital banking activity.

The platform addresses questions such as:

### 💳 Credit Risk

- Which customers represent the highest credit risk?
- How does credit score influence loan exposure?
- Which customers have high credit utilization?
- Which customers require additional credit monitoring?

### 🏦 Loan Risk

- What is the overall loan default rate?
- Which loan types have the highest default risk?
- Which branches have the highest loan exposure?
- Which loans have high outstanding balances?

### 🚨 Fraud

- How much financial loss is associated with fraud?
- Which fraud types are most common?
- Which customers have repeated fraud activity?
- Which fraud alerts require investigation?

### 👤 Customer Profitability

- Which customers generate the highest value?
- Which customer segments are most profitable?
- How does customer profitability relate to risk?
- Which high-value customers also carry high financial risk?

### 🏢 Branch Performance

- Which branches generate the highest revenue?
- Which branches have the highest loan exposure?
- Which branches have strong customer activity?
- Where are risk concentrations developing?

### 📈 Portfolio Risk

- How diversified is the investment portfolio?
- Which investment categories have the highest exposure?
- Where is portfolio concentration occurring?
- How does market performance affect portfolio value?

---

# 🧰 Technology Stack

| Category | Technology |
|---|---|
| 🗄️ Database | PostgreSQL |
| 🖥️ Database Management | pgAdmin |
| 🧮 Analytics | Advanced SQL |
| 🐍 Programming | Python |
| 📊 Data Analysis | Pandas, NumPy |
| 📈 Visualization | Power BI |
| 🔄 Data Transformation | Power Query |
| 📐 BI Calculations | DAX |
| 📓 Development | Jupyter |
| 🔧 Version Control | Git |
| 🌐 Repository | GitHub |
| 📝 Documentation | Markdown / PDF |

---

# 🗃️ Banking Data

The platform works with multiple interconnected banking datasets.

## Core Datasets

```text
Customers
Accounts
Transactions
Loans
Loan Payments
Credit Cards
Mortgages
Investments
Branches
Employees
Digital Banking
ATM Transactions
Complaints
Fraud Alerts
Market Data
```

## Dataset Scale

| Dataset | Records |
|---|---:|
| 👤 Customers | 25,000 |
| 💳 Accounts | 40,000 |
| 💰 Transactions | 1,000,000 |
| 🏦 Loans | 15,000 |
| 💵 Loan Payments | 150,000 |
| 💳 Credit Cards | 20,000 |
| 🏠 Mortgages | 8,000 |
| 📈 Investments | 30,000 |
| 📱 Digital Banking | 300,000 |
| 🏧 ATM Transactions | 250,000 |
| 🚨 Fraud Alerts | 10,000 |
| 📝 Complaints | 30,000 |
| 🏢 Branches | 100 |
| 👔 Employees | 1,500 |
| 📊 Market Data | 6,258 |

---

# 🏗️ Project Architecture

```text
                         ┌──────────────────────┐
                         │   Banking Data       │
                         │ Customers / Loans /  │
                         │ Transactions / Fraud │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Python Data          │
                         │ Generation           │
                         │ Pandas + NumPy       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Data Quality Layer   │
                         │ Validation & Checks  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ PostgreSQL           │
                         │ Banking Database     │
                         └──────────┬───────────┘
                                    │
                      ┌─────────────┴─────────────┐
                      │                           │
                      ▼                           ▼
             ┌─────────────────┐        ┌─────────────────┐
             │ Advanced SQL    │        │ Python Analytics│
             │ Risk Views      │        │ Risk Scoring    │
             └────────┬────────┘        └────────┬────────┘
                      │                           │
                      └─────────────┬─────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Power BI             │
                         │ Data Model + DAX     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Financial Risk       │
                         │ Intelligence         │
                         └──────────────────────┘
```

---

# 🗄️ Database Architecture

PostgreSQL acts as the central analytical database.

The database is organized into logical layers:

```text
PostgreSQL
│
├── core
│   ├── customers
│   ├── accounts
│   ├── transactions
│   ├── loans
│   ├── loan_payments
│   ├── credit_cards
│   ├── mortgages
│   ├── investments
│   ├── branches
│   ├── employees
│   ├── digital_banking
│   ├── atm_transactions
│   ├── fraud_alerts
│   ├── complaints
│   └── market_data
│
└── analytics
    ├── customer_risk_profile
    ├── loan_risk_analysis
    ├── fraud_analysis
    └── customer_profitability
```

---

# 🧮 Advanced SQL Analytics

The project demonstrates practical SQL techniques used for financial analytics and business intelligence.

### SQL Techniques

- CTEs
- Window Functions
- Ranking
- Recursive Queries
- Multi-table Joins
- Aggregations
- Conditional Logic
- Date Functions
- Time Intelligence
- Views
- Stored Procedures
- Query Optimization

### Analytical Views

```text
analytics.customer_risk_profile
analytics.loan_risk_analysis
analytics.fraud_analysis
analytics.customer_profitability
```

These views create a dedicated analytical layer between the core banking database and Power BI.

---

# 🐍 Python Analytics

Python is used for data generation, data validation, risk scoring, segmentation, fraud analysis, and statistical analysis.

## Python Workflow

```text
Data Generation
       ↓
Data Validation
       ↓
Risk Scoring
       ↓
Customer Segmentation
       ↓
Fraud Analysis
       ↓
Loan Risk Analysis
       ↓
Statistical Analysis
```

## Analytics Performed

- 🔍 Outlier Detection
- 🎯 Risk Scoring
- 👥 Customer Segmentation
- 📊 Statistical Analysis
- 📈 Correlation Analysis
- 🚨 Fraud Analysis
- 🏦 Loan Risk Analysis
- 📉 Default Risk Analysis
- 💳 Credit Risk Analysis

---

# 🎯 Risk Scoring

The platform combines multiple financial indicators to build analytical risk profiles.

```text
Credit Score
     +
Loan Exposure
     +
Outstanding Balance
     +
Default History
     +
Credit Utilization
     +
Fraud Activity
     +
Financial Profile
     ↓
Customer Risk Profile
```

Risk categories can be interpreted as:

```text
🟢 Low Risk
🟡 Medium Risk
🟠 High Risk
🔴 Critical Risk
```

The risk framework helps identify customers and financial relationships requiring additional monitoring.

---

# 📊 Power BI Dashboards

The Power BI solution contains multiple dashboard perspectives for different banking stakeholders.

---

## 1️⃣ Executive Dashboard

Provides a high-level view of financial performance and risk.

### Key Metrics

- Total Customers
- Total Loan Exposure
- Default Rate
- Fraud Loss
- Interest Income
- Customer Profitability
- Risk Exposure
- Branch Revenue

### Purpose

Provides executives with a consolidated view of the institution's financial health and major risk indicators.

---

# 2️⃣ Risk Dashboard

Focuses on overall financial risk.

### Analysis

- Customer Risk Scores
- Loan Default Risk
- Risk Distribution
- Outstanding Exposure
- High-Risk Customers
- Default Trends
- Risk Concentration

### Purpose

Helps risk teams identify areas of elevated financial exposure.

---

# 3️⃣ Credit Dashboard

Analyzes customer credit behavior and lending risk.

### Analysis

- Credit Score Distribution
- Credit Utilization
- Loan Amount vs Credit Score
- Loan Approval Patterns
- Loan Risk Categories
- Credit Risk Segmentation

### Purpose

Supports credit assessment and lending decisions.

---

# 4️⃣ Fraud Dashboard

Focuses on suspicious financial activity.

### Analysis

- Fraud Loss
- Fraud Alert Volume
- Fraud Types
- Fraud Resolution Status
- High-Risk Customers
- Transaction Risk
- Fraud Concentration

### Purpose

Helps identify suspicious activity and prioritize investigation.

---

# 5️⃣ Branch Dashboard

Measures branch-level performance and risk.

### Analysis

- Branch Revenue
- Loan Exposure
- Customer Count
- Branch Risk
- Top Performing Branches
- Regional Performance
- Loan Concentration

### Purpose

Supports branch performance management and resource allocation.

---

# 6️⃣ Portfolio Dashboard

Provides investment portfolio intelligence.

### Analysis

- Portfolio Value
- Investment Exposure
- Asset Distribution
- Portfolio Diversification
- Market Performance
- Risk Concentration

### Purpose

Provides visibility into investment exposure and diversification.

---

# 7️⃣ Customer Dashboard

Provides customer-level financial intelligence.

### Analysis

- Customer Profitability
- Customer Risk
- Credit Score
- Account Activity
- Product Ownership
- Digital Adoption
- Customer Segment

### Purpose

Helps understand customer value, behavior, and risk simultaneously.

---

# 📌 Key KPIs

| KPI | Business Purpose |
|---|---|
| 📉 Default Rate | Measures loan default risk |
| 💳 Credit Score | Measures customer credit quality |
| ⚠️ NPA | Measures stressed loan exposure |
| 🚨 Fraud Loss | Measures financial fraud impact |
| 💵 Loan Recovery | Measures recovery performance |
| 💰 Interest Income | Measures lending revenue |
| 👤 Customer Profitability | Measures customer value |
| 🎯 Risk Exposure | Measures financial risk concentration |
| 🏦 Capital Allocation | Supports resource allocation |
| 🏢 Branch Revenue | Measures branch performance |

---

# 🔬 Key Analytical Questions

The platform is designed to answer practical financial business questions.

### Loan Risk

> Which loans have high outstanding exposure and weak credit profiles?

### Credit Risk

> Which customers have low credit scores combined with high financial exposure?

### Fraud

> Which fraud types generate the greatest financial losses?

### Customer Profitability

> Which customers generate the greatest value for the institution?

### Branch Performance

> Which branches combine high revenue with high loan exposure?

### Portfolio Risk

> How diversified is the investment portfolio?

### Digital Banking

> Which customers are actively adopting digital banking services?

---

# 🧪 Data Quality Framework

Before analytical processing, the banking datasets are validated through automated Python checks.

## Validation Areas

```text
✓ Primary Key Validation
✓ Duplicate Detection
✓ NULL Detection
✓ Foreign Key Validation
✓ Numeric Range Validation
✓ Business Rule Validation
✓ Date Validation
✓ Status Validation
✓ Credit Score Validation
✓ Loan Amount Validation
✓ Transaction Amount Validation
✓ Fraud Amount Validation
✓ Credit Card Limit Validation
```

Example validation output:

```text
[PASS] Primary keys contain no NULL values
[PASS] Primary keys contain no duplicates
[PASS] Foreign key relationships validated
[PASS] Credit scores within valid range
[PASS] Loan amounts are positive
[PASS] Transaction amounts are positive
[PASS] Credit card balances within limits
[PASS] Fraud amounts are non-negative
```

---

# 📁 Project Structure

```text
Investment-Banking-Risk-Intelligence/
│
├── 📂 data/
│   ├── 📂 raw/
│   │   ├── accounts.csv
│   │   ├── branches.csv
│   │   ├── complaints.csv
│   │   ├── credit_cards.csv
│   │   ├── customers.csv
│   │   ├── employees.csv
│   │   ├── fraud_alerts.csv
│   │   ├── investments.csv
│   │   ├── loans.csv
│   │   ├── market_data.csv
│   │   └── mortgages.csv
│   │
│   └── 📂 processed/
│
├── 📂 database/
│   ├── 📂 01_schema/
│   │   ├── 01_create_schemas.sql
│   │   └── 02_create_core_tables.sql
│   │
│   └── 📂 04_views/
│       ├── 01_customer_risk.sql
│       ├── 02_loan_risk.sql
│       ├── 03_fraud_analysis.sql
│       └── 04_customer_profitability.sql
│
├── 📂 python/
│   ├── 00_environment_test.py
│   │
│   ├── 📂 data_generation/
│   │   ├── 01_generate_branches.py
│   │   ├── 02_generate_employees.py
│   │   ├── 03_generate_customers.py
│   │   ├── 04_generate_accounts.py
│   │   ├── 05_generate_transactions.py
│   │   ├── 06_generate_loans.py
│   │   ├── 07_generate_loan_payments.py
│   │   ├── 08_generate_credit_cards.py
│   │   ├── 09_generate_mortgages.py
│   │   ├── 10_generate_investments.py
│   │   ├── 11_generate_market_data.py
│   │   ├── 12_generate_digital_banking.py
│   │   ├── 13_generate_atm_transactions.py
│   │   ├── 14_generate_fraud_alerts.py
│   │   ├── 15_generate_complaints.py
│   │   └── 16_validate_generated_data.py
│   │
│   ├── 📂 data_quality/
│   │   └── 01_validate_raw_data.py
│   │
│   ├── 📂 database/
│   │   └── 01_load_csv_to_postgres.py
│   │
│   └── 📂 risk_analysis/
│       ├── 01_customer_risk_scoring.py
│       └── 02_loan_fraud_analysis.py
│
├── 📂 powerbi/
│   └── Investment_Banking_Risk_Intelligence.pbix
│
├── 📂 documentation/
│   ├── 01_database_architecture.md
│   ├── 02_data_dictionary.md
│   ├── 03_data_generation_plan.md
│   ├── 04_data_quality_report.md
│   └── 05_database_architecture.md
│
├── 📂 screenshots/
│
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md
```

---

# ⚙️ Project Execution

## 1. Clone Repository

```bash
git clone https://github.com/devx-manu/Investment-Banking-Financial-Risk-Intelligence.git
```

```bash
cd Investment-Banking-Financial-Risk-Intelligence
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate on Windows:

```powershell
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Generate Banking Data

Run the data-generation scripts in sequence:

```text
01_generate_branches.py
02_generate_employees.py
03_generate_customers.py
04_generate_accounts.py
05_generate_transactions.py
06_generate_loans.py
07_generate_loan_payments.py
08_generate_credit_cards.py
09_generate_mortgages.py
10_generate_investments.py
11_generate_market_data.py
12_generate_digital_banking.py
13_generate_atm_transactions.py
14_generate_fraud_alerts.py
15_generate_complaints.py
```

---

## 5. Validate Generated Data

Run:

```bash
python python/data_quality/01_validate_raw_data.py
```

The validation framework checks the generated banking datasets before database loading.

---

## 6. Create PostgreSQL Database

Open **pgAdmin** and execute:

```text
database/01_schema/01_create_schemas.sql
```

Then:

```text
database/01_schema/02_create_core_tables.sql
```

---

## 7. Load Data into PostgreSQL

Run:

```bash
python python/database/01_load_csv_to_postgres.py
```

---

## 8. Create Analytical Views

Execute the SQL scripts under:

```text
database/04_views/
```

These scripts create the analytical layer used by Power BI and Python analytics.

---

## 9. Run Python Risk Analytics

Run:

```bash
python python/risk_analysis/01_customer_risk_scoring.py
```

Then:

```bash
python python/risk_analysis/02_loan_fraud_analysis.py
```

---

## 10. Open Power BI

Open:

```text
powerbi/Investment_Banking_Risk_Intelligence.pbix
```

Refresh the model and explore the dashboards.

---

# 💡 Business Insights Enabled

The platform enables stakeholders to identify:

## 🔴 High-Risk Exposure

Customers and loans with combinations of:

- Low credit scores
- High loan exposure
- High outstanding balances
- Default indicators

## 🚨 Fraud Concentration

Fraud analysis identifies:

- Fraud type distribution
- Fraud losses
- Alert volumes
- Resolution status
- Customer-level fraud exposure

## 🏢 Branch Risk

Branch-level analysis identifies locations with significant loan exposure and potential risk concentration.

## 👤 Customer Value

Customer profitability analysis enables segmentation such as:

```text
High Value + Low Risk
High Value + High Risk
Low Value + Low Risk
Low Value + High Risk
```

This allows financial institutions to apply more targeted customer and risk strategies.

---

# 📈 Business Recommendations

### 1. Strengthen High-Risk Loan Monitoring

Prioritize loans combining high exposure with elevated risk indicators.

### 2. Improve Credit-Based Decision Making

Use credit score, exposure, repayment behavior, and customer financial characteristics together when evaluating credit risk.

### 3. Prioritize Fraud Investigations

Focus investigation resources on alerts associated with higher financial exposure and repeated suspicious activity.

### 4. Improve Portfolio Diversification

Monitor concentration across investment categories and reduce excessive exposure to individual asset groups.

### 5. Optimize Branch Strategy

Compare branch revenue, customer activity, loan exposure, and risk to improve resource allocation.

### 6. Increase Digital Adoption

Identify customers with low digital engagement and develop targeted digital banking strategies.

---

# 📊 Portfolio Highlights

This project demonstrates the complete financial analytics lifecycle:

```text
                 FINANCIAL DATA
                       │
                       ▼
               DATA GENERATION
                       │
                       ▼
                DATA QUALITY
                       │
                       ▼
                POSTGRESQL
                       │
                       ▼
                ADVANCED SQL
                       │
                       ▼
              PYTHON ANALYTICS
                       │
                       ▼
                 RISK SCORING
                       │
                       ▼
                  POWER BI
                       │
                       ▼
            BUSINESS INTELLIGENCE
```

## Technical Skills Demonstrated

```text
Python
SQL
PostgreSQL
Power BI
Excel
DAX
Power Query
Pandas
NumPy
Data Analytics
Business Intelligence
Financial Analytics
Credit Risk Analysis
Fraud Analytics
Customer Segmentation
Risk Scoring
Data Quality
Git & GitHub
```

---

# 📚 Documentation

Detailed project documentation is available in:

```text
documentation/
```

Documentation includes:

- Database Architecture
- Data Dictionary
- Data Generation Plan
- Data Quality Report
- Analytics Architecture
- Dashboard Design
- KPI Framework
- Business Recommendations

---

# 🔮 Future Enhancements

Potential future improvements include:

- 🤖 Machine Learning Default Prediction
- 🚨 Real-Time Fraud Detection
- 📈 Time-Series Risk Forecasting
- 🧠 Customer Lifetime Value Prediction
- 🏦 Basel Risk Metrics
- 📊 Automated Risk Reporting
- ☁️ Cloud Data Warehouse Integration
- 🔄 Automated ETL Pipelines
- 📡 Real-Time Transaction Monitoring
- 🧬 Advanced Portfolio Optimization

---

# 🏆 Project Outcome

The **Investment Banking & Financial Risk Intelligence Platform** demonstrates how raw financial data can be transformed into a structured analytical ecosystem.

The project combines:

```text
Data Engineering
      +
Database Design
      +
Advanced SQL
      +
Python Analytics
      +
Risk Intelligence
      +
Business Intelligence
      +
Power BI
```

into an end-to-end financial analytics solution.

The final platform provides analytical capabilities across:

```text
Credit Risk
Loan Defaults
Fraud Detection
Customer Profitability
Branch Performance
Portfolio Risk
Digital Banking
Credit Utilization
NPA Analysis
Risk Scoring
```

---

# 👨‍💻 Author

## Manu S

📍 Bengaluru, India

🎓 Bachelor of Computer Applications (BCA)

📊 Data Analytics | Business Intelligence | Financial Analytics

### Core Skills

```text
Python
SQL
PostgreSQL
Power BI
Excel
DAX
Pandas
NumPy
Data Analytics
Business Intelligence
Financial Analytics
```

---

# ⭐ Project

**Investment Banking & Financial Risk Intelligence Platform**

Built as a portfolio project demonstrating end-to-end **Financial Data Analytics, Risk Intelligence, SQL Analytics, Python Analytics, and Business Intelligence** capabilities.

---
