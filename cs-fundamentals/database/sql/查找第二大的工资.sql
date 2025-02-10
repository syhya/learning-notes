
SELECT MAX(Salary)
FROM Employees;

# 查出第二高的薪资 
#方法一

SELECT MAX(Salary)AS 第二大的工资
FROM employees
WHERE Salary<(SELECT MAX(Salary) FROM employees);


#方法二
SELECT 
(SELECT  Salary 
FROM employees 
WHERE Salary NOT IN (SELECT MAX(Salary) FROM employees)
ORDER BY Salary DESC
LIMIT 1) AS 第二大的工资;     





