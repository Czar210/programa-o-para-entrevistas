
SELECT
    a.iban AS IBAN,
    ROUND(MIN(t.amount),2) AS min_transaction,
    ROUND(MAX(t.amount),2) AS max_transaction,
    ROUND(AVG(t.amount),2) AS avg_transaction,
    COUNT(t.amount) AS total_transaction
FROM accounts a
JOIN transactions t ON a.id = t.account_id
WHERE MONTH(t.dt) = 9
GROUP BY a.iban
ORDER BY a.iban ASC;
