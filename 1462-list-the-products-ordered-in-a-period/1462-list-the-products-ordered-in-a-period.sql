# Write your MySQL query statement below
select p.product_name, 
    sum(o.unit) as unit
from Products p
join Orders o
on p.product_id=o.product_id
WHERE order_date >= '2020-02-01'
  AND order_date < '2020-03-01' 
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100;