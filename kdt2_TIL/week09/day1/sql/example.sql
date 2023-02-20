-- Prepare for transaction
-- 자동 COMMIT 비활성화
SET autocommit = 0;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

-- Transaction #1
START TRANSACTION;

INSERT INTO users (name)
VALUES ('harry'), ('test');

SELECT * FROM users;

ROLLBACK;
-- COMMIT;

SELECT * FROM users;


-- Prepare for trigger
DROP TABLE IF EXISTS articles;
CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    -- createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title1', CURRENT_TIME(), CURRENT_TIME());

CREATE TABLE articleLogs (
	id INT AUTO_INCREMENT,
    description VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

-- Trigger #1
-- DELIMITER ';' 구문문자 대체
DELIMITER //
CREATE TRIGGER beforeArticleUpdate
	BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
	SET NEW.updatedAt = CURRENT_TIME();
END//
DELIMITER ;

-- Trigger #2
DELIMITER //
CREATE TRIGGER recordLogs
    AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
    INSERT INTO articleLogs (description, createdAt)
    VALUES ("글이 작성 되었습니다.", CURRENT_TIME());
END//
DELIMITER ;

-- Trigger #2-1
DROP TRIGGER IF EXISTS recordLogs;
DELIMITER //
CREATE TRIGGER recordLogs
    AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
    INSERT INTO articleLogs (description, createdAt)
    VALUES (CONCAT(NEW.id, "번 글이 작성 되었습니다."), CURRENT_DATE());
END//
DELIMITER ;

-- Trigger #3
DELIMITER //
CREATE TRIGGER backupLogs 
	AFTER DELETE
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO backupArticles (title, createdAt, updatedAt)
    VALUES (OLD.title, OLD.createdAt, OLD.updatedAT);
END//
DELIMITER ;