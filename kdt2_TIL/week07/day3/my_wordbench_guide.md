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