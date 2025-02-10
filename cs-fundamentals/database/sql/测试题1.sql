
# 1.可以
SELECT last_name ,job_id,salary AS sal FROM employees;

# 2.可以

# 中文字符错误

#4
DESC departments;
SELECT * FROM departments;
#5
SELECT DISTINCT job_id FROM employees;


#6  

#ifnull 函数
SELECT 
	IFNULL(commission_pct,0) AS 奖金率,
	commission_pct
FROM
	employees;
	
SELECT 
CONCAT (`first_name`,',',`last_name`,',',IFNULL(commission_pct,0)) AS "OUT_PUT" 
FROM employees;

#concat_ws()函数 :可以指定分隔符。

SELECT 
CONCAT_WS(',',`first_name`,`last_name`,`email`,
`phone_number`,`job_id`,`salary`,IFNULL(`commission_pct`,0),
`manager_id`,`department_id`,`hiredate`)
FROM `employees`;