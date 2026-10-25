CREATE DATABASE IF NOT EXISTS `products_suppliers`;

USE `products_suppliers`;

CREATE TABLE S
(
    `S#` CHAR(5) NOT NULL,
    SNAME CHAR(20) NOT NULL,
    STATUS SMALLINT NOT NULL,
    CITY CHAR(15) NOT NULL,
    PRIMARY KEY (`S#`)
);

INSERT INTO S (`S#`, SNAME, STATUS, CITY) VALUES
('S1', 'Smith', 20, 'London'),
('S2', 'Jones', 10, 'Paris'),
('S3', 'Blake', 30, 'Paris'),
('S4', 'Clark', 20, 'London'),
('S5', 'Adams', 30, 'Athens');

CREATE TABLE P
(
    `P#` CHAR(6) NOT NULL,
    PNAME CHAR(20) NOT NULL,
    COLOR CHAR(6) NOT NULL,
    WEIGHT SMALLINT NOT NULL,
    CITY CHAR(15) NOT NULL,
    PRIMARY KEY (`P#`)
);

INSERT INTO P (`P#`, PNAME, COLOR, WEIGHT, CITY) VALUES
('P1', 'Nut', 'Red', 12, 'London'),
('P2', 'Bolt', 'Green', 17, 'Paris'),
('P3', 'Screw', 'Blue', 17, 'Rome'),
('P4', 'Screw', 'Red', 14, 'London'),
('P5', 'Cam', 'Blue', 12, 'Paris'),
('P6', 'Cog', 'Red', 19, 'London');

CREATE TABLE SP
(
    `S#` CHAR(5) NOT NULL,
    `P#` CHAR(6) NOT NULL,
    QTY INTEGER NOT NULL,
    PRIMARY KEY (`S#`, `P#`),
    FOREIGN KEY (`S#`) REFERENCES S (`S#`),
    FOREIGN KEY (`P#`) REFERENCES P (`P#`)
);

INSERT INTO SP (`S#`, `P#`, QTY) VALUES
('S1', 'P1', 300),
('S1', 'P2', 200),
('S1', 'P3', 400),
('S1', 'P4', 200),
('S1', 'P5', 100),
('S1', 'P6', 100),
('S2', 'P1', 300),
('S2', 'P2', 400),
('S3', 'P2', 200),
('S4', 'P2', 200),
('S4', 'P4', 300),
('S4', 'P5', 400);

