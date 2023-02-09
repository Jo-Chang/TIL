# Week07-4

-   Database basic, Query


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">


[Parent Contents...](../../README.md/#til-today-i-learned)

-----


## SQL

-   SQL ( Structure Query[^1] Language ) : 테이블의 형태로 <span>구조화</span>된 관계형 데이터베이스에게 요청을 <span>질의(요청)</span>
-   컴퓨터와의 대화 - 프로그래밍 언어, 관계형 데이터베이스와의 대화 - SQL
    
    ```sql
    /* How old is earth */
    SELECT age FROM solar_system WHERE name = 'earth'
    ```
-   SQL 키워드는 대소문자 구분 X
-   SQL Statements의 끝에는 세미콜론(;)이 필요

[^1] : Query : 묻다, 질문하다


-----


## SQL Statements

-   SQL 문, Query 문 ( SQL Statements ) : SQL 코드 실행을 위한 가장 기본적인 블록

|유형|역할|SQL 키워드|
| :---: | :---: | :---: |
|DDL<br>(Data Definition Language)|데이터의 기본 구조 및 형식 변경|CREATE<br>DROP<br>ALTER|
|DQL<br>(Data Query Language)|데이터 검색|SELECT|
|DML<br>(Data Manipulation Language|데이터 조작<br>(추가, 수정, 삭제)|INSERT<br>UPDATE<br>DELETE|
|DCL<br>(Data Control Language)|데이터 및 작업에 대한<br>사용자 권한 제어|COMMIT<br>ROLLBACK<br>GRANT<br>REVOKEV|


-----


## Querying Data

-   <span>SELECT</span> statement : 테이블에서 데이터를 조회
-   SELECT statement 실행 순서
>   FROM (테이블에서) -> SELECT (조회하여) -> ORDER BY (정렬)

-   Example

    1.   테이블 employees에서 lastName 필드의 모든 데이터 조회

    ```sql
    SELECT lastName FROM employees;
    ```

    2.   테이블 employees에서 lastName, firstName 필드의 모든 데이터 조회

    ```sql
    SELECT lastName, firstName FROM employees;
    ```

    3.   테이블 employees에서 모든 필드의 데이터 조회

    ```sql
    SELECT * FROM employees;
    ```

    4.   테이블 employees에서 firstName 필드의 모든 데이터 조회 
    <br>('이름'으로 출력명 변경)

    ```sql
    SELECT firstName AS '이름' FROM employees;
    ```

    5.   테이블 orderedetails에서 productCode, 주문 총액 필드의 모든 데이터를 조회
    <br>(단, 주문 총액 필드는 quantityOrdered와 priceEach 필드를 곱한 결과 값)

    ```sql
    SELECT productCode, (quantityOrdered * priceEach) AS '주문총액' FROM orderdetails;
    ```

    
-----


## Sorting Data

-   ORDER BY syntax : 하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬
    +   ASC : 오름차순 (기본 값)
    +   DESC : 내림차순

    ```sql
    SELECT
        select_list
    FROM
        table_name
    ORDER BY
        column1 [ASC|DESC],
        column2 [ASC|DESC],
        ...;
    ```

-   Example

    1.  테이블 employees에서 firstName 필드의 모든 데이터를 오름차순으로 조회

    ```sql
    SELECT firstName FROM employees ORDER BY firstName;
    ```

    2. 테이블 employees에서 firstName 필드의 모든 데이터를 내림차순으로 조회

    ```sql
    SELECT firstName FROM employees ORDER BY firstName DESC;
    ```

    3. 테이블 employees에서 lastName 필드를 기준으로 내림차순으로 정렬한 다음 firstName 필드 기준으로 오름차순 정렬하여 조회

    ```sql
    SELECT lastName, firstName FROM employees ORDER BY lastName DESC, firstName;
    ```

    4. 테이블 orderdetails에서 totalSales 필드를 기준으로 내림차순으로 정렬한 다음 productCode, totalSales 필드의 모든 데이터를 조회
    <br>(단, totalSales 필드는 quantityOrdered와 priceEach 필드를 곱한 결과 값)

    ```sql
    SELECT productcode, (quantityOrdered * priceEach) AS totalSales FROM orderdetails ORDER BY totalSales DESC;
    ```

