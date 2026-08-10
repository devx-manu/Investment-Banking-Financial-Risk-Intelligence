-- ============================================================
-- LOAN & NPA RISK ANALYSIS
-- ============================================================

CREATE OR REPLACE VIEW analytics.loan_risk_analysis AS

SELECT
    l.loan_id,
    l.customer_id,
    l.branch_id,
    l.loan_type,
    l.application_date,
    l.approval_date,
    l.loan_amount,
    l.interest_rate,
    l.tenure_months,
    l.credit_score,
    l.loan_status,
    l.default_flag,
    l.outstanding_amount,

    -- Approval turnaround
    (
        l.approval_date - l.application_date
    ) AS approval_days,

    -- Risk category
    CASE
        WHEN l.credit_score < 580
            THEN 'Very High Risk'

        WHEN l.credit_score < 650
            THEN 'High Risk'

        WHEN l.credit_score < 700
            THEN 'Medium Risk'

        WHEN l.credit_score < 750
            THEN 'Low Risk'

        ELSE 'Very Low Risk'
    END AS credit_risk_category,

    -- NPA classification
    CASE
        WHEN l.default_flag = TRUE
            THEN 'NPA'

        ELSE 'Standard'
    END AS npa_status,

    -- Outstanding percentage
    CASE
        WHEN l.loan_amount > 0
        THEN
            l.outstanding_amount
            / l.loan_amount

        ELSE 0
    END AS outstanding_ratio

FROM core.loans l;