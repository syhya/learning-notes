
USE myemployees;
#基础查询
#1.查询单个字段：  查询员工表中的last_name  
SELECT last_name FROM employees;

#2. 查询多个字段：
SELECT last_name, email, job_id FROM employees;

#3.所有字段：
SELECT * FROM employees;

#4.查询常量值、表达式和函数
SELECT 100;
SELECT "join";
SELECT 12%3;
SELECT VERSION();


#5.起别名
#方法一：
SELECT 12*3 AS "结果" ;
SELECT last_name AS 姓, first_name AS 名 FROM employees; 

#方法二：
SELECT last_name  姓, first_name  名 FROM employees; 

6.#去重

#查询员工表中涉及到的所有的部门编号 distinct

SELECT DISTINCT department_id FROM employees;

7.# +号的作用
# mysql：+是运算符

# 查询员工名和姓连接成一个字段，并显示为 姓名   concat

SELECT CONCAT(last_name, first_name) AS 姓名 FROM employees; 
