use master;
go

if DB_ID (N'lab6') is not null
drop database lab6;

create database lab6
on (
NAME = lab6dat,
FILENAME = '/home/lab6dat.mdf',
SIZE = 10,
MAXSIZE = 30,
FILEGROWTH = 5
)

log on (
NAME = lab6log,
FILENAME = '/home/lab6log.ldf',
SIZE = 5,
MAXSIZE = 20,
FILEGROWTH = 5
);
go

use lab6;
go
if OBJECT_ID(N'Orders',N'U') is NOT NULL
	DROP TABLE Orders;
go

CREATE TABLE Orders
(
    order_num_in_table int IDENTITY(1,1) NOT NULL,
    order_id Varchar(100) NOT NULL Primary KEY,
    creation_date date NOT NULL CHECK (creation_date <= (CONVERT(date,GETDATE()))),
    discount Numeric NOT NULL CHECK (discount > 0),
    payment_type Varchar(100) NOT NULL,
    payment_status Varchar(100) NOT NULL,
    status Varchar(100) NOT NULL DEFAULT 'new',

    CONSTRAINT checkCreationDate CHECK (creation_date > CONVERT(date,N'01-01-2000'))
);
go

INSERT INTO Orders
    (order_id, creation_date, discount, payment_type, payment_status)
VALUES
    ('Y-4567', CONVERT(date,N'10-25-2022'), 7, 'cache', 'not paid'),
    ('Y-4875', CONVERT(date,N'10-26-2022'), 7, 'cache', 'not paid'),
    ('Y-3578', CONVERT(date,N'10-27-2022'), 7, 'cache', 'not paid'),
    ('Y-4613', CONVERT(date,N'10-28-2022'), 7, 'cache', 'not paid')
go

SELECT COUNT(*)
FROM Orders
go


if OBJECT_ID(N'Products',N'U') is NOT NULL
	DROP TABLE Products;
go

CREATE TABLE Products
(
    product_id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT (NEWID()),
    name VARCHAR(100) NOT NULL,
    weight_kg VARCHAR(100),
    price VARCHAR(100) NOT NULL,
    description VARCHAR(100)
);
go

INSERT INTO Products
    (name, price, description)
VALUES
    (N'Пакет1', 10, N'нормальный пакет'),
    (N'Конверт1', 1000, N'хороший конверт')
go
INSERT INTO Products
    (product_id, name, price, description)
VALUES
    (NEWID(), N'Пакет2', 10, N'нормальный пакет'),
    (NEWID(), N'Конверт2', 1010, N'хороший конверт')
go

SELECT *
FROM Products
go



IF EXISTS (SELECT *
FROM sys.sequences
WHERE NAME = N'seq' AND TYPE='SO')
DROP SEQUENCE seq
go

CREATE SEQUENCE seq
	START WITH 1
	INCREMENT BY 1;
go


if OBJECT_ID(N'GrocerySoreList') is NOT NULL
	DROP Table GrocerySoreList;
go

CREATE TABLE GrocerySoreList
(
    nomer int PRIMARY KEY NOT NULL,
    product_name Varchar(100) NOT NULL,
);
go

INSERT INTO GrocerySoreList
    (nomer, product_name)
VALUES
    (NEXT VALUE FOR DBO.seq, 'grechka'),
    (NEXT VALUE FOR DBO.seq, 'hleb'),
    (NEXT VALUE FOR DBO.seq, 'moloko')
go

SELECT *
from GrocerySoreList
go



if OBJECT_ID(N'FK_Servers') is NOT NULL
    ALTER TABLE Clients DROP CONSTRAINT FK_Servers
if OBJECT_ID(N'Clients') is NOT NULL
	DROP Table Clients;
if OBJECT_ID(N'Servers') is NOT NULL
	DROP Table Servers;
go


CREATE TABLE Servers
(
    server_num int PRIMARY KEY NOT NULL,
    os VARCHAR(100) NOT NULL,
    ram NUMERIC NOT NULL,
    cpu VARCHAR(100) NOT NULL
)

INSERT INTO Servers
    (server_num, os, ram, cpu)
VALUES
    (1, 'buboontu', 4.5, 'intel core i10100500k'),
    (2, 'debibanan', 8, 'zeon3000')

CREATE TABLE Clients
(
    user_id int PRIMARY KEY NOT NULL,
    server_id int NOT NULL,
    name VARCHAR(100) NOT NULL

    CONSTRAINT FK_Servers FOREIGN KEY (server_id) REFERENCES Servers (server_num)
    ON DELETE CASCADE
)

INSERT INTO Clients
    (user_id, server_id, name)
VALUES
    (111, 1, 'Vasya'),
    (222, 2, 'Petya')
go

SELECT * from Clients
go 

-- DELETE FROM Servers
-- WHERE server_num=1
-- go

SELECT * FROM Clients
go
