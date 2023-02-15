-- INNER JOIN example
SELECT
    *
FROM
    articles
INNER JOIN users
    ON articles.userID = users.id;

-- INNER JOIN #1
SELECT
    productCode, productName
FROM
    products AS p
INNER JOIN productlines AS pl
    ON p.productline = pl.productline;

-- INNER JOIN #2
SELECT
    o.orderNumber, status
FROM
    orders AS o
INNER JOIN orderdetails AS od
    ON o.orderNumber = od.orderNumber;

-- INNER JOIN #3
SELECT
    o.orderNumber, 
    status, 
    SUM(od.quantityOrdered*od.priceEach) AS total
FROM
    orders AS o
INNER JOIN orderdetails AS od
    ON o.orderNumber = od.orderNumber
GROUP BY
	o.orderNumber;

-- LEFT JOIN #1
SELECT
	contactFirstName, orderNumber, status
FROM
	customers AS c
LEFT JOIN orders AS o
	ON c.customerNumber = o.customerNumber;

-- LEFT JOIN #2
SELECT
	contactFirstName, orderNumber, status
FROM
	customers AS c
LEFT JOIN orders AS o
	ON c.customerNumber = o.customerNumber
WHERE
	orderNumber IS NULL;

-- RIGHT JOIN #1
SELECT
	employeeNumber, firstName, customerNumber, contactFirstName
FROM
	customers
RIGHT JOIN employees
	ON salesRepEmployeeNumber = employeeNumber;

-- RIGHT JOIN #2
SELECT
	employeeNumber, firstName, customerNumber, contactFirstName
FROM
	customers
RIGHT JOIN employees
	ON salesRepEmployeeNumber = employeeNumber
WHERE
	customerNumber IS NULL;