#1
SELECT CONCAT(DATE(NOW())," ",TIME(NOW())) AS 系统时间;

SELECT NOW();

#2.
SELECT `employee_id`,`last_name`,`salary`,
salary*1.2 AS new_salary 
FROM employees;

#3.
SELECT LENGTH(last_name) AS 长度,SUBSTR(last_name,1,1) AS 首字符,last_name
FROM employees
ORDER BY 首字符;



#4.
SELECT CONCAT(last_name," earns ",salary," monthly but wants ",3*salary)
AS "Dream Salary"
FROM employees;



# 5.
SELECT last_name,job_id AS job,
CASE job_id 
WHEN "AD_PRES" THEN "A"
WHEN "ST_MAN"	THEN "B"
WHEN "IT_PROG" THEN "C"
WHEN "SA_REP" THEN "D"
WHEN "ST_CLERK" THEN "E"
END AS Gtade 
FROM employees
WHERE job_id="AD_PRES";
