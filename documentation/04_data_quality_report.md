# Data Quality Report

## Objective

Validate the synthetic banking datasets before loading them into PostgreSQL.

## Validation Areas

### 1. File Validation

- All expected datasets exist.
- Dataset record counts are checked.

### 2. Primary Key Validation

Each table is checked for:
- NULL primary keys
- Duplicate primary keys

### 3. Foreign Key Validation

Relationships are checked between:
- Customers and Accounts
- Customers and Loans
- Accounts and Transactions
- Loans and Loan Payments
- Customers and Credit Cards
- Customers and Mortgages
- Customers and Investments
- Customers and Digital Banking
- Customers and ATM Transactions
- Transactions and Fraud Alerts
- Customers and Complaints
- Branches and operational tables

### 4. Business Rule Validation

Examples:
- Credit scores must be between 300 and 850.
- Loan amounts must be positive.
- Account balances cannot be negative.
- Credit card balances cannot exceed credit limits.
- Investment values cannot be negative.

### 5. Missing Value Analysis

All datasets are analyzed for missing values.

## Validation Status

Pending execution.