# 进阶2：条件查询

/*
一.按条件表达式筛选
条件运算符:>   <   =   !=  <>  >=   <=

二.按逻辑表达式筛选
逻辑运算符：and or not 

三.模糊查询
	like 
	between and 
	in 
	is null   is not null
	
like:一般搭配通配符使用，可以判断字符型或数值型
通配符：%任意多个字符，_任意单个字符
*/



SELECT * 
FROM employees 
WHERE last_name LIKE "%a%";


#查询员工的工种编号是IT_PROG、AD_VP、AD_PRES的员工信息
SELECT*
FROM employees
WHERE job_id IN ("IT_PROG","AD_VP","AD_PRES")


# 安全等于 <=>

SELECT * 
FROM employees
WHERE salary <=>12000;