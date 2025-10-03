-- select a1.player_id, b1.event_date as first_login
-- from Activity a1
-- join Activity b1
-- on a1.player_id=b1.event_date
-- and a1.player_id>b1.player_id;


SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;

-- SELECT player_id, event_date AS first_login
-- FROM (
--     SELECT player_id, event_date,
--            ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rn
--     FROM Activity
-- ) t
-- WHERE rn = 1;