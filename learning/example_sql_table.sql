create database demo;
use database demo;

create table employees (
  eid INT AUTO_INCREMENT PRIMARY KEY,
  birth_date DATE NOT NULL,
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  gender ENUM("M", "F") NOT NULL,
  hired_date DATE NOT NULL,
  email VARCHAR(64) NOT NULL UNIQUE KEY
);

insert into employees(
  birth_date,
  first_name,
  last_name,
  gender,
  hired_date,
  email
) values (
  "1994-09-05",
  "Yang Jie",
  "Su",
  "M",
  "2021-07-01",
  "BetaPhoenixSNSD@gmail.com"
);