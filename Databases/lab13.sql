use master
go

DROP DATABASE IF EXISTS lab131
GO
DROP DATABASE IF EXISTS lab132
GO

create database lab131
on (
NAME = lab131,
FILENAME = '/home/lab131.mdf',
SIZE = 10,
MAXSIZE = 30,
FILEGROWTH = 5
)
log on (
NAME = lab131log,
    FILENAME = '/home/lab131log.log',
SIZE = 5,
MAXSIZE = 20,
FILEGROWTH = 5
);
go

create database lab132
on (
NAME = lab132,
FILENAME = '/home/lab132.mdf',
SIZE = 10,
MAXSIZE = 30,
FILEGROWTH = 5
)
log on (
NAME = lab132log,
FILENAME = '/home/lab132log.log',
SIZE = 5,
MAXSIZE = 20,
FILEGROWTH = 5
);
go



-- Создать в базах данных п.1. горизонтально
-- фрагментированные таблицы.
USE lab131
GO

DROP TABLE IF EXISTS Orders
GO
CREATE TABLE Orders(
    order_id INT NOT NULL Primary KEY CHECK (order_id <= 3),
    -- creation_date date NOT NULL CHECK (creation_date <= (CONVERT(date,GETDATE()))),
    discount Numeric NOT NULL DEFAULT 0,
    -- payment_type VARCHAR(100) NOT NULL,
    -- payment_status VARCHAR(100) NOT NULL,
    status VARCHAR(100) NOT NULL DEFAULT 'new',
	-- delivery_date date NOT NULL DEFAULT CONVERT(date,GETDATE()),
	-- delivery_service_status VARCHAR(100) NOT NULL DEFAULT 'new',
	-- delivery_address VARCHAR(100) NOT NULL,
	client_email VARCHAR(100) NOT NULL,
);
GO

DROP TRIGGER IF EXISTS upd1;
DROP TRIGGER IF EXISTS ins1;
GO 

CREATE TRIGGER upd1 ON Orders
AFTER UPDATE AS
    BEGIN 
        IF UPDATE(order_id) 
            THROW 50002, 'u cant update order_id',1
        IF (EXISTS (SELECT * FROM inserted as i JOIN lab132.dbo.Orders as o2 ON i.order_id = o2.order_id))
            THROW 50001, 'such order already exists',1
    END
GO

CREATE TRIGGER ins1 ON Orders
AFTER INSERT AS
    BEGIN
        IF (EXISTS (SELECT * FROM inserted as i JOIN lab132.dbo.Orders as o2 ON i.order_id = o2.order_id))
            BEGIN 
                ROLLBACK TRANSACTION;
                THROW 50001, 'such order already exists',1
            END
    END
GO

USE lab132
GO

DROP TABLE IF EXISTS Orders
GO
CREATE TABLE Orders(
    order_id INT NOT NULL Primary KEY CHECK (order_id > 3),
    -- creation_date date NOT NULL CHECK (creation_date <= (CONVERT(date,GETDATE()))),
    discount Numeric NOT NULL DEFAULT 0,
    -- payment_type VARCHAR(100) NOT NULL,
    -- payment_status VARCHAR(100) NOT NULL,
    status VARCHAR(100) NOT NULL DEFAULT 'new',
	-- delivery_date date NOT NULL DEFAULT CONVERT(date,GETDATE()),
	-- delivery_service_status VARCHAR(100) NOT NULL DEFAULT 'new',
	-- delivery_address VARCHAR(100) NOT NULL,
	client_email VARCHAR(100) NOT NULL,
);
GO

DROP TRIGGER IF EXISTS upd1;
DROP TRIGGER IF EXISTS ins1;
GO 

CREATE TRIGGER upd1 ON Orders
AFTER UPDATE AS
    BEGIN
        IF UPDATE(order_id) 
            THROW 50002, 'u cant update order_id',1
        IF (EXISTS (SELECT * FROM inserted as i JOIN lab131.dbo.Orders as o1 ON i.order_id = o1.order_id))
            BEGIN 
                ROLLBACK TRANSACTION;
                THROW 50001, 'such order already exists',1
            END
    END
GO

CREATE TRIGGER ins1 ON Orders
AFTER INSERT AS
    BEGIN
        IF (EXISTS (SELECT * FROM inserted as i JOIN lab131.dbo.Orders as o1 ON i.order_id = o1.order_id))
            THROW 50001, 'such order already exists',1
    END
GO


USE lab131
GO

DROP VIEW IF EXISTS myview
GO
CREATE VIEW myview AS
SELECT * FROM lab131.dbo.Orders UNION ALL SELECT * FROM lab132.dbo.Orders
GO

USE lab132
GO

DROP VIEW IF EXISTS myview
GO
CREATE VIEW myview AS
SELECT * FROM lab131.dbo.Orders UNION ALL SELECT * FROM lab132.dbo.Orders
GO

INSERT INTO myview
VALUES
(6, 0, 'new', '@6'),
(5, 0, 'new', '@5'),
(4, 0, 'new', '@4'),
(3, 0, 'new', '@3'),
(7, 0, 'new', '@2'),
(1, 0, 'new', '@1')
GO

SELECT * FROM myview
SELECT * FROM lab131.dbo.Orders
SELECT * FROM lab132.dbo.Orders


DELETE FROM myview WHERE order_id = 7
GO
UPDATE myview SET order_id = 2 WHERE order_id = 6
GO
UPDATE myview SET status = 'ready to assemble' WHERE order_id = 6
GO

SELECT * FROM myview
SELECT * FROM lab131.dbo.Orders
SELECT * FROM lab132.dbo.Orders