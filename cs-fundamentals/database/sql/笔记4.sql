# 分组函数

/*
功能：统计使用，又称为聚合函数或者组函数

sum 、avg 、max 、min 、count

*/


#sum ,avg 忽略null值

SELECT SUM(commission_pct) ,AVG(commission_pct),SUM(commission_pct)/35
,SUM(commission_pct)/107 FROM employees;


#和distinct 搭配

SELECT SUM(DISTINCT salary),SUM(salary) FROM employees;

SELECT COUNT(DISTINCT salary),COUNT(salary) FROM employees;



#count函数的详细介绍

SELECT COUNT(*)FROM employees;

SELECT COUNT(1)FROM employees;

# 和分组函数一同查询的字段又限制


#分组查询


# 查询邮箱中包含a字符的，每个部门的平均工资
SELECT AVG(salary),department_id
FROM employees
WHERE `email` LIKE "%a%"
GROUP BY department_id;

#分组后的筛洗
#查询哪个部门的员工个数大于2
SELECT COUNT(`employee_id`),department_id
FROM employees
GROUP BY department_id
HAVING COUNT(`employee_id`)>2;



#按表达式或者函数分组

#案例：按员工姓名的长度分组，查询每一组的员工个数，筛选员工个数>5的有哪些

SELECT COUNT(*),LENGTH(last_name) AS len_name
FROM employees
GROUP BY LENGTH(last_name)
HAVING COUNT(*)>5;


#按多个字段分组

#案例:查询每个部门每个工种的员工的平均工资

SELECT AVG(salary),department_id,job_id
FROM employees
GROUP BY job_id,department_id;