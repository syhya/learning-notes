# 连接查询

/*
笛卡尔乘积：表1:m行，表2：n行, m*n。


按功能分类:
	内连接:
		等值连接
		非等值连接
		自连接
	外连接:
		左外连接
		右外连接
		全外连接
	交叉连接
*/

/* 等值连接
n表连接，至少需要n-1个连接条件。
多变的顺序没有要求。
多表等值连接的结果为多表的交集部分。
*/

SELECT G.name,B.boyName
FROM beauty AS G,boys AS B
WHERE G.`id`=B.`id`;



# 查询有奖金的每个部门的部门名和部门的领导编号和该部门的最低工资
SELECT d.`department_name`,d.manager_id,MIN(salary)
FROM `departments` AS d,`employees` AS e
WHERE d.`department_id`= e.`department_id` AND e.`commission_pct` IS NOT NULL
GROUP BY d.`department_name`;

#非等值链接

#案例：查询员工的工资和工资级别
SELECT salary,grade_level 
FROM employees e,job_grades j
WHERE salary BETWEEN j.`lowest_sal` AND j.`highest_sal`;

#自连接

#查询员工名和上级的名称


SELECT e.`employee_id`,e.`last_name`, m.employee_id,m.last_name
FROM employees e,employees m
WHERE e.manager_id = m.employee_id;


/*
sql 99语法

  select 查询列表
  from 表1 别名 【连接类型】
  join 表2  别名
  on  连接条件
  【where 筛选条件】
  【group by 分组】
  【having 筛选条件】
  【order by 排序条件】
  
内连接:inner 
左连接：left
右连接：right
全连接:full

交叉连接：cross

*/


# 1.等值连接

#查询员工名、部门名

SELECT `last_name`,`department_name`
FROM employees AS e
INNER JOIN departments AS d
ON e.`department_id`=d.`department_id`;


#查询名字中包含e的员工名和工种名（添加筛选）
SELECT  `last_name`,`job_title`
FROM `employees` AS e 
INNER JOIN `jobs` AS j
ON e.`job_id`=j.`job_id`
WHERE last_name LIKE "%e%";


#查询部门个数>3的城市名和部门个数 （添加分组+筛选）
SELECT city,COUNT(*)
FROM locations l 
INNER JOIN departments d
ON  l.`location_id`=d.`location_id`
GROUP BY city
HAVING COUNT(*)>3;

#查询哪个部门的员工个数>3的部门名和员工个数，并按个数降序（添加排序）
SELECT COUNT(*) 个数,department_name
FROM employees e 
INNER JOIN departments d
ON e.`department_id`=d.`department_id`
GROUP BY department_name
HAVING COUNT(*)>3
ORDER BY COUNT(*) DESC;


#查询员工名、部门名、工种名，并按部门名降序(三表连接)
SELECT last_name,department_name,job_title
FROM employees e
INNER JOIN  departments d  ON e.`department_id`=d.`department_id`
INNER JOIN jobs j ON j.`job_id`=e.`job_id`
ORDER BY department_name DESC; 


#2.非等值连接

#查询员工的工资级别

SELECT salary,`grade_level` 
FROM employees e
INNER JOIN job_grades j
ON e.`salary` BETWEEN j.`lowest_sal` AND j.`highest_sal`;


#自连接
#查询员工的名字和他上级的名字
SELECT e.last_name,m.last_name
FROM employees e
INNER JOIN employees m
ON e.`manager_id`=m.`employee_id`;

/*外连接
#应用场景：用于查询一个表中有，另一个表中没有的记录。

特点：1.外连接的查询结果为主表中的所有记录
如果从表中有和它匹配的，则显示匹配的值
如果从表中没有和它匹配的，则显示null
外连接查询结果=内连接结果+主表中有而从表没有的记录

# 查询男朋友不在boys表的女生名。

*/

SELECT * FROM beauty;
SELECT * FROM boys;



SELECT *
FROM beauty g
LEFT  JOIN boys b
ON g.`boyfriend_id`=b.`id`
WHERE b.`id` IS NULL;

SELECT g.`name`
FROM boys b
RIGHT JOIN beauty g
ON b.`id`=g.`boyfriend_id`
WHERE b.`id` IS NULL;

#查询哪个部门没有员工
SELECT d.`department_name`
FROM departments d
LEFT JOIN employees e
ON d.`department_id`=e.`department_id`
WHERE e.`employee_id` IS NULL;

#全连接 full

#交叉连接:笛卡尔乘积
SELECT *
FROM beauty g
CROSS  JOIN boys b;






