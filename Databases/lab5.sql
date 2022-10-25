use master;
go

-- создание базы 
if DB_ID (N'lab5') is not null
drop database lab5;
go

create database lab5
on (
NAME = lab5,
FILENAME = '/home/lab5.mdf',
SIZE = 10,
MAXSIZE = 30,
FILEGROWTH = 5
)
log on (
NAME = lab5log,
FILENAME = '/home/lab5log.log',
SIZE = 5,
MAXSIZE = 20,
FILEGROWTH = 5
);
go

-- создание таблицы

use lab5
go
if OBJECT_ID(N'Clients') is NOT NULL
	DROP Table Clients;
go

CREATE TABLE Clients
(
    client_email VARCHAR(100) PRIMARY KEY NOT NULL,
    phone VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100),
    birhtdate Date
);
go

INSERT INTO Clients
    (client_email, phone, name)
VALUES
    ('petya@mail.com', '88005553535', 'Petya')
go

select *
from Clients
go

-- создание фацловой группы и файла данных
alter database lab5
add filegroup lab5_fg
go

alter database lab5
add file(
	NAME = lab5dat,
	FILENAME = '/home/lab5dat.ndf',
	SIZE = 10MB,
	MAXSIZE = 100MB,
	FILEGROWTH = 5MB
)
to filegroup lab5_fg
go

-- назначение созданной файловой группы файловой группой по умолчанию

ALTER database lab5 
	MODIFY FILEGROUP lab5_fg DEFAULT
go

-- еще одна таблица

if OBJECT_ID(N'Products') is NOT NULL
	DROP Table Products;
go

CREATE TABLE Products
(
    product_id VARCHAR(100) PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL,
    weight_kg VARCHAR(100),
    price VARCHAR(100) NOT NULL,
    description VARCHAR(100)
);
go

alter database lab5
	modify filegroup [primary] default;
go

drop table Products
go

ALTER DATABASE lab5 
	REMOVE FILE lab5dat
go

alter database lab5
	REMOVE FILEGROUP lab5_fg
go

-- создаем схему 

CREATE SCHEMA zschema
go

ALTER SCHEMA zschema Transfer dbo.Clients
go

DROP TABLE zschema.Clients
DROP SCHEMA zschema
go