#进阶4：常见函数
/*
1.单行函数

2.分组函数




 
 */
 
 #length
 SELECT LENGTH("python");
 SELECT LENGTH("张三");   # utf8一个汉字三个字节
 SHOW VARIABLES LIKE "%char%";
 
#upper、lower
SELECT UPPER("john");
SELECT LOWER("JOHn");
 
#将姓变大写，名变小写，然后拼接

SELECT CONCAT(UPPER(last_name),"_",LOWER(first_name)) AS 姓名
FROM employees;


#substr、substring

#注意：索引从1开始
SELECT SUBSTRING("今天天气很好",5) AS 很好;

SELECT SUBSTRING("今天天气很好",1,2) AS 今天;


SELECT CONCAT(UPPER(SUBSTR(last_name,1,1)),"_",LOWER(SUBSTR(last_name,2)))
FROM employees;

#instr 返回子串第一次出现的索引，如果找不到返回0
SELECT INSTR("今天天气很好","很好") AS out_put;

#trim 去前后空格
SELECT LENGTH (TRIM("   天气   ")) ;

SELECT TRIM("a" FROM "aaa天aaa气aaaaaaaaa") AS out_put;


#lpad 用指定的字符实现左填充指定长度

SELECT LPAD("天气",10,"&") AS out_put;

#rpad 用指定的字符实现右填充指定长度

SELECT RPAD("天气",10,"&") AS out_put;


#replace 替换

SELECT REPLACE("天气很好很好很好","很好","不好") AS out_put;

# round 四舍五入

SELECT ROUND(-1.45);
SELECT ROUND(1.56788,2);

#ceil 向上取整,返回>=该参数的最小整数

SELECT CEIL(1.00001);

#floor 向下取整,返回<=该参数的最大整数

SELECT FLOOR(-9.99);

#truncate 截断

SELECT TRUNCATE(1.999,2);

#mod 取余
SELECT MOD(10,3);

SELECT 10%3;

#日期函数

#now 返回当前系统日期+时间

SELECT NOW();

#curdate 
SELECT CURDATE();

#curtime
SELECT CURTIME()

#可以获取指定的部分，年、月、日、小时、分钟、秒
SELECT YEAR(NOW())


USE myemployees;
SELECT YEAR(hiredate) AS 年 FROM employees;

SELECT MONTH(NOW()) AS  月 ;
SELECT MONTHNAME(NOW()) AS 月 ;

#str_to_date

SELECT STR_TO_DATE("1998-3-2","%Y-%c-%d") AS out_put;

SELECT* FROM employees WHERE hiredate = "1992-4-3";

SELECT *FROM employees WHERE hiredate = STR_TO_DATE("4-3 1992","%c-%d %Y"); 

#date_format

SELECT DATE_FORMAT(NOW(),"%y年%m月%d日") AS out_put;

#查询有奖金的员工名和入职日期（xx月/xx日 xx年）

SELECT last_name,DATE_FORMAT(hiredate,"%m月/%d日 %y年") AS 入职日期
FROM employees
WHERE commission_pct IS NOT NULL;


#其他函数

SELECT VERSION();
SELECT DATABASE();
SELECT USER();


#流程控制函数

#if函数
SELECT IF(10>5,"大","小")

SELECT last_name,commission_pct,
IF(commission_pct IS NULL,"无奖金","有奖金") AS 备注
FROM employees;
 
#case函数: switch case 的效果

/*


case 要判断的字段或者表达式

when 常量1 then 要显示的值1或者语句1；
when 常量2 then  要显示的值2或者语句2；
...
else 要显示的值n或者语句n;
end
*/

SELECT salary  AS 原始工资,department_id,
CASE department_id
WHEN 30 THEN salary*1.1
WHEN 40 THEN salary*1.2
WHEN 50 THEN salary*1.3
ELSE salary
END AS 新工资
FROM employees;


# case函数的使用2

/*
case 
when 条件1 then 要显示的值1或者语句1
when 条件2 then 要显示的值2或者语句2
...
else 要显示的值n或者语句n
*/

#案例：查询员工的工资的情况
/*
如果工资>20000,显示A级别
如果>15000
>10000
否则D
*/


SELECT salary 

  

