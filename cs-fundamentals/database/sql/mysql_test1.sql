USE myemployees;

SELECT * FROM employees;

SELECT * FROM employees WHERE department_id=90;

SELECT  last_name, salary FROM employees WHERE salary<=3000;

SELECT  last_name, salary FROM employees WHERE salary
BETWEEN 2000 AND 3000;

SELECT employee_id,last_name,salary,manager_id FROM employees
WHERE manager_id IN (100,101,201);

SELECT employee_id,last_name,salary,manager_id,job_id
FROM employees
WHERE salary>=10000 
AND job_id LIKE "%MAN";

SELECT employee_id,last_name,salary,manager_id
FROM employees
ORDER BY salary DESC;

SELECT last_name,department_id,salary
FROM employees
ORDER BY department_id DESC, salary DESC;

SELECT AVG(salary),MAX(salary),MIN(salary),SUM(salary)
FROM employees
WHERE job_id LIKE "%REP%";

SELECT COUNT(*) 
FROM employees
WHERE department_id=50;

SELECT department_id,MAX(salary)
FROM employees
GROUP BY department_id
HAVING MAX(salary)>10000;

`girls`

SELECT last_name, job_id,salary,
   CASE job_id WHEN "IT_PROG"THEN 1.1*salary
	WHEN "SA_REP" THEN 1.2*salary
	ELSE salary END "REVISED_SALARY"
	FROM employees;
`girls`
SELECT last_name FROM employees WHERE salary>
(SELECT salary FROM employees WHERE last_name ="Abel");

SELECT last_name,department_name
FROM employees AS e,departments AS d
WHERE e.`department_id`=d.`department_id`;

SELECT last_name,department_name
FROM employees AS e
INNER JOIN departments AS d
ON e.`department_id`=d.`department_id`;



