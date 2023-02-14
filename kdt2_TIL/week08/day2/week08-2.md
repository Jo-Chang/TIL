# Week08-2

-   SQL - Managing Tables


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)

## Contents
- [Managing Tables](#managing-tables)
- [Modifying Data](#modifying-data)

-----

## Managing Tables

-   DDL ( Data Definition Language ) : 데이터의 기본 구조 및 형식 변경
    +   CREATE
    +   DROP
    +   ALTER

### CREATE a table

-   <span>CREATE TABLE</span> statement : 테이블 생성
-   CREATE syntax
```sql
CREATE TABLE table_name (
    column_1 data_type,
    column_2 data_type,
    ...,
    constraints
);
```

-   CHAR vs VARCHAR : CHAR은 어떤 문자열이 들어와도 설정한 길이만큼 문자열 길이를 가지고 VARCHAR은 들어온 문자열 길이만큼만 길이 할당

-   제약 조건 ( Constraint ) : 데이터 <span>무결성</span>[^1]을 지키기 위해 데이터를 입력 받을 때 실행하는 검사 규칙
    +   PRIMARY KEY : 해당 필드를 기본 키로 지정
    +   NOT NULL : 해당 필드에 NULL 값을 저장하지 못하도록 지정

-   AUTO_INCREMENT attribute : 테이블의 기본 키에 대한 번호 자동 생성
    +   기본 키 필드에 사용
    +   시작 값은 1이며 데이터 입력 시 값을 생략하면 자동으로 1씩 증가
    +   이미 사용한 값을 재사용하지 않음

[^1] : 무결성 : 데이터의 정확성과 일관성을 보증

### Delete a table

-   <span>DROP Table statement</span> : 테이블 삭제
-   DROP syntax
```sql
DROP TABLE table_name;
```

### Modifying table fields

-   <span>ALTER TABLE</span> statement : 테이블 필드 조작(생성, 수정, 삭제)
    +   ALTER TABLE <span>ADD</span> : 필드 추가
    ```sql
    /*
    ADD 키워드 이후 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성
    */
    ALTER TABLE
        table_name
    ADD
        new_column_name column_definition
    ```

    +   ALTER TABLE <span>MODIFY</span> : 필드 속성 변경
    ```sql
    /* 
    MODIFY 키워드 이후 변경하고자 하는 필드 이름
    그리고 데이터 타입 및 제약 조건 작성
    */
    ALTER TABLE
        table_name
    MODIFY
        column_name column_definition;
    ```

    +   ALTER TABLE <span>CHANGE COLUMN</span> : 필드 이름 변경
    ```sql
    /*
    CHANGE COLUMN 키워드 이후
    기존 필드 이름, 변경하고자 하는 필드 이름 그리고 데이터 타입 및 제약조건 작성
    */
    ALTER TABLE
        table_name
    CHANGE COLUMN
        original_name new_name column_definition
    ```

    +   ALTER TABLE <span>DROP COLUMN</span> : 필드 삭제
    ```sql
    /*
    DROP COLUMN 키워드 이후 삭제하고자 하는 필드 이름 작성
    */
    ALTER TABLE
        table_name
    DROP COLUMN
        column_name;
    ```


-----


## Modifying Data

-   DML ( Data Manipulation Language ) : 데이터 조작 (추가, 수정, 삭제)
    +   INSERT
    +   UPDATE
    +   DELETE

### INSERT data into table

-   <span>INSERT</span> statement : 테이블 레코드 삽입
-   INSERT syntax
```sql
/*
INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록을 작성
VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록을 작성
*/
INSERT INTO table_name (c1, c2, ...)
VALUES (v1, v2, ...)
```

### Update data in table

-   <span>UPDATE</span> statement : 테이블 레코드 수정
-   UPDATE syntax
```sql
/*
SET 절 다음에 수정 할 필드와 새 값을 지정
WHERE 절에서 수정 할 레코드를 지정하는 조건 작성
*/
UPDATE table_name
SET column_name = expression,
[WHERE
    condition];
```

## Delete data from table

-   <span>DELETE</span> statement : 테이블 레코드 삭제
-   DELETE syntax
```sql
/*
DELETE FROM 절 다음에 테이블 이름 작성
WHERE 절에서 삭제할 레코드를 지정하는 조건 작성
*/
DELETE FROM table_name
[WHERE
    condition];
```