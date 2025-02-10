SELECT NAME,boyName FROM boys,beauty
WHERE beauty.boyfriend_id=boys.id;

SELECT *FROM beauty;
SELECT *FROM boys;

SELECT b.name,bo.*
FROM beauty AS b 
LEFT OUTER JOIN  boys AS bo
ON b.`boyfriend_id`= bo.`id`
WHERE bo.`id` IS NULL;`boys``boys`
 