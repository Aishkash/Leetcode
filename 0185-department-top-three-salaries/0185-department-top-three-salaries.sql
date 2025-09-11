# Write your MySQL query statement below
select d.name as Department, 
       e.name as Employee,
       e.salary as Salary
FROM (
    SELECT e.*,
           DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee e
) e
JOIN Department d
  ON e.departmentId = d.id
WHERE e.salary_rank <= 3
ORDER BY d.name, e.salary DESC;