-- Select non-null names from second_table ordered by score DESC
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
