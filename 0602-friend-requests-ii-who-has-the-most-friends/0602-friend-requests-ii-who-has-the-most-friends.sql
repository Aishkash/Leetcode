WITH AllFriends AS (
    SELECT requester_id AS id, accepter_id AS friend
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id, requester_id AS friend
    FROM RequestAccepted
),
FriendCount AS (
    SELECT id, COUNT(DISTINCT friend) AS num
    FROM AllFriends
    GROUP BY id
)
SELECT id, num
FROM FriendCount
WHERE num = (SELECT MAX(num) FROM FriendCount);