# Write your MySQL query statement below
select u.user_id AS buyer_id,
        u.join_date,
        COUNT(o.order_id) AS orders_in_2019

from Users u
left join Orders o
on u.user_id=o.buyer_id
AND YEAR(o.order_date) = 2019
group by u.user_id, u.join_date;
