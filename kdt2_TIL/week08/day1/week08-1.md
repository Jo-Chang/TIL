# Week08-1

-   SQL query


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">


<br>[Parent Contents...](../../README.md/#til-today-i-learned)

-----

## Filtering Data

-   <span>DISTINCT</span> clause : 중복된 값을 제외하고 표시

    ```sql
    SELECT DISTINC
        select_list
    FROM
        table_name;
    ```

-   <span>WHERE</span> cluase : 조회 시 특정 검색 조건을 지정
    +   AND(&&), OR(||), NOT(!)
    +   IN
    +   LIKE "%" "_"
    
-   <span>LIMIT</span> clause : 조회하는 레코드 수를 제한

    ```sql
    SELECT
        select_list
    FROM
        table_name
    LIMIT [offset,] row_count;


## Grouping Data

-   <span>GROUP BY</span> clause : 레코드를 그룹화하여 요약본 생성 with 집계 함수(Aggregation Functions)

-   집계 함수 ( Aggregation Functions ) : 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
    +   SUM, AVG, MAX, MIN, COUNT

    ```sql
    SELECT
        c1, c2, ..., cn, aggregate_function(ci)
    FROM
        table_name
    GROUP BY
        c1, c2, ..., cn;
    ```

## Tips

-   정렬에서의 NULL
    +   오름차순 정렬 시 NULL이 가장 먼저 출력

    ```sql
    SELECT
        postalCode
    FROM
        customers
    WHERE
        postalCode IS NOT NULL
    ORDER BY
        postalCode;
    ```