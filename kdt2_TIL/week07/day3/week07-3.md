# Week07-3

-   Database


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

-----

<br>[Parent Contents...](../../README.md/#til-today-i-learned)

## Contents
- [sample](#sample)

<br>

-----


## Why Database

-   정보, 데이터 ( Data ) : <span>저장</span>이나 <span>처리</span>에 효율적인 형태로 변환된 정보 (information)
-   너무 많은 데이터양을 다룰 도구 필요
-   CRUD
    +   Create 저장
    +   Read 조회
    +   Update 갱신
    +   Delete 삭제

-----


## Relational Database

-   관계형 데이터베이스 : 데이터 간에 <span>관계</span>가 있는 데이터 항목들의 모음
-   테이블, 행, 열의 정보를 구조화하는 방식
-   용어
    +   Table (=Relation)
    :   데이터를 기록하는 위치, 표나 엑셀 시트
    +   Field (=Column, Attribute)
    :   동일한 속성, 형식을 가진 데이터들
    +   Record (=Row, Tuple)
    :   한 객체가 나타내는 데이터 값들의 집합 = 한 객체
    +   Database (=Schema)
    :   테이블들의 집합
    +   Primary Key (기본 키)
    :   각 객체의 고유값, RDB에서는 <span>객체의 식별자</span>로 활용
    +   Foreign Key (외래 키)
    :   테이블에서 다른 테이블의 객체를 구분할 수 있는 값, 다른 테이블 간 <span>관계 생성</span>에 활용

### RDBMS

-   관계형 데이터베이스 관리 시스템 ( Relational Database Management System )
    <br>:   관계형 데이터베이스를 관리하는 소프트웨어 프로그램
>   mySQL, mariaDB, ...


-----


# My Workbench Guide

## Access

1.  메인 화면에서 접속을 원하는 데이터베이스를 클릭
2.  접속 창에서 비밀번호를 입력하고 DB 접속
3.  새로 나온 쿼리 창에 쿼리 명령문 입력


## 쿼리문 작성 및 실행

1.  데이터 베이스를 import, 없으면 생성한다.
    +   1-1. Use : 데이터베이스 선택

    ```sql
    Use {Database name};
    ```

    +   1-2. CREATE : 테이블 생성 

    ```sql
    CREATE TABLE {Table name}(
        {Field1} {FieldType}, 
        {Field2 {FieldType}, ...}
        );
    ```

    +   1-3. INSERT : 테이블에 데이터 삽입 

    ```sql
    INSERT INTO {Table name}({Field1}, {Field2}, ...);
    ```

2.  테이블에서 원하는 작업을 진행하기 위한 쿼리문 작성

    +   SELECT  : 테이블로부터 데이터 열람

    ```sql
    SELECT * FROM {Table name}
    ```

    +   UPDATE  : 데이터 수정

    ```sql
    UPDATE {Table name} SET {Field name} = {Update value}
    ```

    +   DELETE  : 데이터 삭제

    ```sql
    DELETE FROM {Table name}
    ```

    +   WHERE   : 원하는 데이터만 접근하기 위한 조건절

    ```sql
    SELECT * FROM {Table name} WHERE {Condition}

    UPDATE {Table name} SET {Field name} = {Update value} WHERE {Condition}

    DELETE FROM {Table name} WHERE {Condition}
    ```