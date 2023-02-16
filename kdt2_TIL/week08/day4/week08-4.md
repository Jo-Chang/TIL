# Week08-4

-   SQL - Nested Queries


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)

<br>

-----


## Introduction to Subquery

-   Subquery : 단일 쿼리문에 여러 테이블의 데이터를 결합하는 방법
    +   A query inside a query
-   조건에 따라 하나 이상의 테이블에서 데이터를 검색하는데 사용
-   SELECT, FROM, WHERE, HAVING 절 등 다양한 맥락에서 사용

-   <span>EXISTS</span> operator : 쿼리 문에서 반환된 레코드의 존재 여부를 확인
    ```sql
    /*
    subquery가 하나 이상의 행을 반환하면 EXISTS 연산자는 true를 반환하고 그렇지 않으면 false를 반환
    주로 WHERE 절에서 subquery의 반환 값 존재 여부를 확인하는데 사용
    */
    SELECT
        select_list
    FROM
        table
    WHERE
        [NOT] EXISTS (subquery);
    ```


-----


## Conditional Statements

-   <span>CASE</span> statement : SQL문에서 조건문을 구성
    ```sql
    /*
    case_value가 when_value와 동일한 것을 찾을 때까지 순차적으로 비교
    when_value와 동일한 case_value를 찾으면 해당 THEN절의 코드를 실행
    동일한 값을 찾지 못하면 ELSE절의 코드를 실행
    */
    CASE case_value
        WHEN when_value1 THEN statements
        WHEN when_value2 THEN statements
        ...
        [ELSE els-statements]
    END CASE;
    ```