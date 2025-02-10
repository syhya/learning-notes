
#测 试
#sql99
#一、查询编号>3的女神的男朋友信息，如果有则列出详细，如果没有，用NULL填充
SELECT g.`name`,b.*
FROM beauty g 
LEFT JOIN boys b
ON g.`boyfriend_id`=b.`id`
WHERE g.`id`>3;



#二、查询哪个城市没有部门
SELECT city
FROM locations l
LEFT JOIN departments d
ON l.`location_id`=d.`location_id`
WHERE department_id IS NULL;


#三、查询部门名为SAL或IT的员工信息
SELECT  e.*
FROM departments d
LEFT JOIN employees e
ON  e.`department_id`=d.`department_id`
WHERE d.`department_name`="SAL" OR d.`department_name`="IT";





#sql92
#1. 显示所有员工的姓名，部门号和部门名称。
SELECT last_name,d.department_id,department_name 
FROM employees AS e,departments AS d
WHERE e.`department_id`=d.`department_id`;

# 2. 查询90号部门员工的job_id和90号部门的location_id
SELECT e.job_id,d.location_id
FROM `employees` AS e,`departments` AS d
WHERE e.`department_id`=d.`department_id` AND d.`department_id`=90;



#3. 选择所有有奖金的员工的
#last_name , department_name , location_id , city
SELECT last_name , department_name , l.location_id , l.city
FROM `employees` e,`departments` d,`locations` l
WHERE e.`department_id`=d.`department_id` AND d.`location_id`=l.`location_id`
AND e.`commission_pct` IS NOT NULL;

#4. 选择city在Toronto工作的员工的
#last_name , job_id , department_id , department_name
SELECT last_name , job_id , d.department_id , department_name
FROM `employees` e,`departments` d,`locations` l
WHERE  e.`department_id`=d.`department_id` AND d.`location_id`=l.`location_id` 
AND l.`city`="Toronto";


#5.查询每个工种、每个部门的部门名、工种名和最低工资
SELECT department_name,job_title,min_salary
FROM `jobs` j,`departments` d,`employees` e
WHERE j.job_id =e.`job_id` AND d.`department_id`=e.`department_id`
GROUP BY `job_title`,`department_name`;



#6.查询每个国家下的部门个数大于2的国家编号
SELECT country_id 
FROM locations l ,departments d
WHERE l.location_id = d.location_id
GROUP BY country_id
HAVING COUNT(*)>2;

#7、选择指定员工的姓名，员工号，以及他的管理者的姓名和员工号，结果类似于下面的格式
SELECT e.last_name ,e.employee_id,m.last_name,m.`employee_id`
FROM employees e,employees m
WHERE e.manager_id = m.employee_id ;