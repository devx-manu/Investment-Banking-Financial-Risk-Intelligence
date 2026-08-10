# Database Architecture

## Database

PostgreSQL

## Database Name

investment_banking_risk

## Schemas

### staging

Used for raw imported datasets before transformation and validation.

### core

Contains the cleaned relational banking data model used for analytics.

## Core Tables

1. branches
2. employees
3. customers
4. accounts
5. transactions
6. loans
7. loan_payments
8. credit_cards
9. mortgages
10. investments
11. market_data
12. digital_banking
13. atm_transactions
14. fraud_alerts
15. complaints

## Major Relationships

Customers → Accounts

Customers → Loans

Customers → Credit Cards

Customers → Mortgages

Customers → Investments

Customers → Digital Banking

Customers → ATM Transactions

Customers → Fraud Alerts

Customers → Complaints

Branches → Employees

Branches → Accounts

Branches → Loans

Branches → Mortgages

Branches → Complaints

Accounts → Transactions

Accounts → ATM Transactions

Loans → Loan Payments

Transactions → Fraud Alerts

## Architecture Flow

Python
→ CSV
→ PostgreSQL Staging
→ PostgreSQL Core
→ SQL Analytics
→ Python Analytics
→ Power BI