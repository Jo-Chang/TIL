# Week09-1

-   Transactions, Triggers


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">


<br>[Parent Contents...](../../README.md/#til-today-i-learned)

-----

## Transactions

-   Transaction : 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법
    +   All or Nothing
    >   계좌 이체, ...

-   Transaction Syntax
    ```sql
    START TRANSACTION;
    state_ments;
    ...
    [ROLLBACK|COMMIT];
    /*
    START TRANSACTION : 트랜잭션 구문의 시작
    COMMIT : 모든 작업이 정상적으로 완료되면 한꺼번에 DB에 반영
    ROLLBACK : 부분적으로 작업이 실패하면 트랜잭션에서 진행한 모든 연산을 취소하고 트랜잭션 실행 전으로 되돌림
    */
    ```

-   쪼개질 수 없는 업무처리의 단위


-----


## Triggers

-   Triggers : 특정 이벤트에 대한 응답으로 자동으로 실행되는 것
    +   INSERT, UPDATE, DELETE

    ```sql
    CREATE TRIGGER trigger_name
        {BEFORE | AFTER} {INSERT | UPDATE | DELETE}
        ON table_name FOR EACH ROW
        trigger_body;
    /*
    CREATE TRIGGER 키워드 다음에 생성하려는 트리거의 이름을 지정
    각 레코드의 어느 시점에 트리거가 실행될지 지정(삽입, 수정, 삭제 전/후)
    ON 키워드 뒤에 트리거가 속한 테이블의 이름을 지정
    트리거가 활성화될 때 실행할 코드를 trigger_body에 지정
        - 여러 명령문을 실행하려면 begin end 키워드로 묶어서 사용
    */
    ```

-   OLD/NEW : 트리거에서 특정 시점 전/후의 값에 접근 할 수 있도록 제공하는 키워드

||OLD|NEW|
|---|---|---|
|INSERT|NO|YES|
|UPDATE|YES|YES|
|DELETE|YES|NO|

## Tips

-   Transaction 생성시 에러
    +   `Error Code:2013. Lost connection to MySQL server during query`
    +   `Error Code:2015. Lock wait timeout exceeded; try restarting transaction`

    ```sql
    -- 실행중인 프로세스 목록 확인
    SELECT * FROM information_schma.INNODB_TRX;

    -- 특정 프로세스의 trx_mysql_thread_id 삭제
    KILL [try_mysql_thread_id1];
    ```