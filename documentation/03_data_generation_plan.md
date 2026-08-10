# Data Generation Plan

## Data Strategy

Synthetic banking data will be generated using Python for portfolio and analytical demonstration purposes.

The generated data will simulate a large financial institution and will contain realistic relationships between customers, accounts, transactions, loans, investments, branches, fraud events, and digital banking activity.

## Historical Period

January 2022 through December 2025.

## Target Dataset Size

| Table | Target Records |
|---|---:|
| Customers | 25,000 |
| Branches | 100 |
| Employees | 1,500 |
| Accounts | 40,000 |
| Transactions | 1,000,000 |
| Loans | 15,000 |
| Loan Payments | 150,000 |
| Credit Cards | 20,000 |
| Mortgages | 8,000 |
| Investments | 30,000 |
| Market Data | 100,000 |
| Digital Banking | 300,000 |
| ATM Transactions | 250,000 |
| Fraud Alerts | 10,000 |
| Complaints | 30,000 |

## Generation Principles

The data should contain realistic business relationships rather than completely independent random values.

Examples:

- Income should influence borrowing capacity.
- Credit score should influence loan risk.
- Debt levels should influence default probability.
- Payment behavior should influence delinquency.
- Credit utilization should influence credit risk.
- Transaction behavior should influence fraud probability.
- Customer activity should influence digital adoption.
- Customer characteristics should influence investment behavior.
- Branch location should influence customer and transaction distribution.

## Generation Order

1. Branches
2. Employees
3. Customers
4. Accounts
5. Transactions
6. Loans
7. Loan Payments
8. Credit Cards
9. Mortgages
10. Investments
11. Market Data
12. Digital Banking
13. ATM Transactions
14. Fraud Alerts
15. Complaints
16. Data Validation

## Output Format

Generated datasets will initially be stored as CSV files inside:

data/raw/