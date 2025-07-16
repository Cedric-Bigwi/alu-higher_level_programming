-- Group second_table records by score and count each group
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
