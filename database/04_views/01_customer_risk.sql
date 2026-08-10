-- ============================================================
-- CUSTOMER RISK PROFILE
-- ============================================================

CREATE OR REPLACE VIEW analytics.customer_risk_profile AS

WITH account_summary AS (

    SELECT
        customer_id,
        COUNT(*) AS account_count,
        SUM(balance) AS total_account_balance

    FROM core.accounts

    GROUP BY customer_id
),

loan_summary AS (

    SELECT
        customer_id,

        COUNT(*) AS loan_count,

        SUM(loan_amount) AS total_loan_amount,

        SUM(outstanding_amount)
            AS total_outstanding_amount,

        SUM(
            CASE
                WHEN default_flag = TRUE
                THEN 1
                ELSE 0
            END
        ) AS default_count,

        SUM(
            CASE
                WHEN default_flag = TRUE
                THEN outstanding_amount
                ELSE 0
            END
        ) AS default_exposure,

        AVG(credit_score)
            AS average_credit_score,

        AVG(interest_rate)
            AS average_loan_interest_rate

    FROM core.loans

    GROUP BY customer_id
),

credit_card_summary AS (

    SELECT
        customer_id,

        COUNT(*) AS credit_card_count,

        SUM(credit_limit)
            AS total_credit_limit,

        SUM(current_balance)
            AS total_credit_card_balance

    FROM core.credit_cards

    GROUP BY customer_id
),

investment_summary AS (

    SELECT
        customer_id,

        COUNT(*) AS investment_count,

        SUM(current_value)
            AS total_investment_value

    FROM core.investments

    GROUP BY customer_id
),

fraud_summary AS (

    SELECT
        customer_id,

        COUNT(*) AS fraud_alert_count,

        SUM(fraud_amount)
            AS total_fraud_amount

    FROM core.fraud_alerts

    GROUP BY customer_id
),

complaint_summary AS (

    SELECT
        customer_id,

        COUNT(*) AS complaint_count,

        SUM(
            CASE
                WHEN resolution_status <> 'Resolved'
                THEN 1
                ELSE 0
            END
        ) AS unresolved_complaint_count

    FROM core.complaints

    GROUP BY customer_id
)

SELECT

    c.customer_id,

    c.first_name,

    c.last_name,

    c.gender,

    c.annual_income,

    c.occupation,

    c.city,

    c.state,

    c.customer_since,

    c.customer_status,

    COALESCE(
        a.account_count,
        0
    ) AS account_count,

    COALESCE(
        a.total_account_balance,
        0
    ) AS total_account_balance,

    COALESCE(
        l.loan_count,
        0
    ) AS loan_count,

    COALESCE(
        l.total_loan_amount,
        0
    ) AS total_loan_amount,

    COALESCE(
        l.total_outstanding_amount,
        0
    ) AS total_outstanding_amount,

    COALESCE(
        l.default_count,
        0
    ) AS default_count,

    COALESCE(
        l.default_exposure,
        0
    ) AS default_exposure,

    COALESCE(
        l.average_credit_score,
        0
    ) AS average_credit_score,

    COALESCE(
        l.average_loan_interest_rate,
        0
    ) AS average_loan_interest_rate,

    COALESCE(
        cc.credit_card_count,
        0
    ) AS credit_card_count,

    COALESCE(
        cc.total_credit_limit,
        0
    ) AS total_credit_limit,

    COALESCE(
        cc.total_credit_card_balance,
        0
    ) AS total_credit_card_balance,

    CASE
        WHEN COALESCE(
            cc.total_credit_limit,
            0
        ) > 0

        THEN
            COALESCE(
                cc.total_credit_card_balance,
                0
            )
            /
            cc.total_credit_limit

        ELSE 0

    END AS credit_utilization,

    COALESCE(
        i.investment_count,
        0
    ) AS investment_count,

    COALESCE(
        i.total_investment_value,
        0
    ) AS total_investment_value,

    COALESCE(
        f.fraud_alert_count,
        0
    ) AS fraud_alert_count,

    COALESCE(
        f.total_fraud_amount,
        0
    ) AS total_fraud_amount,

    COALESCE(
        cp.complaint_count,
        0
    ) AS complaint_count,

    COALESCE(
        cp.unresolved_complaint_count,
        0
    ) AS unresolved_complaint_count

FROM core.customers c

LEFT JOIN account_summary a
    ON c.customer_id = a.customer_id

LEFT JOIN loan_summary l
    ON c.customer_id = l.customer_id

LEFT JOIN credit_card_summary cc
    ON c.customer_id = cc.customer_id

LEFT JOIN investment_summary i
    ON c.customer_id = i.customer_id

LEFT JOIN fraud_summary f
    ON c.customer_id = f.customer_id

LEFT JOIN complaint_summary cp
    ON c.customer_id = cp.customer_id;