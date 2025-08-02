-- Write your PostgreSQL query statement below
With cte as
(
    SELECT NUM, COUNT (NUM) AS CNT FROM MyNumbers
    Group by num
)
SELECT MAX(NUM) as num
FROM cte
WHERE CNT=1 