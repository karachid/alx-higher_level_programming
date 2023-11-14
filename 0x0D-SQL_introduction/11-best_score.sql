-- Lists all records in the table second_table with a score >= 10
-- Records are ordered in descending score order
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
