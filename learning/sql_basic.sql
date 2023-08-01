--------------------------------------------------------

-- 顯示資料庫
SHOW databases;

-- 建立資料庫
CREATE DATABASE <name>;

-- 刪除資料庫
DROP DATABASE <name>;

-- 切換使用資料庫
USE <name>;

-- 查看當前資料庫
SELECT database();

--------------------------------------------------------

-- 建立 table 範例
CREATE TABLE person (
  id INT AUTO_INCREMENT PRIMARY KEY
  name VARCHAR(20) NOT NULL DEFAULT "TEST NAME",
  phone VARCHAR(20) NOT NULL,
  age INT NOT NULL,
  email VARCHAR(64) NOT NULL UNIQUE KEY
);

-- 查看當前 database 所有 table
SHOW tables;

-- 展示 column 內容
SHOW COLUMNS FROM <table_name>;

-- 查看 table 內容
DESC <table_name>;

-- 刪除 table
DROP TABLE <table_name>;

--------------------------------------------------------

-- 插入單筆數據
INSERT INTO <table_name>(column1_name , column2_name) VALUES (column1_value, column2_vlaue);

-- 插入多筆數據
INSERT INTO <table_name>(column1_name, column2_name) VALUES (column1_value, column2_vlaue), (column1_value, column2_vlaue);

--------------------------------------------------------

-- 查看 table 數據
  SELECT * FROM <table_name>;

-- 查看特定內容
SELECT <column_name>, <column_name> FROM <table_name>;

-- 查看特定內容 - 更改別名
SELECT <column_name AS alias_column_name> FROM <table_name>;

-- 過濾數據
SELECT * FROM <table_name> WHERE <column_name=篩選內容> AND <column_name=篩選內容>;
SELECT * FROM <table_name> WHERE <column_name=篩選內容> OR <column_name=篩選內容>;
SELECT * FROM <table_name> WHERE <column_name=篩選內容> NOT <column_name=篩選內容>;
ex: SELECT * FROM employee WHERE title="Database Administrator";
ex: SELECT * FROM employee WHERE title="Database Administrator" AND salary=6000;
ex: SELECT * FROM employee WHERE title="Software Engineer" OR salary=6000;
ex: SELECT * FROM employee WHERE NOT title="Software Engineer";

-- 更新數據
UPDATE <table_name> SET <column_name=內容> WHERE <column_name=內容>;
ex: UPDATE employee SET salary=10000 WHERE title="Software Architect";
ex: UPDATE employee SET salary=20000, notes="update" WHERE title="Software Architect";

-- 刪除數據
DELETE FROM <table_name> WHERE <column_name=篩選內容> AND <column_name=篩選內容>;
DELETE FROM <table_name> WHERE <column_name=篩選內容> OR <column_name=篩選內容>;
DELETE FROM <table_name> WHERE <column_name=篩選內容> NOT <column_name=篩選內容>;
ex: DELETE FROM employee WHERE title="Software Architect";

--------------------------------------------------------

-- 字串相加
CONCAT("A", "B");
ex: SELECT CONCAT(first_name, ", ",last_name) AS full_name FROM employee;

-- 字串相加 - 間格符號
CONCAT_WS("-","A", "B");
ex: SELECT CONCAT_WS("-",first_name, last_name) AS full_name FROM employee;

-- 子串
SUBSTRING(<column_name>, <起始位置(包含)>, <終止位置(包含)>);
ex: SELECT SUBSTRING(title, 1, 5) FROM employee;

-- 替換字串
REPLACE(<字串>, <欲替換字串>, <替換的字串>);
ex: SELECT REPLACE("Hello World", "World", "MySQL");

-- 反轉字串
REVERSE(<字串>);
ex: SELECT REVERSE("Hello World");

-- 字串長度
CHAR_LENGTH(<字串>);
ex: SELECT CHAR_LENGTH("Hello World");

-- 字串大小寫轉換
UPPER(<字串>);
LOWER(<字串>);
ex: SELECT UPPER("Hello World");
ex: SELECT LOWER("Hello World");

--------------------------------------------------------

-- 排序
ORDER BY <column_name>, <column_name>;       -- 低到高
ORDER BY <column_name>, <column_name> DESC;  -- 高到低
ex: SELECT * FROM employee ORDER BY salary;
ex: SELECT first_name, last_name, salary FROM employee ORDER BY last_name, first_name;

-- 限制數量
LIMIT <number>;
LIMIT <number(起始), number(終止)>;
ex: SELECT * FROM employee ORDER BY salary LIMIT 3;
ex: SELECT * FROM employee ORDER BY salary LIMIT 2, 4;
ex: SELECT * FROM employee ORDER BY salary LIMIT 2, 18446744073709551615;

-- 模糊比對
LIKE <比對方式>
ex: SELECT * FROM employee WHERE last_name LIKE "C%"; -- 以 C 開頭的
ex: SELECT * FROM employee WHERE last_name LIKE "%i%"; -- 內容包含 i
ex: SELECT * FROM employee WHERE last_name LIKE "%n"; -- 以 n 結尾的
ex: SELECT * FROM employee WHERE last_name LIKE "__an"; -- 以 an 結尾的，且前面為長度 2
ex: SELECT * FROM employee WHERE last_name LIKE "____an"; -- 以 an 結尾的，且前面為長度 4
ex: SELECT * FROM employee WHERE last_name LIKE "J______"; -- 以 J 開頭，且後面為長度 6
SELECT * FROM employee WHERE last_name LIKE "%\%__"; -- 取 %__ 結尾，前面任意字符

--------------------------------------------------------