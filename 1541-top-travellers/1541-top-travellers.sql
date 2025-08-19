# Write your MySQL query statement below
select u.name, 
    COALESCE(SUM(r.distance), 0) as travelled_distance
from Users u 
left join Rides r
on u.id=r.user_id
group by u.id, u.name
order by travelled_distance DESC, u.name ASC;


-- COALESCE(..., 0): replaces NULL with 0 for users without rides.