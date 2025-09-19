SELECT 
    user_id,
    ROUND(AVG(CASE WHEN activity_type = 'free_trial' THEN activity_duration END), 2) AS trial_avg_duration,
    ROUND(AVG(CASE WHEN activity_type = 'paid' THEN activity_duration END), 2) AS paid_avg_duration
FROM UserActivity
WHERE activity_type IN ('free_trial', 'paid')
GROUP BY user_id
HAVING 
    SUM(CASE WHEN activity_type = 'free_trial' THEN 1 ELSE 0 END) > 0
    AND SUM(CASE WHEN activity_type = 'paid' THEN 1 ELSE 0 END) > 0
ORDER BY user_id;