CREATE DATABASE if not exists flaskdocker;
USE flaskdocker;

CREATE TABLE `flaskdocker`.`users` (
    `id` INT NOT NULL, 
    `name` VARCHAR(255),
    PRIMARY KEY(ID)
);

CREATE SEQUENCE seq_id
INCREMENT 1
MINVALUE 1
MAXVALUE 9999
START 1
CACHE 1;

ALTER TABLE users ALTER COLUMN id SET DEFAULT NEXTVAL("seq_id"::regclass);