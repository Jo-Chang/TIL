-- SQL Nested queries



-- 문제 1
SELECT productCode, productName, MSRP
FROM products
WHERE MSRP > (
	SELECT AVG(MSRP)
    FROM products
)
ORDER BY MSRP;



-- 문제 2
SELECT customerNumber, customerName
FROM customers c
WHERE EXISTS (
	SELECT orderDate
    FROM orders o
    WHERE orderDate BETWEEN "030106" AND "030326"
    AND c.customerNumber = o.customerNumber
)
ORDER BY customerNumber;



-- 문제 3
SELECT productCode, productName, productLine, MSRP
FROM products
WHERE MSRP = (
	SELECT MAX(MSRP)
    FROM products
    WHERE productLine = "Classic Cars"
);

SELECT productCode, productName, productLine, MSRP
FROM products
WHERE productLine = "Classic Cars"
ORDER BY MSRP DESC
LIMIT 1;



-- 문제 4
SELECT customerNumber, customerName, country
FROM customers
WHERE country IN (
	SELECT country
    FROM (
		SELECT country, count(*) population
        FROM customers
        GROUP BY country
    ) AS countryPopulation
    WHERE population = (
		SELECT count(*)
        FROm customers
        GROUP BY country
        ORDER BY count(*) DESC
        LIMIT 1
    )
)
ORDER BY customerNumber;

SELECT customerNumber, customerName, country
FROM customers
WHERE country IN (
	SELECT country
    FROM customers
	GROUP BY country
    HAVING count(*) = (
		SELECT count(*) c
        FROm customers
        GROUP BY country
        ORDER BY c DESC
        LIMIT 1
    )
)
ORDER BY customerNumber;

/* LIMIT 안 쓰고 풀이 */
SELECT customerNumber, customerName, country
FROM customers
WHERE country IN (
	SELECT country
    FROM customers
    GROUP BY country
    HAVING count(*) = (
		SELECT MAX(population)
		FROM (
			SELECT country, count(*) population
			FROM customers
			GROUP BY country
		) AS nationalCustomer
    )
)
ORDER BY customerNumber;

SELECT customerNumber, customerName, country
FROM customers
WHERE country = (SELECT MAX(country) FROM customers)
ORDER BY customerNumber DESC;


-- 문제 5
SELECT customerNumber, customerName, order_count
FROM (
	SELECT c.customerNumber, customerName, count(*) order_count
    FROM customers c
    NATURAL JOIN orders o
    GROUP BY customerNumber
) AS newCustomer
WHERE customerNumber IN (
	SELECT customerNumber
	FROM orders o
	GROUP BY customerNumber
	HAVING count(*) = (
		SELECT count(*)
		FROM orders
		GROUP BY customerNumber
		ORDER BY count(*) DESC
		LIMIT 1
	)
);
    
SELECT customerNumber, customerName, count(*) order_count
FROM customers
NATURAL JOIN orders
GROUP BY customerNumber
HAVING order_count = (
	SELECT count(*) cnt
    FROM orders
    GROUP BY customerNumber
    ORDER BY cnt DESC
    LIMIT 1
);



-- 문제 6
SELECT productCode, productName
FROM products
WHERE productCode IN (
	SELECT DISTINCT productCode
    FROM orderdetails
    WHERE orderNumber IN (
		SELECT orderNumber
        FROM orders
        WHERE orderDate BETWEEN "040101" AND "041231"
    )
)
ORDER BY productCode DESC;


SELECT DISTINCT productCode, productName
FROM products
NATURAL JOIN orderdetails
NATURAL JOIN orders
WHERE orderDate BETWEEN "040101" AND "041231"
ORDER BY productCode DESC;


SELECT DISTINCT productCode, productName
FROM products
NATURAL JOIN orderdetails
NATURAL JOIN orders
WHERE YEAR(orderDate) = 2004
ORDER BY productCode DESC;