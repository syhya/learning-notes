# 子查询

/*
含义:出现在其他语句中的select语句，称为子查询或内查询。
外

分类：
按子查询出现的位置：
	select后面：
		仅仅支持标量子查询
	from 后面
		支持表子查询
	where或者having后面：
		标量子查询（单行）
		列子查询（多行）
		行子查询
	exists后面（相关子查询）
		表子查询
按结果集的行列数不同：
	标量子查询（结果集只有一行一列）
	列子查询（结果集只有一列多行）
	行子查询(结果集有一行多列)
	表子查询（结果集一般为多行多列）

*/



#一.where或者having后面
/*
标量子查询（单行子查询）
列子查询（多行子查询）
行子查询


特点：
1.子查询放在小括号内
2.子查询一般放在条件的右侧
3.标量子查询，一般搭配着单行操作符使用
> < >= <= = <>

列子查询，一般搭配着多行操作符使用
in、any/some、all

4.子查询的执行优先于主查询执行。

*/


#1.标量子查询

#谁的工资比Abel高？

SELECT salary
FROM employees 
WHERE last_name ="Abel";


SELECT last_name
FROM employees
WHERE salary >(
	SELECT salary
	FROM employees 
	WHERE last_name ="Abel"
);


#题目：返回job_id与141号员工相同，salary比143号员工多的员工姓名，job_id 和工资
SELECT job_id 
FROM employees
WHERE employee_id =141;

SELECT salary
FROM employees
WHERE employee_id =143;

SELECT job_id,salary
FROM employees
WHERE job_id =(
	SELECT job_id 
	FROM employees
	WHERE employee_id =141
)
AND salary>(
	SELECT salary
	FROM employees
	WHERE employee_id =143
);

#返回公司工资最少的员工的last_name,job_id和salary

SELECT MIN(salary)
FROM employees;

SELECT last_name,job_id,salary
FROM employees
WHERE salary=(
	SELECT MIN(salary)
	FROM employees
);

#查询最低工资大于50号部门最低工资的部门id和其最低工资

SELECT department_id,MIN(salary)
FROM employees
GROUP BY department_id
HAVING MIN(salary)>(
	SELECT MIN(salary)
	FROM employees
	WHERE department_id =50);

# 非法使用标量子查询 

#列子查询（多行子查询）

#返回location_id是1400或1700的部门中的所有员工姓名

SELECT DISTINCT `department_id`
FROM departments
WHERE location_id IN(1400,1700);

SELECT last_name
FROM employees 
WHERE department_id IN(
	SELECT DISTINCT `department_id`
	FROM departments
	WHERE location_id IN(1400,1700)
);


#返回其它工种中比job_id为‘IT_PROG’部门任一工资低的员工的员工号、姓名、
#job_id以及salary

SELECT salary 
FROM employees
WHERE job_id ="IT_PROG";

SELECT `employee_id`,`last_name`,`job_id`,salary
FROM employees
WHERE salary< ANY(
	SELECT salary 
	FROM employees
	WHERE job_id ="IT_PROG"
)AND job_id<>"IT_PROG";


SELECT `employee_id`,`last_name`,`job_id`,salary
FROM employees
WHERE salary< (
	SELECT MAX(salary) 
	FROM employees
	WHERE job_id ="IT_PROG"
)AND job_id<>"IT_PROG";


#返回工种中比job_id为‘IT_PROG’部门所有工资都低的员工的员工号、姓名、job_id 以及salary
SELECT `employee_id`,`last_name`,`job_id`,salary
FROM employees
WHERE salary< ALL(
	SELECT salary 
	FROM employees
	WHERE job_id ="IT_PROG"
)AND job_id<>"IT_PROG";


SELECT `employee_id`,`last_name`,`job_id`,salary
FROM employees
WHERE salary<(
	SELECT MIN(salary) 
	FROM employees
	WHERE job_id ="IT_PROG"
)AND job_id<>"IT_PROG";

#行子查询
#查询员工编号最小并且工资最高的员工信息

SELECT MIN(`employee_id`)
FROM employees;

SELECT MAX(salary)
FROM employees;

SELECT * 
FROM employees
WHERE employee_id=(
	SELECT MIN(`employee_id`)
	FROM employees)
AND salary=(
	SELECT MAX(salary)
	FROM employees);
	
	
	
SELECT * 
FROM employees
WHERE (employee_id,salary)=(
	SELECT MIN(employee_id),MAX(salary)
	FROM employees);



# select 后面
# 查询每个部门的员工个数

SELECT d.*,(

	SELECT COUNT(*)
	FROM employees e 
	WHERE e.department_id = d.department_id
	)个数
FROM departments d;

SELECT d.*,COUNT(employee_id)
FROM departments d 
LEFT JOIN employees e
ON d.`department_id`=e.`department_id`
GROUP BY d.`department_id`;



