SELECT employee_id
FROM (
    -- 1. Get employees with a name but NO salary (LEFT JOIN's unmatched part)
    SELECT 
        e.employee_id
    FROM Employees e
    LEFT JOIN Salaries s
    ON e.employee_id = s.employee_id
    WHERE s.salary IS NULL
    
    UNION 
    
    -- 2. Get employees with a salary but NO name (RIGHT JOIN's unmatched part)
    SELECT 
        s.employee_id
    FROM Employees e
    RIGHT JOIN Salaries s
    ON e.employee_id = s.employee_id
    WHERE e.name IS NULL
) AS t
ORDER BY employee_id;