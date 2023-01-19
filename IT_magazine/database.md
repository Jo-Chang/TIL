# Database

<link rel="stylesheet" href="./assets/my_style.css">
-----

## 데이터베이스의 성질

-   무결성 : 데이터를 관리하는데 있어서 한치의 오차도 있어서는 안됨
-   속도 : 방대한 양의 데이터량을 가정해도 무조건 몇 초 이내에 처리가 완료되어야 함

-----

## Relational Database
-   관계형 데이터베이스 ( RDB, Relational Database ) : 테이블 간의 관계를 통해 데이터를 관리
    >   ex) 엑셀, MySQL, MariaDB, Oracle DB, SQL Server, ...
    
    | 엑셀 | RDB | 
    | --- | --- |
    | sheet | Table |
    | 엑셀 파일 | Schma / Database |
-   RDB를 조작하기 위해 **SQL**[^1] 이라는 언어를 사용하는 것과 같음

[^1] : SQL (Structured Query Language)

-----

## Big Data

### Data
-   수집
    +   웹 - 많은 정보 존재, 빅데이터를 <span>크롤링/스크레이핑</span>
    +   서비스 - 서비스 이용자들의 유입과 이탈 분석, <span>Google Analytics</span>

-   저장 / 분석
    +   DBMS ( Database Management System ) - 데이터 전처리[^1] ,설계, 저장
    >   MySQL, ORACLE Databse, Microsoft SQL Server, MariaDB, ...
    +   통계 / 확률 / 기계학습 - 데이터 분석

-   시각화
    +   Data Visualization - 데이터를 그래프로 표현하거나, 데이터의 어떤 숫자를 표시할지 연구

[^1]: 데이터 전처리 : 데이터를 개발자가 필요한 형태로 변환하는 과정, 오류 수정 포함