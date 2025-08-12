-- select a1.player_id, b1.event_date as first_login
-- from Activity a1
-- join Activity b1
-- on a1.player_id=b1.event_date
-- and a1.player_id>b1.player_id;


-- SELECT player_id, MIN(event_date) AS first_login
-- FROM Activity
-- GROUP BY player_id;

SELECT a.player_id, a.event_date AS first_login
FROM Activity a
JOIN (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) b
ON a.player_id = b.player_id
AND a.event_date = b.first_login;