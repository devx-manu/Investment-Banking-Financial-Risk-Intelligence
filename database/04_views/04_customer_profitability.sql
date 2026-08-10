-- ============================================================
-- CUSTOMER PROFITABILITY
-- ============================================================

CREATE OR REPLACE VIEW analytics.customer_profitability AS

WITH transaction_summary AS (

    SELECT
        customer_id,

        SUM(
            CASE
                WHEN transaction_type IN ('Deposit', 'Credit')
                THEN amount
                ELSE 0
            END
        ) AS total_deposits,

        SUM(
            CASE
                WHEN transaction_type IN ('Withdrawal', 'Debit')
                THEN amount
                ELSE 0
            END
        ) AS total_withdrawals,

        COUNT(*) AS transaction_count

    FROM core.transactions

    GROUP BY customer_id
),

loan_summary AS (

    SELECT
        customer_id,

        SUM(loan_amount) AS total_loan_amount,

        SUM(outstanding_amount) AS total_outstanding_amount,

        SUM(
            outstanding_amount * interest_rate / 100
        ) AS estimated_interest_income

    FROM core.loans

    GROUP BY customer_id
),

investment_summary AS (

    SELECT
        customer_id,

        SUM(current_value) AS investment_value

    FROM core.investments

    GROUP BY customer_id
)

SELECT

    c.customer_id,

    c.first_name,

    c.last_name,

    c.annual_income,

    c.customer_status,

    COALESCE(
        t.total_deposits,
        0
    ) AS total_deposits,

    COALESCE(
        t.total_withdrawals,
        0
    ) AS total_withdrawals,

    COALESCE(
        t.transaction_count,
        0
    ) AS transaction_count,

    COALESCE(
        l.total_loan_amount,
        0
    ) AS total_loan_amount,

    COALESCE(
        l.total_outstanding_amount,
        0
    ) AS total_outstanding_amount,

    COALESCE(
        l.estimated_interest_income,
        0
    ) AS estimated_interest_income,

    COALESCE(
        i.investment_value,
        0
    ) AS investment_value,

    (
        COALESCE(
            l.estimated_interest_income,
            0
        )
        +
        COALESCE(
            t.total_deposits,
            0
        ) * 0.002
    ) AS estimated_customer_revenue

FROM core.customers c

LEFT JOIN transaction_summary t
    ON c.customer_id = t.customer_id

LEFT JOIN loan_summary l
    ON c.customer_id = l.customer_id

LEFT JOIN investment_summary i
    ON c.customer_id = i.customer_id;