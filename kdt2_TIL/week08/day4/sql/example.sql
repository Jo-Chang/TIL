-- Subquery example
-- table1에서 가장 나이가 어린 사람을 삭제
DELETE FROM table1
WHERE age = (
    SELECT MIN(age) FROM table1
);

-- Subquery #1
SELECT customerNumber
FROM payments
WHERE amount = (SELECT MAX(amount) FROM payments);
/*
SELECT customerNumber
FROM payments
ORDER BY amount DESC
LIMIT 1;
*/
/*
같지 않지만 소비 '누적금'이 가장 많은 고객 번호 조회
SELECT customerNumber, SUM(amount) amount2
FROM payments
GROUP BY customerNumber
HAVING amount2
ORDER BY amount2 DESC
LIMIT 1;

SELECT customerNumber, SUM(amount) amount2
FROM payments
GROUP BY customerNumber
HAVING amount2 = (
	select sum(amount) amount3
    from payments
    group by customerNumber
    order by amount3 DESC
    LIMIT 1
);
*/

-- Subquery #1+
SELECT customerNumber, amount, contactFirstName
FROM payments
NATURAL JOIN customers
WHERE amount = (
	SELECT MAX(amount)
    FROM payments
);
/*
SELECT customerNumber, amount, contactFirstName
FROM (
    SELECT contactFirstName, amount, p.customerNumber
    FROM payments p
    NATURAL JOIN customers
    // INNTER JOIN customers USING (customerNumber)
) AS findName
WHERE amount = (
    SELECT MAX(amount)
    FROM payments
);

소비 '누적금'이 가장 많은 고객 번호와 이름 조회
SELECT customerNumber, SUM(amount) sumAmount, contactFirstName
FROM (
	SELECT customerNumber, amount, contactFirstName
    FROM payments
    INNER JOIN customers USING (customerNumber)
) AS sumPayments
GROUP BY customerNumber
HAVING sumAmount = (
	SELECT MAX(sumAmount)
    FROM (
		SELECT SUM(amount) sumAmount
        FROM payments
        GROUP BY customerNumber
    ) AS groupPayments
);
*/

-- Subquery #2
SELECT lastName, firstName
FROM employees
WHERE officeCode IN (
	SELECT officeCode
	FROM offices
	WHERE country = "USA"
);

-- Subquery #3
SELECT customerName
FROM customers
WHERE customerNumber NOT IN (
	SELECT DISTINCT customerNumber
    FROM orders
);

-- EXISTS #1
SELECT customerNumber, customerName
FROM customers c
WHERE EXISTS (
	SELECT *
    FROM orders o
    WHERE c.customerNumber = o.customerNumber
);

-- EXISTS #2
SELECT *
FROM employees e
WHERE EXISTS (
	SELECT *
    FROM offices o
    WHERE city = "Paris"
    AND e.officeCode = o.officeCode
);

-- CASE #1
SELECT contactFirstName, creditLimit, 
	CASE
		WHEN creditLimit > 100000 THEN "VIP"
        WHEN creditLimit > 70000 THEN "Platinum"
        ELSE "Bronze"
    END AS grade
FROM customers;

-- CASE #2
SELECT orderNumber, status, 
	CASE
		WHEN status = "In Process" THEN "주문중"
        WHEN status = "Shipped" THEN "발주완료"
        WHEN status = "Cancelled" THEN "주문취소"
		ELSE "기타사유"
    END AS details
FROM orders;