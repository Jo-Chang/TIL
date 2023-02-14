-- CREATE TABLE examples
CREATE TABLE examples (
    examId INT AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    PRIMARY KEY (examId)
);

--  Table 구조 확인
SHOW COLUMNS FROM examples;

-- DROP TABLE examples
DROP TABLE examples;

--  ALTER TABLE ADD #1
ALTER TABLE 
    examples
ADD
    country VARCHAR(100) NOT NULL;

--  ALTER TABLE ADD #2
ALTER TABLE examples
ADD age INT NOT NULL,
ADD address VARCHAR(100) NOT NULL;
/*
ADD (age INT NOT NULL, address VARCHAR(100) NOT NULL)
*/

-- ALTER TABLE MODIFY #1
ALTER TABLE
    examples
MODIFY
    address VARCHAR(50) NOT NULL;

-- ALTER TABLE MODIFY #2
ALTER TABLE examples
MODIFY lastName VARCHAR(10) NOT NULL,
MODIFY firstName VARCHAR(10) NOT NULL;

-- ALTER TABLE CHANGE COLUMN #1
ALTER TABLE 
    examples 
CHANGE COLUMN
    country state VARCHAR(100) NOT NULL;

-- ALTER TABLE DROP COLUMN #1
ALTER TABLE 
    examples 
DROP COLUMN
    address;

-- ALTER TABLE DROP COLUMN #2
ALTER TABLE 
    examples 
DROP COLUMN state,
DROP COLUMN age;

-- INSERT #1
INSERT INTO articles (title, content, createdAt)
VALUES ("hello", "world", "2000-01-01");

-- INSERT #2
INSERT INTO 
    articles (title, content, createdAt)
VALUES 
    ("title1", "content1", "1900-01-01"),
    ("title2", "content2", "1800-01-01"),
    ("title3", "content3", "1700-01-01");

-- INSERT #3
INSERT INTO articles (title, content, createdAt)
VALUES ("hello", "world", CURDATE());
/* 
현재 날짜를 반환 - CURDATE()
현재 시간을 반환 - CURTIME()
현재 날짜와 시간을 반환 - NOW() 
*/

-- UPDATE #1
UPDATE 
    articles
SET 
    title = "newTitle"
WHERE 
    id = 1;

-- UPDATE #2
UPDATE 
    articles
SET 
    title = "newTitle2",
    content = "newContent2"
WHERE 
    id = 2;

-- UPDATE #3
UPDATE
    articles
SET 
    content = REPLACE(content, "content", "TEST");

-- DELETE #1
DELETE FROM 
    articles 
WHERE 
    id = 1;

-- DELETE #2
DELETE FROM 
    articles
ORDER BY
    createdAt DESC
LIMIT 2;