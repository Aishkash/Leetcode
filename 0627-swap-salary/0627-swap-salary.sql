-- UPDATE Salary
-- SET sex = IF(sex = 'm', 'f', 'm');

UPDATE Salary
SET sex = CASE
             WHEN sex = 'm' THEN 'f'
             ELSE 'm'
          END;