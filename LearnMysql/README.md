# LearnMysql

## Mysql中常用的文本处理函数

| 函数               | 说明                 |
| ------------------ | ----------------     |
| Left()             | 返回字符串左边的字符 |
| Right()            | 返回串右边的字符     |
| Length()           | 返回串的长度         |
| Locate()           | 找出串的一个子串     |
| Lower()            | 将串转为小写         |
| Upper()            | 将串转为大写         |
| LTrim()            | 去除字符串左边的空格 |
| RTrim()            | 去除字符串右边的空格 |
| SubString()        | 返回子串的字符       |
| Soundex()          | 返回串的 SOUNDEX值   |

## 常用的日期和时间处理函数

| 函数          | 说明                           |
|---------------|--------------------------------|
| AddDate()     | 增加一个日期（天，周等）       |
| AddTime()     | 增加一个时间（时，分等）       |
| CurDate()     | 返回当前日期                   |
| CurTime()     | 返回当前的时间                 |
| Date()        | 返回日期时间的日期部分         |
| DateDiff()    | 计算两个日期只差               |
| Date_Add()    | 高度灵活的日期运算函数         |
| Date_Format() | 返回一个格式化的日期或时间     |
| Day()         | 返回一个日期的天数部分         |
| DayOfWeek()   | 对于一个日期，返回对应的星期几 |
| Hour()        | 返回一个时间的小时部分         |
| Minute()      | 返回一个时间的分钟部分         |
| Month()       | 返回一个日期的月份部分         |
| Now()         | 返回当前日期和时间             |
| Second()      | 返回一个时间的秒部分           |
| Time()        | 返回一个时间的时间部分         |
| Year()        | 返回一个时间的年份部分         |


- 示例1

```
mysql> SELECT now(), order_date,DATE(order_date), DAYOFWEEK(order_date), CURDATE(), CURTIME(), cust_id, order_num FROM orders WHERE order_date = '2005-09-01';
+---------------------+---------------------+------------------+-----------------------+------------+-----------+---------+-----------+
| now()               | order_date          | DATE(order_date) | DAYOFWEEK(order_date) | CURDATE()  | CURTIME() | cust_id | order_num |
+---------------------+---------------------+------------------+-----------------------+------------+-----------+---------+-----------+
| 2020-04-19 21:24:03 | 2005-09-01 00:00:00 | 2005-09-01       |                     5 | 2020-04-19 | 21:24:03  |   10001 |     20005 |
+---------------------+---------------------+------------------+-----------------------+------------+-----------+---------+-----------+
1 row in set (0.00 sec)


mysql> SELECT
    -> order_date,
    -> YEAR(order_date),
    -> Time(order_date),
    -> SECOND(order_date),
    -> Now(),
    -> MONTH(order_date),
    -> MINUTE(order_date),
    -> HOUR(order_date),
    -> DAYOFWEEK(order_date),
    -> DAY(order_date),
    -> DATE(order_date),
    -> CURTIME(),
    -> CURDATE(),
    -> cust_id,
    -> order_num
    -> FROM
    -> orders
    -> WHERE
    -> DATE(order_date) = '2005-09-01'\G
*************************** 1. row ***************************
           order_date: 2005-09-01 10:09:50
     YEAR(order_date): 2005
     Time(order_date): 10:09:50
   SECOND(order_date): 50
                Now(): 2020-04-19 21:35:00
    MONTH(order_date): 9
   MINUTE(order_date): 9
     HOUR(order_date): 10
DAYOFWEEK(order_date): 5
      DAY(order_date): 1
     DATE(order_date): 2005-09-01
            CURTIME(): 21:35:00
            CURDATE(): 2020-04-19
              cust_id: 10001
            order_num: 20005
```

## 常用的数值处理函数

| 函数   | 说明               |
| ------ | ------             |
| Abs()  | 返回一个说的绝对值 |
| Cos()  | 返回一个角度的余弦 |
| Exp()  | 返回一个数的指数值 |
| Mod()  | 返回操作数的余数   |
| Pi()   | 返回圆周率         |
| Rand() | 返回一个随机数     |
| Sin()  | 返回一个角度的正弦 |
| Sqrt() | 返回一个数的平方根 |
| Tan()  | 返回一个说的正切   |


## 聚合函数

| 函数    | 说明             |
|---------|------------------|
| AVG()   | 返回某列的平均值 |
| Count() | 返回某列的行数   |
| MAX()   | 返回某列的最大值 |
| MIN()   | 返回某列的最小值 |
| SUM()   | 返回某列之和     |


- COUNT(*) 对表中行的数目进行计数，不管表列中包含的是空值（NULL) 还是非空值
- COUNT(column) 对特定列中具有值的行进行计数，湖绿NULL值


## 连接表查询

> 下面的等值联结和内部联结效果相同，`ANSI SQL`规范首选 `INNER JOIN`语法

- 等值联结
	- 基于两个表之间的相等

```
mysql> SELECT vend_name, prod_name, prod_price FROM vendors, products WHERE vendors.vend_id = products.vend_id ORDER BY vend_name, prod_name;
+-------------+----------------+------------+
| vend_name   | prod_name      | prod_price |
+-------------+----------------+------------+
| ACME        | Bird seed      |      10.00 |
| ACME        | Carrots        |       2.50 |
| ACME        | Detonator      |      13.00 |
| ACME        | Safe           |      50.00 |
| ACME        | Sling          |       4.49 |
| ACME        | TNT (1 stick)  |       2.50 |
| ACME        | TNT (5 sticks) |      10.00 |
| Anvils R Us | .5 ton anvil   |       5.99 |
| Anvils R Us | 1 ton anvil    |       9.99 |
| Anvils R Us | 2 ton anvil    |      14.99 |
| Jet Set     | JetPack 1000   |      35.00 |
| Jet Set     | JetPack 2000   |      55.00 |
| LT Supplies | Fuses          |       3.42 |
| LT Supplies | Oil can        |       8.99 |
+-------------+----------------+------------+
14 rows in set (0.00 sec)
```


> 创建联结的基本规则，首先列出所有的表，然后定义表之间的关系

- 内部联结

```SQL
SELECT vend_name, prod_name, prod_price FROM vendors INNER JOIN products ON vendors.vend_id = products.vend_id;
```

> 联结多个表

```SQL
SELECT prod_name, vend_name, prod_price, quantity 
FROM orderitems, products, vendors 
WHERE 
	products.vend_id = vendors.vend_id AND
	orderitems.prod_id = products.prod_id
```

- 自联结

	> 优先采用自联结而不是子查询

	- 子查询
	```SQL
	SELECT prod_id, prod_name FROM products WHERE vend_id = ( SELECT vend_id FROM products WHERE prod_id = 'DTNTR');
	```

	- 自联结
	```SQL
	 SELECT p1.prod_id, p1.prod_name FROM products AS p1, products AS p2 WHERE p1.vend_id = p2.vend_id AND p2.prod_id = 'DTNTR';
	```

- 外部联结 `OUTER JOIN` 必须指定`LEFT或RIGHT`关键字
	> `LEFT OUTER JOIN xx ON` 以左边的表为基础

	- SELECT x,x FROM A LEFT OUTER JOIN B ON a.xx = b.xx;

	```SQL
	mysql> SELECT customers.cust_id, orders.order_num FROM customers LEFT OUTER JOIN orders ON customers.cust_id = orders.cust_id;
	+---------+-----------+
	| cust_id | order_num |
	+---------+-----------+
	|   10001 |     20005 |
	|   10001 |     20009 |
	|   10002 |      NULL |
	|   10003 |     20006 |
	|   10004 |     20007 |
	|   10005 |     20008 |
	+---------+-----------+
	6 rows in set (0.00 sec)
	```

	> `RIGHT OUTER JOIN xx ON` 

	```SQL
	mysql> SELECT customers.cust_id, orders.order_num FROM customers RIGHT OUTER JOIN orders ON customers.cust_id = orders.cust_id;
	+---------+-----------+
	| cust_id | order_num |
	+---------+-----------+
	|   10001 |     20005 |
	|   10001 |     20009 |
	|   10003 |     20006 |
	|   10004 |     20007 |
	|   10005 |     20008 |
	+---------+-----------+
	5 rows in set (0.00 sec)
	```

- 使用带聚集函数的联结

```
mysql> SELECT customers.cust_name, customers.cust_id, COUNT(orders.order_num) AS num_ord
    -> FROM customers INNER JOIN orders
    -> ON customers.cust_id = orders.cust_id
    -> GROUP BY customers.cust_id;
+----------------+---------+---------+
| cust_name      | cust_id | num_ord |
+----------------+---------+---------+
| Coyote Inc.    |   10001 |       2 |
| Wascals        |   10003 |       1 |
| Yosemite Place |   10004 |       1 |
| E Fudd         |   10005 |       1 |
+----------------+---------+---------+
4 rows in set (0.01 sec)
```

```
mysql> SELECT customers.cust_name, customers.cust_id,COUNT(orders.order_num) AS num_ord
    -> FROM customers LEFT OUTER JOIN orders
    -> ON customers.cust_id = orders.cust_id
    -> GROUP BY customers.cust_id ;
+----------------+---------+---------+
| cust_name      | cust_id | num_ord |
+----------------+---------+---------+
| Coyote Inc.    |   10001 |       2 |
| Mouse House    |   10002 |       0 |
| Wascals        |   10003 |       1 |
| Yosemite Place |   10004 |       1 |
| E Fudd         |   10005 |       1 |
+----------------+---------+---------+
5 rows in set (0.00 sec)
```

## 组合查询

> UNION 规则

- `UNION`必须由两条或两条以上的SELECT 语句组成
- `UNION`中的每个查询必须包含相同的列、表达式或聚集函数（各个列不需要以相同的次序列出）
- `UNION ALL` 包含重复的列

> 示例: 达到`SELECT vend_id, prod_id, prod_price FROM products WHERE prod_price <= 5 or vend_id IN (1001, 1002);`的效果

```SQL
ql> SELECT vend_id, prod_id, prod_price FROM products WHERE prod_price <= 5
    -> UNION
    -> SELECT vend_id, prod_id, prod_price FROM products WHERE vend_id IN(1001,1002);
+---------+---------+------------+
| vend_id | prod_id | prod_price |
+---------+---------+------------+
|    1003 | FC      |       2.50 |
|    1002 | FU1     |       3.42 |
|    1003 | SLING   |       4.49 |
|    1003 | TNT1    |       2.50 |
|    1001 | ANV01   |       5.99 |
|    1001 | ANV02   |       9.99 |
|    1001 | ANV03   |      14.99 |
|    1002 | OL1     |       8.99 |
+---------+---------+------------+
8 rows in set (0.00 sec)
```
