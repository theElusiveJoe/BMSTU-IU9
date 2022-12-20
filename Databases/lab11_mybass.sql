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
DROP TRIGGER IF EXISTS prod_del
DROP TRIGGER IF EXISTS order_item_del
DROP TABLE if EXISTS Orders
DROP TABLE if EXISTS Clients
DROP TABLE if EXISTS Products
DROP TABLE if EXISTS Order_items
DROP TABLE if EXISTS Packages
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
	delivery_date date NOT NULL DEFAULT CONVERT(date,GETDATE()),
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

-------------------------ФУНКЦИИ И ПРОЦЕДУРЫ
CREATE FUNCTION dbo.assert_items()
RETURNS INT
AS 
BEGIN
	DECLARE @ret INT;
	DECLARE @p1 INT;
	DECLARE @p2 INT;
	SET @p1 = (SELECT COUNT(*) FROM Orders WHERE Orders.order_id IN (SELECT order_id FROM Order_items));
	SET @p2 = (SELECT COUNT(*) FROM Orders);
	RETURN @p1-@p2;
END;
GO

IF OBJECT_ID ( 'count_required_units', 'P' ) IS NOT NULL
    DROP PROCEDURE count_required_units;
GO
IF OBJECT_ID ( 'count_required_units_by_each_product', 'P' ) IS NOT NULL
    DROP PROCEDURE count_required_units_by_each_product;
GO


-- По каждому товару вывожу требуемое количество единиц этого товара
CREATE PROCEDURE count_required_units
@product_id VARCHAR(100)
AS 
	DECLARE @my_cur CURSOR;
	SET @my_cur = CURSOR FORWARD_ONLY STATIC FOR
		SELECT quantity
		FROM Order_items WHERE Order_items.product_id = @product_id;
	OPEN @my_cur;

	DECLARE @quantity int;
	DECLARE @sum int;
	SET @sum = 0;
	FETCH NEXT FROM @my_cur INTO @quantity;
	WHILE (@@FETCH_STATUS = 0)
		BEGIN
			set @sum = @sum + @quantity;
			FETCH NEXT FROM @my_cur INTO @quantity;
		END
	DECLARE @product_name VARCHAR(100);
	SELECT @product_name = name FROM Products WHERE Products.product_id = @product_id
	PRINT @product_name + '(' + @product_id + ')' + ' - required '+ CAST(@sum AS VARCHAR) + ' pieces';
GO

CREATE PROCEDURE count_required_units_by_each_product
AS 	
	DECLARE @my_cur CURSOR;
	SET @my_cur = CURSOR FORWARD_ONLY STATIC FOR
		SELECT product_id
		FROM Products;
	OPEN @my_cur;
	DECLARE @product_id VARCHAR(100);
	FETCH NEXT FROM @my_cur INTO @product_id;
	WHILE (@@FETCH_STATUS = 0)
		BEGIN
			EXEC count_required_units @product_id;
			FETCH NEXT FROM @my_cur INTO @product_id;
		END

GO

-------------------------ТРИГГЕРЫ

-- Запрет удалять клиента
CREATE TRIGGER client_del ON Clients 
    INSTEAD OF DELETE
    AS THROW 50001, 'u cant delete a client', 1
go

-- Запрет удалять все товары в корзине заказа
CREATE TRIGGER order_item_del ON Order_items 
    AFTER DELETE AS 
	IF ((SELECT COUNT(*) FROM Order_items) = 0)
	BEGIN
		ROLLBACK TRANSACTION;
		THROW 50002, 'u cant delete all products from order', 1
	END
go

-- Запрет удалять товары, которые есть в заказах
CREATE TRIGGER prod_del ON Products 
    INSTEAD OF DELETE
	AS
	IF ((SELECT COUNT(*) FROM Order_items INNER JOIN deleted on deleted.product_id = Order_items.product_id) <> 0)
    	THROW 50003, 'u cant delete product that is in some order', 1
	DELETE FROM Products WHERE Products.product_id in (SELECT product_id FROM deleted)
go

CREATE TRIGGER check_items_insert ON Order_items 
    INSTEAD OF INSERT
	AS
	DECLARE @order_id VARCHAR(100);
	DECLARE @product_id VARCHAR(100);
	DECLARE @quantity INT;
	DECLARE @quantity2 INT;
	DECLARE @price INT;
	DECLARE @price2 INT;
	DECLARE @cur CURSOR;
	SET @cur = CURSOR FORWARD_ONLY STATIC FOR
		SELECT order_id, product_id, quantity, price
		FROM inserted;
	OPEN @cur;

	FETCH NEXT FROM @cur INTO @order_id, @product_id, @quantity, @price;
	WHILE (@@FETCH_STATUS = 0)
		BEGIN
			IF (SELECT COUNT(*) FROM Order_items WHERE order_id = @order_id AND product_id = @product_id) = 0
				INSERT INTO Order_items (order_id, product_id, quantity, price) VALUES (@order_id, @product_id, @quantity, @price)
			ELSE
			BEGIN
				SELECT @price2 = price FROM Order_items WHERE order_id = @order_id AND product_id = @product_id
				IF (@price2 <> @price)
				BEGIN
					ROLLBACK TRANSACTION;
					THROW 50004, 'u cant add one product to cart with different price', 1
				END
				ELSE
				BEGIN
					SELECT @quantity2 = quantity FROM Order_items WHERE order_id = @order_id AND product_id = @product_id
					UPDATE Order_items SET quantity = @quantity + @quantity2 WHERE order_id = @order_id AND product_id = @product_id
				END
			END 
			FETCH NEXT FROM @cur INTO @order_id, @product_id, @quantity, @price;
		END

	IF (dbo.assert_items() <> 0)
	BEGIN
		ROLLBACK TRANSACTION;
    	THROW 50004, 'there are some orders without items', 1
	END
	
go

-- ВОТ ЭТО УЖЕ НЕ ПОНАДОБИТСЯ
-- Проверка, что нет пустых заказов
-- CREATE TRIGGER items_insert ON Order_items 
--     AFTER INSERT
-- 	AS
-- 	PRINT dbo.assert_items() 
-- 	IF (dbo.assert_items() = 0)
-- 	BEGIN
-- 		ROLLBACK TRANSACTION;
--     	THROW 50004, 'there are some orders without items', 1
-- 	END
-- go


-- -------------------------ВЬЮХИ И ИНДЕКСЫ
DROP INDEX IF EXISTS ORDERS
ON Products
go

CREATE INDEX ProductsIX ON 
    Products(product_id)
INCLUDE
    (price, name)
go

DROP VIEW IF EXISTS Orders_to_assemble
go
CREATE View Orders_to_assemble AS
    SELECT o.order_id, i.product_id, i.quantity, o.delivery_date
    FROM Orders as o INNER JOIN Order_items as i on o.order_id = i.order_id WHERE o.status = 'new'
go


-------------------------ДОБАВИМ ЧТО_НИБУДЬ

INSERT INTO Clients (client_email, phone, name)
VALUES	
	('@1', '89999999999', 'Petya'),
	('@2', '88888888888', 'Vasya'),
	('@3', '66666666666', 'Sasha'),
	('@4', '77777777777', 'Vanya')

INSERT INTO Orders (order_id, creation_date, client_email)
VALUES  
	('order1', CONVERT(date,N'10-25-2022'), '@1'), 
	('order2', CONVERT(date,N'10-26-2022'), '@1'), 
	('order3', CONVERT(date,N'10-27-2022'), '@2'), 
	('order4', CONVERT(date,N'10-28-2022'), '@3')


INSERT INTO Products (product_id, name, price)
VALUES 
	('prid1', 'tovar1', 1000),
	('prid2', 'tovar2', 2000),
	('prid3', 'tovar3', 3000),
	('prid4', 'tovar4', 4000),
	('prid5', 'tovar5', 5000),
	('prid6', 'tovar6', 6000),
	('prid7', 'tovar7', 7000)

INSERT INTO Order_items (order_id, product_id, quantity, price)
VALUES
	('order1', 'prid1', 10, 1000),
	('order2', 'prid2', 12, 1950),
	('order3', 'prid3', 2, 3000),
	('order3', 'prid1', 100, 950),
	('order4', 'prid4', 10, 4000),
	('order4', 'prid4', 20, 4000)
GO

INSERT INTO Packages (order_id)
VALUES 
	('order1'),
	('order1'),
	('order2'),
	('order2')
GO
-------------------------ТЕСТИРУЕМ

-- заказы, которые надо начать собирать на складе
-- SELECT order_id, product_id, quantity, delivery_date FROM Orders_to_assemble ORDER BY quantity


-- имя клиента - на сколько денег он назаказывал
-- SELECT c.name , SUM(i.price*i.quantity) AS price_sum 
-- FROM Order_items as i INNER JOIN Orders AS o ON i.order_id = o.order_id INNER JOIN Clients as c ON c.client_email = o.client_email
-- GROUP BY c.name
-- HAVING SUM(i.price*i.quantity) > 40000
-- ORDER BY price_sum DESC 


-- имена клиентов, у которых есть заказы
-- Select DISTINCT c.name FROM Clients as c INNER JOIN Orders as o ON c.client_email = o.client_email


-- альтернативная реализация проверки целостности связи M-M
SELECT o.order_id FROM Orders as o WHERE EXISTS (SELECT * FROM Order_items as i WHERE o.order_id = i.order_id)


-- пример вызова процедуры
-- EXEC count_required_units_by_each_product;



-- проверки на целостнсть...
-- -- UPDATE Orders SET client_email = '@2' Where client_email = '@1'
-- UPDATE Clients SET client_email = '@new' Where client_email = '@1'

-- SELECT * FROM Orders
-- GO 

-- SELECT * FROM Order_items
-- DELETE FROM Order_items WHERE product_id = 'prid1'
-- SELECT * FROM Order_items

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
