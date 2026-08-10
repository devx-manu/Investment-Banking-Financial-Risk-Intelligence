-- ============================================================
-- CORE BANKING DATABASE
-- ============================================================


-- ============================================================
-- BRANCHES
-- ============================================================

CREATE TABLE IF NOT EXISTS core.branches (
    branch_id       INTEGER PRIMARY KEY,
    branch_name     VARCHAR(150) NOT NULL,
    city            VARCHAR(100) NOT NULL,
    state           VARCHAR(100) NOT NULL,
    region          VARCHAR(50) NOT NULL,
    branch_type     VARCHAR(50) NOT NULL,
    opening_date    DATE NOT NULL
);


-- ============================================================
-- EMPLOYEES
-- ============================================================

CREATE TABLE IF NOT EXISTS core.employees (
    employee_id         INTEGER PRIMARY KEY,
    branch_id           INTEGER NOT NULL,
    employee_name       VARCHAR(150) NOT NULL,
    job_role            VARCHAR(100) NOT NULL,
    hire_date           DATE NOT NULL,
    salary              NUMERIC(15,2) NOT NULL,
    employment_status   VARCHAR(30) NOT NULL,

    CONSTRAINT fk_employee_branch
        FOREIGN KEY (branch_id)
        REFERENCES core.branches(branch_id)
);


-- ============================================================
-- CUSTOMERS
-- ============================================================

CREATE TABLE IF NOT EXISTS core.customers (
    customer_id       INTEGER PRIMARY KEY,
    first_name        VARCHAR(100) NOT NULL,
    last_name         VARCHAR(100) NOT NULL,
    date_of_birth     DATE NOT NULL,
    gender            VARCHAR(20) NOT NULL,
    annual_income     NUMERIC(18,2) NOT NULL,
    occupation        VARCHAR(100) NOT NULL,
    city              VARCHAR(100) NOT NULL,
    state             VARCHAR(100) NOT NULL,
    customer_since    DATE NOT NULL,
    customer_status   VARCHAR(30) NOT NULL
);


-- ============================================================
-- ACCOUNTS
-- ============================================================

CREATE TABLE IF NOT EXISTS core.accounts (
    account_id       INTEGER PRIMARY KEY,
    customer_id      INTEGER NOT NULL,
    branch_id        INTEGER NOT NULL,
    account_type     VARCHAR(50) NOT NULL,
    open_date        DATE NOT NULL,
    balance          NUMERIC(18,2) NOT NULL,
    currency         CHAR(3) NOT NULL,
    account_status   VARCHAR(30) NOT NULL,

    CONSTRAINT fk_account_customer
        FOREIGN KEY (customer_id)
        REFERENCES core.customers(customer_id),

    CONSTRAINT fk_account_branch
        FOREIGN KEY (branch_id)
        REFERENCES core.branches(branch_id)
);


-- ============================================================
-- TRANSACTIONS
-- ============================================================

CREATE TABLE IF NOT EXISTS core.transactions (
    transaction_id        BIGINT PRIMARY KEY,
    account_id            INTEGER NOT NULL,
    customer_id           INTEGER NOT NULL,
    transaction_date      TIMESTAMP NOT NULL,
    transaction_type      VARCHAR(30) NOT NULL,
    transaction_category  VARCHAR(50) NOT NULL,
    amount                NUMERIC(18,2) NOT NULL,
    merchant              VARCHAR(150),
    channel               VARCHAR(30) NOT NULL,
    location              VARCHAR(100),
    status                VARCHAR(30) NOT NULL,

    CONSTRAINT fk_transaction_account
        FOREIGN KEY (account_id)
        REFERENCES core.accounts(account_id),

    CONSTRAINT fk_transaction_customer
        FOREIGN KEY (customer_id)
        REFERENCES core.customers(customer_id)
);


-- ============================================================
-- LOANS
-- ============================================================

CREATE TABLE IF NOT EXISTS core.loans (
    loan_id             INTEGER PRIMARY KEY,
    customer_id         INTEGER NOT NULL,
    branch_id           INTEGER NOT NULL,
    loan_type           VARCHAR(50) NOT NULL,
    application_date    DATE NOT NULL,
    approval_date       DATE NOT NULL,
    loan_amount         NUMERIC(18,2) NOT NULL,
    interest_rate       NUMERIC(8,3) NOT NULL,
    tenure_months      INTEGER NOT NULL,
    credit_score        INTEGER NOT NULL,
    loan_status         VARCHAR(30) NOT NULL,
    default_flag        BOOLEAN NOT NULL,
    outstanding_amount  NUMERIC(18,2) NOT NULL,

    CONSTRAINT fk_loan_customer
        FOREIGN KEY (customer_id)
        REFERENCES core.customers(customer_id),

    CONSTRAINT fk_loan_branch
        FOREIGN KEY (branch_id)
        REFERENCES core.branches(branch_id),

    CONSTRAINT chk_credit_score
        CHECK (credit_score BETWEEN 300 AND 850),

    CONSTRAINT chk_loan_amount
        CHECK (loan_amount > 0)
);


-- ============================================================
-- LOAN PAYMENTS
-- ============================================================

CREATE TABLE IF NOT EXISTS core.loan_payments (
    payment_id       BIGINT PRIMARY KEY,
    loan_id          INTEGER NOT NULL,
    payment_date     DATE NOT NULL,
    due_amount       NUMERIC(18,2) NOT NULL,
    paid_amount      NUMERIC(18,2) NOT NULL,
    days_late        INTEGER NOT NULL,
    payment_status   VARCHAR(30) NOT NULL,

    CONSTRAINT fk_payment_loan
        FOREIGN KEY (loan_id)
        REFERENCES core.loans(loan_id)
);


-- ============================================================
-- CREDIT CARDS
-- ============================================================

CREATE TABLE IF NOT EXISTS core.credit_cards (
    credit_card_id   INTEGER PRIMARY KEY,
    customer_id      INTEGER NOT NULL,
    issue_date       DATE NOT NULL,
    credit_limit     NUMERIC(18,2) NOT NULL,
    current_balance  NUMERIC(18,2) NOT NULL,
    interest_rate    NUMERIC(8,3) NOT NULL,
    card_status      VARCHAR(30) NOT NULL,

    CONSTRAINT fk_card_customer
        FOREIGN KEY (customer_id)
        REFERENCES core.customers(customer_id),

    CONSTRAINT chk_card_limit
        CHECK (credit_limit > 0),

    CONSTRAINT chk_card_balance
        CHECK (current_balance >= 0),

    CONSTRAINT chk_card_utilization
        CHECK (current_balance <= credit_limit)
);


-- ============================================================
-- MORTGAGES
-- ============================================================

CREATE TABLE IF NOT EXISTS core.mortgages (
    mortgage_id          INTEGER PRIMARY KEY,
    customer_id          INTEGER NOT NULL,
    branch_id            INTEGER NOT NULL,
    property_value       NUMERIC(18,2) NOT NULL,
    loan_amount          NUMERIC(18,2) NOT NULL,
    interest_rate        NUMERIC(8,3) NOT NULL,
    term_years           INTEGER NOT NULL,
    start_date           DATE NOT NULL,
    outstanding_balance  NUMERIC(18,2) NOT NULL,
    mortgage_status      VARCHAR(30) NOT NULL,

    CONSTRAINT fk_mortgage_customer
        FOREIGN KEY (customer_id)
        REFERENCES core.customers(customer_id),

    CONSTRAINT fk_mortgage_branch
        FOREIGN KEY (branch_id)
        REFERENCES core.branches(branch_id)
);


-- ============================================================
-- INVESTMENTS
-- ============================================================

CREATE TABLE IF NOT EXISTS core.investments (
    investment_id    INTEGER PRIMARY KEY,
    customer_id      INTEGER NOT NULL,
    investment_type  VARCHAR(50) NOT NULL,
    asset_name       VARCHAR(150) NOT NULL,
    investment_date  DATE NOT NULL,
    quantity         NUMERIC(18,6) NOT NULL,
    purchase_price   NUMERIC(18,2) NOT NULL,
    current_value    NUMERIC(18,2) NOT NULL,
    risk_level       VARCHAR(30) NOT NULL,

    CONSTRAINT fk_investment_customer
        FOREIGN KEY (customer_id)
        REFERENCES core.customers(customer_id)
);


-- ============================================================
-- MARKET DATA
-- ============================================================

CREATE TABLE IF NOT EXISTS core.market_data (
    market_date   DATE NOT NULL,
    asset_name    VARCHAR(100) NOT NULL,
    asset_type    VARCHAR(50) NOT NULL,
    open_price    NUMERIC(18,4) NOT NULL,
    high_price    NUMERIC(18,4) NOT NULL,
    low_price     NUMERIC(18,4) NOT NULL,
    close_price   NUMERIC(18,4) NOT NULL,
    volume        BIGINT NOT NULL,

    PRIMARY KEY (market_date, asset_name)
);


-- ============================================================
-- DIGITAL BANKING
-- ============================================================

CREATE TABLE IF NOT EXISTS core.digital_banking (
    digital_activity_id  BIGINT PRIMARY KEY,
    customer_id          INTEGER NOT NULL,
    activity_date        TIMESTAMP NOT NULL,
    channel              VARCHAR(30) NOT NULL,
    device_type          VARCHAR(30) NOT NULL,
    login_count          INTEGER NOT NULL,
    transaction_count    INTEGER NOT NULL,
    session_minutes      INTEGER NOT NULL,

    CONSTRAINT fk_digital_customer
        FOREIGN KEY (customer_id)
        REFERENCES core.customers(customer_id)
);


-- ============================================================
-- ATM TRANSACTIONS
-- ============================================================

CREATE TABLE IF NOT EXISTS core.atm_transactions (
    atm_transaction_id  BIGINT PRIMARY KEY,
    customer_id         INTEGER NOT NULL,
    account_id          INTEGER NOT NULL,
    transaction_date    TIMESTAMP NOT NULL,
    atm_location        VARCHAR(100) NOT NULL,
    transaction_type    VARCHAR(50) NOT NULL,
    amount              NUMERIC(18,2) NOT NULL,
    status              VARCHAR(30) NOT NULL,

    CONSTRAINT fk_atm_customer
        FOREIGN KEY (customer_id)
        REFERENCES core.customers(customer_id),

    CONSTRAINT fk_atm_account
        FOREIGN KEY (account_id)
        REFERENCES core.accounts(account_id)
);


-- ============================================================
-- FRAUD ALERTS
-- ============================================================

CREATE TABLE IF NOT EXISTS core.fraud_alerts (
    alert_id        INTEGER PRIMARY KEY,
    transaction_id  BIGINT NOT NULL,
    customer_id     INTEGER NOT NULL,
    alert_date      TIMESTAMP NOT NULL,
    fraud_type      VARCHAR(100) NOT NULL,
    risk_level      VARCHAR(30) NOT NULL,
    fraud_status    VARCHAR(50) NOT NULL,
    fraud_amount    NUMERIC(18,2) NOT NULL,

    CONSTRAINT fk_fraud_transaction
        FOREIGN KEY (transaction_id)
        REFERENCES core.transactions(transaction_id),

    CONSTRAINT fk_fraud_customer
        FOREIGN KEY (customer_id)
        REFERENCES core.customers(customer_id)
);


-- ============================================================
-- COMPLAINTS
-- ============================================================

CREATE TABLE IF NOT EXISTS core.complaints (
    complaint_id       INTEGER PRIMARY KEY,
    customer_id        INTEGER NOT NULL,
    branch_id          INTEGER NOT NULL,
    complaint_date     TIMESTAMP NOT NULL,
    complaint_type     VARCHAR(100) NOT NULL,
    channel            VARCHAR(30) NOT NULL,
    priority           VARCHAR(30) NOT NULL,
    resolution_status  VARCHAR(30) NOT NULL,
    resolution_date    TIMESTAMP,

    CONSTRAINT fk_complaint_customer
        FOREIGN KEY (customer_id)
        REFERENCES core.customers(customer_id),

    CONSTRAINT fk_complaint_branch
        FOREIGN KEY (branch_id)
        REFERENCES core.branches(branch_id)
);