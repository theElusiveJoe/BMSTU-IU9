wuse master;
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


CREATE TRIGGER t4
    ON OrdersView
    INSTEAD OF UPDATE
    AS 
    BEGIN
        PRINT 'helllol'
        UPDATE OrdersView
        SET status = 'was attemp to update by view'
        WHERE order_id  in (SELECT order_id FROM inserted)
    END 
GO
UPDATE OrdersView
SET status = 'new'
GO
SELECT * from Orders
GO 

CREATE TRIGGER t5
    ON OrdersView
    INSTEAD OF DELETE
    AS 
    BEGIN
        PRINT 'MSG: "u are not allowed to delete via view"'
    END 
GO
DELETE FROM OrdersView
GO 

CREATE TRIGGER t6
    ON OrdersView
    INSTEAD OF INSERT
    AS 
    BEGIN
        INSERT INTO OrdersView
        (order_id, creation_date, discount, payment_type, payment_status)
        SELECT order_id, creation_date, discount, payment_type, payment_status FROM inserted WHERE discount > 5
    END 
GO

INSERT INTO OrdersView
    (order_id, creation_date, discount, payment_type, payment_status)
VALUES
    ('Y-11111', CONVERT(date,N'10-27-2022'), 7, 'cache', 'not paid'),
    ('Y-22222', CONVERT(date,N'10-28-2022'), 0, 'cache', 'not paid')
GO
SELECT * from OrdersView
GO 
