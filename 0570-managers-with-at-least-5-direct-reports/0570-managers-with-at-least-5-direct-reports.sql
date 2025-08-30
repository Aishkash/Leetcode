# Write your MySQL query statement below
select e.name
from Employee e
join Employee s
on e.id=s.managerId
group by s.managerId
having count(s.managerId)>=5;