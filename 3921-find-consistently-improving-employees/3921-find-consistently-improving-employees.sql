WITH ranked_reviews AS (
    SELECT
        pr.employee_id,
        pr.review_date,
        pr.rating,
        ROW_NUMBER() OVER (
            PARTITION BY pr.employee_id
            ORDER BY pr.review_date DESC
        ) AS rn
    FROM performance_reviews pr
),
last_three AS (
    SELECT
        employee_id,
        rating,
        rn
    FROM ranked_reviews
    WHERE rn <= 3
),
pivoted AS (
    SELECT
        employee_id,
        MAX(CASE WHEN rn = 3 THEN rating END) AS first_rating,
        MAX(CASE WHEN rn = 2 THEN rating END) AS middle_rating,
        MAX(CASE WHEN rn = 1 THEN rating END) AS last_rating
    FROM last_three
    GROUP BY employee_id
    HAVING COUNT(*) = 3
       AND MAX(CASE WHEN rn = 3 THEN rating END) < MAX(CASE WHEN rn = 2 THEN rating END)
       AND MAX(CASE WHEN rn = 2 THEN rating END) < MAX(CASE WHEN rn = 1 THEN rating END)
)
SELECT
    e.employee_id,
    e.name,
    (p.last_rating - p.first_rating) AS improvement_score
FROM pivoted p
JOIN employees e ON e.employee_id = p.employee_id
ORDER BY improvement_score DESC, e.name ASC;