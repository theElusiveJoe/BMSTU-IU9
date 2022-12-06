use master;
go

DROP DATABASE IF EXISTS lab9

CREATE DATABASE lab9
on (
	NAME = lab9dat,
	FILENAME = '/home/lab9dat.mdf',
	SIZE = 10,
	MAXSIZE = UNLIMITED,
	FILEGROWTH = 5
)
log on (
	NAME = lab9log,
	FILENAME = '/home/lab9log.ldf',
	SIZE = 5,
	MAXSIZE = 20,
	FILEGROWTH = 5
);
go 

use lab9;
go 

DROP TABLE if EXISTS Orders
DROP VIEW IF EXISTS OrdersView
DROP TRIGGER IF EXISTS t1
DROP TRIGGER IF EXISTS t2
DROP TRIGGER IF EXISTS t3
DROP TRIGGER IF EXISTS t4
DROP TRIGGER IF EXISTS t5
DROP TRIGGER IF EXISTS t6
go

CREATE TABLE Orders
(
    order_num_in_table int IDENTITY(1,1) NOT NULL,
    order_id Varchar(100) NOT NULL Primary KEY,
    creation_date date NOT NULL CHECK (creation_date <= (CONVERT(date,GETDATE()))),
    discount Numeric NOT NULL CHECK (discount >= 0),
    payment_type Varchar(100) NOT NULL,
    payment_status Varchar(100) NOT NULL,
    status Varchar(100) NOT NULL DEFAULT 'new',

    CONSTRAINT checkCreationDate CHECK (creation_date > CONVERT(date,N'01-01-2000'))
);
go 

CREATE VIEW OrdersView AS
    SELECT * 
    FROM Orders
    WHERE Orders.creation_date >= CONVERT(date,N'10-27-2022')
go 

-- 1. Для одной из таблиц пункта 2 задания 7 создать
-- триггеры на вставку, удаление и добавление, при
-- выполнении заданных условий один из триггеров
-- должен инициировать возникновение ошибки
-- (RAISERROR / THROW).

-- 1. INSERT TRIGGER
INSERT INTO Orders
    (order_id, creation_date, discount, payment_type, payment_status)
VALUES
    ('Y-4567', CONVERT(date,N'10-25-2022'), 2, 'cache', 'paid'),
    ('Y-4875', CONVERT(date,N'10-26-2021'), 3, 'cache', 'not paid')
go 

CREATE TRIGGER t1 
    ON Orders 
    AFTER INSERT
    AS 
    BEGIN
        UPDATE Orders
        SET discount = 5
        WHERE order_id  in (SELECT inserted.order_id FROM inserted WHERE inserted.discount < 5)
    END 
GO

INSERT INTO Orders
    (order_id, creation_date, discount, payment_type, payment_status)
VALUES
    ('Y-3578', CONVERT(date,N'10-27-2022'), 1, 'cache', 'not paid'),
    ('Y-4613', CONVERT(date,N'10-28-2022'), 0, 'cache', 'not paid')
go

SELECT * FROM Orders
GO

-- 2. UPDATE TRIGGER
CREATE TRIGGER t2
    ON Orders
    AFTER UPDATE
    AS 
    BEGIN
        DELETE Orders
        WHERE creation_date < DATEADD(DAY, -200,  CONVERT(date,GETDATE()))
    END 
GO


UPDATE Orders
SET [status] = 'not new'

SELECT * FROM Orders
GO 

-- 3. Delete Trigger
CREATE TRIGGER t3
    ON Orders
    INSTEAD OF  DELETE
    AS 
    if (SELECT COUNT(*) FROM Orders WHERE payment_status = 'paid') > 0
        RAISERROR('U cant delete paid order', 1, 1)
    else 
        DELETE FROM Orders WHERE order_id in (SELECT order_id FROM deleted)
GO 

DELETE FROM Orders
GO

SELECT * FROM Orders
GO 



-- 2. Для представления пункта 2 задания 7 создать
-- триггеры на вставку, удаление и добавление,
-- обеспечивающие возможность выполнения
-- операций с данными непосредственно через
-- представление.


if OBJECT_ID(N'FK_Servers') is NOT NULL
    ALTER TABLE Clients DROP CONSTRAINT FK_Servers
if OBJECT_ID(N'Clients') is NOT NULL
	DROP Table Clients;
if OBJECT_ID(N'Servers') is NOT NULL
	DROP Table Servers;
DROP VIEW IF EXISTS cs_view 
go


CREATE TABLE Servers
(
    server_id int PRIMARY KEY NOT NULL,
    os VARCHAR(100) NOT NULL,
    ram NUMERIC NOT NULL,
    cpu VARCHAR(100) NOT NULL
)

INSERT INTO Servers
    (server_id, os, ram, cpu)
VALUES
    (1, 'buboontu', 4.5, 'intel core i10100500k'),
    (2, 'debibanan', 8, 'zeon3000')

CREATE TABLE Clients
(
    user_id int PRIMARY KEY NOT NULL,
    server_id int NOT NULL,
    name VARCHAR(100) NOT NULL

    CONSTRAINT FK_Servers UNIQUE FOREIGN KEY (server_id) REFERENCES Servers (server_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)

INSERT INTO Clients
    (user_id, server_id, name)
VALUES
    (111, 1, 'Vasya'),
    (222, 2, 'Petya')
go


CREATE View cs_view AS
    SELECT s.server_id as server_id, s.os as os, s.ram as ram, s.cpu as cpu, c.name as name, c.user_id as user_id
    FROM Servers as s INNER JOIN Clients as c on s.server_id = c.server_id
go

SELECT * FROM cs_view
go



-- 1. INSERT TRIGGER
CREATE TRIGGER t4 ON cs_view INSTEAD OF INSERT
AS 
    BEGIN 
        IF (
            ((SELECT COUNT(*) FROM inserted INNER JOIN Servers on Servers.server_id = inserted.server_id) > 0)
            OR ((SELECT COUNT(*) FROM inserted INNER JOIN Clients on Clients.user_id = inserted.user_id) > 0))
        RAISERROR('Such sever or user already exists', 18, 1)
        ELSE
        BEGIN
            INSERT INTO Servers(server_id, os, ram, cpu)
            SELECT server_id, os, ram, cpu FROM inserted

            INSERT INTO Clients(name, user_id, server_id)
            SELECT name, user_id, server_id FROM inserted
        END
    END
go

INSERT INTO cs_view(server_id, os, ram, cpu, name, user_id)
VALUES (3, 'okoshki', 2, 'radeon', 'Sasha', 333)
go

INSERT INTO cs_view(server_id, os, ram, cpu, name, user_id)
VALUES (3, 'fail insert', 2, 'fail insert', 'fail insert', 0)
go
INSERT INTO cs_view(server_id, os, ram, cpu, name, user_id)
VALUES (34, 'fail insert', 2, 'fail insert', 'fail insert', 333)
go

SELECT * FROM cs_view
go

-- 2. UPDATE TRIGGER
CREATE TRIGGER t5 ON cs_view INSTEAD OF UPDATE
AS 
BEGIN
    IF UPDATE(server_id) RAISERROR('U cant update server id', 18, 1)
    ELSE
    BEGIN 
        UPDATE Clients SET Clients.user_id = inserted.user_id, Clients.name = inserted.name FROM inserted WHERE inserted.user_id = Clients.user_id
        UPDATE Servers SET Servers.os = inserted.os, Servers.ram = inserted.ram, Servers.cpu = inserted.cpu FROM inserted WHERE inserted.server_id = Servers.server_id
    END
END
go 

UPDATE cs_view set name = 'VASYA2' where server_id = 1
UPDATE cs_view set ram = 1000 where user_id = 111
go
UPDATE cs_view set os = 'NEWOS2' where server_id = 1
UPDATE cs_view set server_id = 222 where server_id = 2
go

SELECT * FROM cs_view
go 

-- 3. DELETE TRIGGER
CREATE TRIGGER t6 ON cs_view INSTEAD OF DELETE
AS 
BEGIN
    DELETE from Servers WHERE Servers.server_id in (SELECT server_id FROM deleted)
END
go 

DELETE FROM cs_view WHERE server_id = 2
SELECT * from cs_view
SELECT * from Clients