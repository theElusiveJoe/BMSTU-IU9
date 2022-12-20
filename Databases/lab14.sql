use master
go

DROP DATABASE IF EXISTS lab141
GO
DROP DATABASE IF EXISTS lab142
GO

create database lab141
on (
NAME = lab141,
FILENAME = '/home/lab141.mdf',
SIZE = 10,
MAXSIZE = 30,
FILEGROWTH = 5
)
log on (
NAME = lab141log,
    FILENAME = '/home/lab141log.log',
SIZE = 5,
MAXSIZE = 20,
FILEGROWTH = 5
);
go

create database lab142
on (
NAME = lab142,
FILENAME = '/home/lab142.mdf',
SIZE = 10,
MAXSIZE = 30,
FILEGROWTH = 5
)
log on (
NAME = lab142log,
FILENAME = '/home/lab142log.log',
SIZE = 5,
MAXSIZE = 20,
FILEGROWTH = 5
);
go

USE lab141
GO

DROP TABLE IF EXISTS Orders
GO
CREATE TABLE Orders(
    order_id INT NOT NULL Primary KEY,
    -- creation_date date NOT NULL CHECK (creation_date <= (CONVERT(date,GETDATE()))),
    -- discount Numeric NOT NULL DEFAULT 0,
    -- payment_type VARCHAR(100) NOT NULL,
    -- payment_status VARCHAR(100) NOT NULL,
    -- status VARCHAR(100) NOT NULL DEFAULT 'new',
	-- delivery_date date NOT NULL DEFAULT CONVERT(date,GETDATE()),
	-- delivery_service_status VARCHAR(100) NOT NULL DEFAULT 'new',
	-- delivery_address VARCHAR(100) NOT NULL,
	client_email VARCHAR(100) NOT NULL
);
GO

USE lab142
GO

DROP TABLE IF EXISTS Orders
GO
CREATE TABLE Orders(
    order_id INT NOT NULL Primary KEY,
    -- creation_date date NOT NULL CHECK (creation_date <= (CONVERT(date,GETDATE()))),
    discount Numeric NOT NULL DEFAULT 0,
    -- payment_type VARCHAR(100) NOT NULL,
    -- payment_status VARCHAR(100) NOT NULL,
    status VARCHAR(100) NOT NULL DEFAULT 'new',
	-- delivery_date date NOT NULL DEFAULT CONVERT(date,GETDATE()),
	-- delivery_service_status VARCHAR(100) NOT NULL DEFAULT 'new',
	-- delivery_address VARCHAR(100) NOT NULL,
	-- client_email VARCHAR(100) NOT NULL,
);
GO

DROP TRIGGER IF EXISTS ins
DROP TRIGGER IF EXISTS upd
DROP TRIGGER IF EXISTS del
DROP VIEW IF EXISTS myview
GO

CREATE VIEW myview AS
    SELECT o1.order_id, o2.discount , o2.status, o1.client_email FROM lab141.dbo.Orders AS o1
    INNER JOIN lab142.dbo.Orders AS o2 
    ON o1.order_id = o2.order_id
GO

CREATE TRIGGER ins ON myview 
INSTEAD OF INSERT
AS
    INSERT INTO lab141.dbo.Orders(order_id, client_email)
    SELECT order_id, client_email FROM inserted

    INSERT INTO lab142.dbo.Orders(order_id, discount, status)
    SELECT order_id, discount, status FROM inserted
GO

CREATE TRIGGER upd ON myview 
INSTEAD OF UPDATE
AS
    UPDATE lab141.dbo.Orders
    SET order_id = inserted.order_id, client_email = inserted.client_email
    FROM inserted 
    WHERE lab141.dbo.Orders.order_id = inserted.order_id

    UPDATE lab142.dbo.Orders
    SET order_id = inserted.order_id, discount = inserted.discount, status = inserted.status
    FROM inserted 
    WHERE lab142.dbo.Orders.order_id = inserted.order_id
GO

CREATE TRIGGER del ON myview 
INSTEAD OF DELETE
AS
    DELETE FROM lab141.dbo.Orders WHERE order_id IN (SELECT order_id FROM deleted)
    DELETE FROM lab142.dbo.Orders WHERE order_id IN (SELECT order_id FROM deleted)
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