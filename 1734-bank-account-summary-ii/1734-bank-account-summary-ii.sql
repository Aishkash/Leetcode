# Write your MySQL query statement below
select u.name, sum(t.amount) as balance
from Users u
join Transactions t
on u.account=t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;#u cant do that above 