-- SQL Modifying Data

-- 문제 1
CREATE TABLE users (
	userId INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100),
    country VARCHAR(100),
    email VARCHAR(100),
    created_at DATETIME DEFAULT NOW(),
    PRIMARY KEY (userId)
);

-- 문제 2
INSERT INTO 
    users (first_name, last_name, birthday, city, country, email)
VALUES 
    ("Beemo", "Jeong", "1000-01-01", "", "","beemo@hphk.kr"),
    ("Jieun", "Lee", "1993-05-16", "Seoul", "Korea", ""),
    ("Dami", "Kim",	"1995-04-09", "Seoul", "Korea", ""),
    ("Kwangsoo", "Lee",	"1985-07-14", "Seoul", "Korea", "");

-- 문제 3
INSERT INTO 
	users (first_name, last_name, birthday)
VALUES
	("first1", "last1", "1100-01-01"),
    ("first2", "last2", "1200-01-01"),
    ("first3", "last3", "1300-01-01"),
    ("first4", "last4", "1400-01-01"),
    ("first5", "last5", "1500-01-01");

-- 문제 4
UPDATE
	users
SET
	first_name = "Changjo",
    last_name = "Kim",
    birthday = "970802"
WHERE
	userId = 2;

-- 문제 5
UPDATE
	users
SET
	country = "Korea"
WHERE
	country IS NULL;

-- 문제 6
DELETE FROM
	users
WHERE
	first_name = "Beemo";

-- 문제 7
DELETE FROM
	users
WHERE
	first_name = "Kwangsoo"
    AND last_name = "Lee";

-- 문제 8
DELETE FROM
	users
ORDER BY
    userId DESC
LIMIT 1;