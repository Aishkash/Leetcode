# Write your MySQL query statement below
select person_name
from (
    select
        person_name,
        sum(weight) over(order by turn) as tot
        from Queue
) q
where tot<=1000
order by tot desc
limit 1