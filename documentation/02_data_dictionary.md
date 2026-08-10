# Data Dictionary

## 1. customers

| Column | Data Type | Key | Description |
|---|---|---|---|
| customer_id | BIGINT | PK | Unique customer identifier |
| first_name | VARCHAR(100) | | Customer first name |
| last_name | VARCHAR(100) | | Customer last name |
| date_of_birth | DATE | | Customer date of birth |
| gender | VARCHAR(20) | | Customer gender |
| annual_income | DECIMAL(15,2) | | Annual customer income |
| occupation | VARCHAR(100) | | Customer occupation |
| city | VARCHAR(100) | | Customer city |
| state | VARCHAR(100) | | Customer state |
| customer_since | DATE | | Date customer joined bank |
| customer_status | VARCHAR(30) | | Active, Inactive, Closed |

---

## 2. accounts

| Column | Data Type | Key | Description |
|---|---|---|---|
| account_id | BIGINT | PK | Unique account identifier |
| customer_id | BIGINT | FK | Linked customer |
| branch_id | INT | FK | Account's primary branch |
| account_type | VARCHAR(50) | | Savings, Current, Salary, etc. |
| open_date | DATE | | Account opening date |
| balance | DECIMAL(18,2) | | Current account balance |
| currency | CHAR(3) | | Account currency |
| account_status | VARCHAR(30) | | Active, Dormant, Closed |

---

## 3. transactions

| Column | Data Type | Key | Description |
|---|---|---|---|
| transaction_id | BIGINT | PK | Unique transaction identifier |
| account_id | BIGINT | FK | Account involved |
| customer_id | BIGINT | FK | Customer involved |
| transaction_date | TIMESTAMP | | Transaction timestamp |
| transaction_type | VARCHAR(50) | | Debit, Credit, Transfer |
| transaction_category | VARCHAR(100) | | Transaction business category |
| amount | DECIMAL(18,2) | | Transaction amount |
| merchant | VARCHAR(150) | | Merchant or counterparty |
| channel | VARCHAR(50) | | ATM, Branch, Mobile, Online, POS |
| location | VARCHAR(150) | | Transaction location |
| status | VARCHAR(30) | | Completed, Failed, Reversed |

---

## 4. loans

| Column | Data Type | Key | Description |
|---|---|---|---|
| loan_id | BIGINT | PK | Unique loan identifier |
| customer_id | BIGINT | FK | Borrowing customer |
| branch_id | INT | FK | Loan-originating branch |
| loan_type | VARCHAR(50) | | Personal, Auto, Business, Education, etc. |
| application_date | DATE | | Loan application date |
| approval_date | DATE | | Loan approval date |
| loan_amount | DECIMAL(18,2) | | Original approved loan amount |
| interest_rate | DECIMAL(6,3) | | Annual interest rate |
| tenure_months | INT | | Loan tenure |
| credit_score | INT | | Credit score at approval |
| loan_status | VARCHAR(30) | | Active, Closed, Defaulted, Rejected |
| default_flag | BOOLEAN | | Whether loan defaulted |
| outstanding_amount | DECIMAL(18,2) | | Current outstanding balance |

---

## 5. loan_payments

| Column | Data Type | Key | Description |
|---|---|---|---|
| payment_id | BIGINT | PK | Unique payment identifier |
| loan_id | BIGINT | FK | Related loan |
| payment_date | DATE | | Payment date |
| due_amount | DECIMAL(18,2) | | Amount due |
| paid_amount | DECIMAL(18,2) | | Amount actually paid |
| days_late | INT | | Number of days payment was late |
| payment_status | VARCHAR(30) | | On Time, Late, Missed, Partial |

---

## 6. credit_cards

| Column | Data Type | Key | Description |
|---|---|---|---|
| credit_card_id | BIGINT | PK | Unique credit card identifier |
| customer_id | BIGINT | FK | Cardholder |
| issue_date | DATE | | Card issue date |
| credit_limit | DECIMAL(18,2) | | Approved credit limit |
| current_balance | DECIMAL(18,2) | | Current outstanding balance |
| interest_rate | DECIMAL(6,3) | | Annual interest rate |
| card_status | VARCHAR(30) | | Active, Blocked, Closed |

---

## 7. mortgages

| Column | Data Type | Key | Description |
|---|---|---|---|
| mortgage_id | BIGINT | PK | Unique mortgage identifier |
| customer_id | BIGINT | FK | Borrowing customer |
| branch_id | INT | FK | Mortgage-originating branch |
| property_value | DECIMAL(18,2) | | Property market value |
| loan_amount | DECIMAL(18,2) | | Original mortgage amount |
| interest_rate | DECIMAL(6,3) | | Annual interest rate |
| term_years | INT | | Mortgage term |
| start_date | DATE | | Mortgage start date |
| outstanding_balance | DECIMAL(18,2) | | Current outstanding balance |
| mortgage_status | VARCHAR(30) | | Active, Closed, Defaulted |

---

## 8. investments

| Column | Data Type | Key | Description |
|---|---|---|---|
| investment_id | BIGINT | PK | Unique investment identifier |
| customer_id | BIGINT | FK | Investor |
| investment_type | VARCHAR(50) | | Equity, Bond, Mutual Fund, ETF, etc. |
| asset_name | VARCHAR(150) | | Asset/security name |
| investment_date | DATE | | Investment purchase date |
| quantity | DECIMAL(18,6) | | Units/shares held |
| purchase_price | DECIMAL(18,2) | | Purchase price per unit |
| current_value | DECIMAL(18,2) | | Current total investment value |
| risk_level | VARCHAR(30) | | Low, Medium, High |

---

## 9. market_data

| Column | Data Type | Key | Description |
|---|---|---|---|
| market_date | DATE | PK | Market observation date |
| asset_name | VARCHAR(150) | PK | Asset/security name |
| asset_type | VARCHAR(50) | | Equity, Bond, Index, ETF, etc. |
| open_price | DECIMAL(18,4) | | Opening price |
| high_price | DECIMAL(18,4) | | Daily high |
| low_price | DECIMAL(18,4) | | Daily low |
| close_price | DECIMAL(18,4) | | Closing price |
| volume | BIGINT | | Trading volume |

---

## 10. branches

| Column | Data Type | Key | Description |
|---|---|---|---|
| branch_id | INT | PK | Unique branch identifier |
| branch_name | VARCHAR(150) | | Branch name |
| city | VARCHAR(100) | | Branch city |
| state | VARCHAR(100) | | Branch state |
| region | VARCHAR(50) | | Bank region |
| branch_type | VARCHAR(50) | | Full Service, Retail, Corporate, etc. |
| opening_date | DATE | | Branch opening date |

---

## 11. employees

| Column | Data Type | Key | Description |
|---|---|---|---|
| employee_id | INT | PK | Unique employee identifier |
| branch_id | INT | FK | Employee's branch |
| employee_name | VARCHAR(150) | | Employee name |
| job_role | VARCHAR(100) | | Employee role |
| hire_date | DATE | | Employment start date |
| salary | DECIMAL(15,2) | | Annual salary |
| employment_status | VARCHAR(30) | | Active, Leave, Resigned |

---

## 12. digital_banking

| Column | Data Type | Key | Description |
|---|---|---|---|
| digital_activity_id | BIGINT | PK | Unique digital activity record |
| customer_id | BIGINT | FK | Customer performing activity |
| activity_date | TIMESTAMP | | Activity timestamp |
| channel | VARCHAR(50) | | Mobile, Web, Tablet |
| device_type | VARCHAR(50) | | Device category |
| login_count | INT | | Number of logins |
| transaction_count | INT | | Number of digital transactions |
| session_minutes | INT | | Total session duration |

---

## 13. atm_transactions

| Column | Data Type | Key | Description |
|---|---|---|---|
| atm_transaction_id | BIGINT | PK | Unique ATM transaction identifier |
| customer_id | BIGINT | FK | Customer using ATM |
| account_id | BIGINT | FK | Related account |
| transaction_date | TIMESTAMP | | ATM transaction timestamp |
| atm_location | VARCHAR(150) | | ATM location |
| transaction_type | VARCHAR(50) | | Withdrawal, Deposit, Balance Inquiry |
| amount | DECIMAL(18,2) | | Transaction amount |
| status | VARCHAR(30) | | Completed, Failed, Reversed |

---

## 14. fraud_alerts

| Column | Data Type | Key | Description |
|---|---|---|---|
| alert_id | BIGINT | PK | Unique fraud alert identifier |
| transaction_id | BIGINT | FK | Related transaction |
| customer_id | BIGINT | FK | Customer involved |
| alert_date | TIMESTAMP | | Alert creation timestamp |
| fraud_type | VARCHAR(100) | | Transaction fraud category |
| risk_level | VARCHAR(30) | | Low, Medium, High, Critical |
| fraud_status | VARCHAR(30) | | Open, Investigating, Confirmed, False Positive, Closed |
| fraud_amount | DECIMAL(18,2) | | Financial amount associated with alert |

---

## 15. complaints

| Column | Data Type | Key | Description |
|---|---|---|---|
| complaint_id | BIGINT | PK | Unique complaint identifier |
| customer_id | BIGINT | FK | Customer submitting complaint |
| branch_id | INT | FK | Related branch |
| complaint_date | DATE | | Complaint date |
| complaint_type | VARCHAR(100) | | Complaint category |
| channel | VARCHAR(50) | | Branch, Phone, Web, Mobile |
| priority | VARCHAR(30) | | Low, Medium, High, Critical |
| resolution_status | VARCHAR(30) | | Open, In Progress, Resolved |
| resolution_date | DATE | | Date complaint was resolved |