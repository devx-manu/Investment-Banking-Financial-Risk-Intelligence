-- ============================================================
-- FRAUD ANALYSIS
-- ============================================================

CREATE OR REPLACE VIEW analytics.fraud_analysis AS

SELECT
    f.alert_id,
    f.transaction_id,
    f.customer_id,
    f.alert_date,
    f.fraud_type,
    f.risk_level,
    f.fraud_status,
    f.fraud_amount,

    t.account_id,
    t.transaction_date,
    t.transaction_type,
    t.amount AS transaction_amount,

    c.first_name,
    c.last_name,
    c.annual_income,
    c.city,
    c.state

FROM core.fraud_alerts f

LEFT JOIN core.transactions t
    ON f.transaction_id = t.transaction_id

LEFT JOIN core.customers c
    ON f.customer_id = c.customer_id;