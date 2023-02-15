-- Multi Table Queries

-- 문제 1
SELECT
	employeeNumber, lastName, firstName, city
FROM
	employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber;
/*
SELECT
	employeeNumber, lastName, firstName, city
FROM
	employees as e, offices as o
where 
	e.officeCode = o.officeCode
ORDER BY
	employeeNumber;
*/  

-- 문제 2
SELECT
	customerNumber, officeCode, c.city, o.city
FROM
	customers AS c
LEFT JOIN offices AS o
	ON c.city = o.city
ORDER BY
	customerNumber DESC;
    
-- 문제 3
SELECT
	customerNumber, officeCode, c.city, o.city
FROM
	customers AS c
RIGHT JOIN offices AS o
	ON c.city = o.city
ORDER BY
	customerNumber DESC;
    
-- 문제 4
SELECT
	customerNumber, officeCode, c.city, o.city
FROM
	customers AS c
INNER JOIN offices AS o
	ON c.city = o.city
ORDER BY
	customerNumber DESC;

-- 문제 5
/*
LEFT JOIN은 왼쪽 테이블(FROM table)의 갯수를 기준으로
RIGHT JOIN은 오른쪽 테이블(JOIN table)의 갯수를 기준으로
INNER JOIN은 왼쪽과 오른쪽 테이블 모두에 존재하는 레코드의 갯수를 기준으로 하기 때문이다.
*/

-- 문제 6
SELECT
	customerNumber, officeCode, c.city, o.city
FROM
	customers AS c
LEFT JOIN offices AS o
	ON c.city = o.city
UNION
SELECT
	customerNumber, officeCode, c.city, o.city
FROM
	customers AS c
RIGHT JOIN offices AS o
	ON c.city = o.city
ORDER BY
	customerNumber DESC;
    
-- 문제 7
SELECT
	o.orderNumber, orderDate
FROM
	orderdetails AS od
INNER JOIN orders AS o
	ON o.orderNumber = od.orderNumber
ORDER BY
	o.orderNumber;
    
-- 문제 8
SELECT
	orderNumber, od.productCode, productName
FROM
	orderdetails AS od
INNER JOIN products AS p
	ON od.productCode = p.productCode
ORDER BY
	orderNumber;
    
-- 문제 9
SELECT
	o.orderNumber, od.productCode, orderDate, productName
FROM
	orderdetails AS od
INNER JOIN orders AS o
	ON o.orderNumber = od.orderNumber
INNER JOIN products AS p
	ON od.productCode = p.productCode
ORDER BY
	orderNumber;