use master;
go

DROP DATABASE IF EXISTS lab11
go

CREATE DATABASE lab11
on (
	NAME = lab11dat,
	FILENAME = '/home/lab11dat.mdf',
	SIZE = 11,
	MAXSIZE = UNLIMITED,
	FILEGROWTH = 5
)
log on (
	NAME = lab11log,
	FILENAME = '/home/lab11log.ldf',
	SIZE = 5,
	MAXSIZE = 20,
	FILEGROWTH = 5
);
go 

use lab11;
go 

-- СОЗДАЕМ ТАБЛИЦЫ

IF EXISTS(
	SELECT table_name FROM INFORMATION_SCHEMA.TABLES 
		WHERE table_schema = 'lab11'AND table_name = 'Orders'
)
	ALTER TABLE  Orders DROP CONSTRAINT IF EXISTS FK_email

IF EXISTS(
	SELECT table_name FROM INFORMATION_SCHEMA.TABLES 
		WHERE table_schema = 'lab11'AND table_name = 'Packages'
)
	ALTER TABLE  Orders DROP CONSTRAINT IF EXISTS FK_pack

IF EXISTS(
	SELECT table_name FROM INFORMATION_SCHEMA.TABLES 
		WHERE table_schema = 'lab11'AND table_name = 'Orders_item'
)
	ALTER TABLE  Orders DROP CONSTRAINT IF EXISTS FK_item1, FK_item2

DROP TRIGGER IF EXISTS client_del

DROP TABLE if EXISTS Orders
DROP TABLE if EXISTS Clients
DROP TABLE if EXISTS Products
DROP TABLE if EXISTS Order_items
go 

-------------------------ТАБЛИЦЫ

CREATE TABLE Clients(
	client_email VARCHAR(100) NOT NULL PRIMARY KEY,
	phone VARCHAR(100) NOT NULL,
	name VARCHAR(100) NOT NULL,
	surname VARCHAR(100),
	birthdate date,
);

CREATE TABLE Orders(
    order_id VARCHAR(100) NOT NULL Primary KEY,
    creation_date date NOT NULL CHECK (creation_date <= (CONVERT(date,GETDATE()))),
    discount Numeric NOT NULL DEFAULT 0 CHECK (discount >= 0),
    -- payment_type VARCHAR(100) NOT NULL,
    -- payment_status VARCHAR(100) NOT NULL,
    status VARCHAR(100) NOT NULL DEFAULT 'new',
	-- delivery_date date NOT NULL,
	-- delivery_service_status VARCHAR(100) NOT NULL DEFAULT 'new',
	-- delivery_address VARCHAR(100) NOT NULL,
	client_email VARCHAR(100) NOT NULL,

	CONSTRAINT FK_email 
	FOREIGN KEY (client_email) 
	REFERENCES Clients (client_email) 
	ON UPDATE CASCADE,

    CONSTRAINT checkCreationDate CHECK (creation_date > CONVERT(date,N'01-01-2000'))
);

CREATE TABLE Products(
	product_id VARCHAR(100) PRIMARY KEY NOT NULL,
	name VARCHAR(100) NOT NULL,
	weight_kg NUMERIC, 
	price NUMERIC NOT NULL,
	description VARCHAR(100)
)

CREATE TABLE Packages (	
	-- table_synthetic_key int IDENTITY(1,1) PRIMARY KEY NOT NULL,
	order_id VARCHAR(100) NOT NULL,
	num int IDENTITY(1,1) NOT NULL PRIMARY KEY,
	weight_kg NUMERIC NOT NULL DEFAULT 100500,
	dim_x_m NUMERIC NOT NULL DEFAULT 100500, 

	UNIQUE(order_id, num),

	CONSTRAINT FK_pack 
	FOREIGN KEY (order_id) 
	REFERENCES Orders(order_id)
	ON UPDATE CASCADE
	ON DELETE CASCADE,
)

CREATE TABLE Order_items(
	table_synthetic_key int IDENTITY(1,1) PRIMARY KEY NOT NULL,
	order_id VARCHAR(100) NOT NULL FOREIGN KEY REFERENCES Orders(order_id),
	product_id VARCHAR(100) NOT NULL,
	PRICE NUMERIC NOT NULL,
	QUANTITY INTEGER NOT NULL,

	UNIQUE(order_id, product_id),

	CONSTRAINT FK_item1 FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT FK_item2 FOREIGN KEY (product_id) REFERENCES Products(product_id) ON UPDATE CASCADE,
)

go

-------------------------ТРИГГЕРЫ

CREATE TRIGGER client_del ON Clients 
    INSTEAD OF DELETE
    AS THROW 50000, 'u cant delete a client', 1
go

CREATE TRIGGER prod_del ON Products 
    INSTEAD OF DELETE
	AS
	IF ((SELECT COUNT(*) FROM Order_items INNER JOIN deleted on deleted.product_id = Order_items.product_id) <> 0)
    	THROW 50000, 'u cant delete product that is in some order', 1
		
go

-- CREATE TRIGGER client_del ON Clients 
--     INSTEAD OF DELETE
--     AS THROW 50000, 'u cant delete a client', 1
-- go

-------------------------ДОБАВИМ ЧТО_НИБУДЬ

INSERT INTO Clients (client_email, phone, name)
VALUES	
	('@1', '89999999999', 'Petya'),
	('@2', '88888888888', 'Vasya')

INSERT INTO Orders (order_id, creation_date, client_email)
VALUES  
	('order1', CONVERT(date,N'10-25-2022'), '@1'), 
	('order2', CONVERT(date,N'10-25-2022'), '@1')

INSERT INTO Packages (order_id)
VALUES 
	('order1'),
	('order1'),
	('order2'),
	('order2')

INSERT INTO Products (product_id, name, price)
VALUES 
	('prid1', 'tovar1', 1111),
	('prid2', 'tovar2', 2222)

INSERT INTO Order_items (order_id, product_id, quantity, price)
VALUES
	('order1', 'prid1', 10, 1700)

-------------------------ТЕСТИРУЕМ

SELECT * FROM Order_items
-- UPDATE Orders SET order_id = 'ordernew' WHERE order_id = 'order1'
DELETE FROM Orders
SELECT * FROM Order_items

-- UPDATE Packages SET order_id = 'ordernew' WHERE order_id = 'order1' 
-- DELETE FROM Orders
-- SELECT * FROM Packages
-- SELECT * FROM Clients


-- SELECT * FROM Clients
-- UPDATE Clients SET client_email = '@new' WHERE client_email = '@1'
-- SELECT * FROM Orders

-- UPDATE Orders SET client_email = '@new2' WHERE client_email = '@1' or client_email = '@new'
-- SELECT * FROM Clients

-- DELETE FROM Clients