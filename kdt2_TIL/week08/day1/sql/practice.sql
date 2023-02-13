--  DISTINC #1
/*
테이블 employees에서 lastName 필드의 모든 데이터를 오름차순 조회
*/
SELECT
    lastName
FROM
    employees
ORDER BY
    lastName;


--  DISTINC #2
/*
테이블 employees에서 lastName 필드의 모든 데이터를 중복없이 오름차순 조회
*/
SELECT DISTINC
    lastName
FROM
    employees
ORDER BY
    lastName;

--  WHERE #1
/*
테이블 employees에서 officeCode 필드 값이 1인 데이터의 lastName, firstName, officeCode 조회
*/
SELECT
    lastName, firstName, officeCode
FROM
    employees
WHERE officeCode = 1;

--  WHERE #2
/*
테이블 employees에서 jobTitle 필드 값이 'Sales Rep'이 아닌 데이터의 
lastName, firstName, jobTitle 조회
*/
SELECT
    lastName, firstName, jobTitle
FROM
    employees
WHERE
    jobTitle != 'Sales Rep'

--  WHERE #3
/*
테이블 employees에서 officeCode 필드 값이 3 이상이고
jobTitle 필드 값이 'Sales Rep'인 데이터의
lastName, firstName, officeCode, jobTitle 조회
*/
SELECT
    lastName, firstName, officeCode, jobTitle
FROM
    employees
WHERE
    officeCode >= 3
    AND jobTitle = "Sales Rep";

--  WHERE #4
/*
테이블 employees에서 officeCode 필드 값이 5 미만이거나
jobTitle 필드 값이 'Sales Rep'이 아닌 데이터의
lastName, firstName, officeCode, jobTitle 조회
*/
SELECT
    lastName, firstName, officeCode, jobTitle
FROM
    employees
WHERE
    officeCode < 5
    OR jobTitle != "Sales Rep";

--  WHERE #5
/*
테이블 employees에서 officeCode 필드 값이 1에서 4 사이 값인 데이터의
lastName, firstName, officeCode, jobTitle 조회 (1과 4를 포함)
*/
SELECT
    lastName, firstName, officeCode, jobTitle
FROM
    employees
WHERE
    officeCode BETWEEN 1 AND 4;

--  WHERE #6
/*
테이블 employees에서 officeCode 필드 값이 1에서 4 사이 값인 데이터의
lastName, firstName, officeCode, jobTitle를 오름차순 조회 (1과 4를 포함)
*/
SELECT
    lastName, firstName, officeCode, jobTitle
FROM
    employees
WHERE
    officeCode BETWEEN 1 AND 4
ORDER BY
    officeCode;

--  WHERE #7
/*
테이블 employees에서 officeCode 필드 값이 1 또는 3 또는 4 값인 데이터의
lastName, firstName, officeCode 조회 
*/
SELECT
    lastName, firstName, officeCode
FROM
    employees
WHERE
    -- officeCode != 2 AND officeCode BETWEEN 1 AND 4;
    officeCode IN (1, 3, 4);

--  WHERE #8
/*
테이블 employees에서 officeCode 필드 값이 1과 3 그리고 4가 아닌 데이터의
lastName, firstName, officeCode 조회 
*/
SELECT
    lastName, firstName, officeCode
FROM
    employees
WHERE
    officeCode NOT IN (1, 3, 4);

--  WHERE #9
/*
테이블 employees에서 lastName 필드 값이 son으로 끝나는 데이터의
lastName, firstName 조회 
*/
SELECT
    lastName, firstName
FROM
    employees
WHERE
    lastName LIKE "%son";

--  WHERE #9
/*
테이블 employees에서 firstName 필드 값이 4자리면서 y로 끝나는 데이터의
lastName, firstName 조회 
*/
SELECT
    lastName, firstName
FROM
    employees
WHERE
    firstName LIKE "___y";

--  LIMIT #1
/*
테이블 employees에서 firstName, officeCode 필드 데이터를
officeCode 기준 내림차순으로 7개만 조회
*/
SELECT
    firstName, officecode
FROM
    employees
ORDER BY officeCode DESC
LIMIT
    officeCode 7;

--  LIMIT #2
/*
테이블 employees에서 firstName, officeCode 필드 데이터를
officeCode 기준 내림차순으로 7개만 조회
*/
SELECT
    firstName, officecode
FROM
    employees
ORDER BY officeCode DESC
-- LIMIT 3, 5;
LIMIT 5 OFFSET 3;

--  GROUP BY #1
/*
테이블 customers에서 country 필드를 그룹화하여 각 그룹에 대한
creditLimit의 평균 값을 내림차순 조회
*/
SELECT
    country, 
    Avg(creditLimit) AS avgOfCreditLimit
FROM
    customers
GROUP BY
    country
ORDER BY
    avgOfCreditLimit DESC;

--  GROUP BY #2
/*
테이블 customers에서 country 필드를 그룹화하여 각 그룹에 대한
creditLimit의 평균 값이 80000을 초과하는 데이터만 조회
*/
SELECT
    country, 
    Avg(creditLimit) AS avgOfCreditLimit
FROM
    customers
GROUP BY
    country
HAVING
	avgOfCreditLimit > 80000;
