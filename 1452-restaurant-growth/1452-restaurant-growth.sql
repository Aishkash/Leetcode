WITH DailyRevenue AS (
    SELECT 
        visited_on,
        SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),
RollingWindow AS (
    SELECT 
        d1.visited_on,
        SUM(d2.amount) AS amount,
        ROUND(SUM(d2.amount) / 7.0, 2) AS average_amount
    FROM DailyRevenue d1
    JOIN DailyRevenue d2
      ON d2.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY) AND d1.visited_on
    GROUP BY d1.visited_on
)
SELECT 
    visited_on,
    amount,
    average_amount
FROM RollingWindow
WHERE visited_on >= (SELECT MIN(visited_on) FROM DailyRevenue) + INTERVAL 6 DAY
ORDER BY visited_on;