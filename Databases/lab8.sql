use master;
go

DROP DATABASE IF EXISTS lab8

CREATE DATABASE lab8
on (
	NAME = lab8dat,
	FILENAME = '/home/lab8dat.mdf',
	SIZE = 10,
	MAXSIZE = UNLIMITED,
	FILEGROWTH = 5
)
log on (
	NAME = lab8log,
	FILENAME = '/home/lab8log.ldf',
	SIZE = 5,
	MAXSIZE = 20,
	FILEGROWTH = 5
);
go 

use lab8;
go 

-- 1. Создать хранимую процедуру, производящую выборку
-- из некоторой таблицы и возвращающую результат
-- выборки в виде курсора.

DROP TABLE IF EXISTS Orders

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
    ('Y-3578', CONVERT(date,N'10-27-2022'), 6, 'cache', 'not paid'),
    ('Y-4613', CONVERT(date,N'10-28-2022'), 5, 'cache', 'not paid')
go

SELECT * FROM Orders

DROP PROCEDURE IF EXISTS get_orders
GO

CREATE PROCEDURE get_orders
	@cursor CURSOR VARYING OUTPUT
AS
	SET @cursor = CURSOR FORWARD_ONLY STATIC FOR
		SELECT order_id, payment_status, discount
		FROM Orders;
	OPEN @cursor;
GO

DECLARE @orders_cursor CURSOR;
EXEC get_orders @cursor = @orders_cursor OUTPUT;
DECLARE @order_id VARCHAR(100), @payment_status VARCHAR(100), @discount INT;


FETCH NEXT FROM @orders_cursor INTO @order_id, @payment_status, @discount;
WHILE (@@FETCH_STATUS = 0)
	BEGIN
		PRINT @order_id + ' -> '+ @payment_status + ' ' + CAST(@discount AS VARCHAR);
		FETCH NEXT FROM @orders_cursor INTO @order_id, @payment_status, @discount;
	END
CLOSE @orders_cursor;
DEALLOCATE @orders_cursor;
GO

-- 2. Модифицировать хранимую процедуру п.1. таким
-- образом, чтобы выборка осуществлялась с
-- формированием столбца, значение которого
-- формируется пользовательской функцией.

DROP FUNCTION IF EXISTS dbo.random_discount;
DROP PROCEDURE IF EXISTS randomize_discount;
GO

CREATE FUNCTION dbo.random_discount (@num FLOAT)
RETURNS int AS
BEGIN
    DECLARE @ret int;
	DECLARE @disc FLOAT;
	SET @disc = @num * 100;
    SELECT @ret = CAST(@disc AS INT) % 100;
RETURN @ret
END;
GO

CREATE PROCEDURE randomize_discount
    @cur CURSOR VARYING OUTPUT
AS
    SET @cur = CURSOR FORWARD_ONLY STATIC FOR
        SELECT order_id, dbo.random_discount(RAND(CAST(CAST(NEWID() AS binary(3)) AS INT))) as discount
        FROM Orders;
    OPEN @cur;
go

DECLARE @orders_cursor CURSOR;
EXEC randomize_discount @cur = @orders_cursor OUTPUT;
DECLARE @order_id VARCHAR(100), @discount INT;

FETCH NEXT FROM @orders_cursor INTO @order_id, @discount;
WHILE (@@FETCH_STATUS = 0)
	BEGIN
		PRINT @order_id + ' -> '+ CAST(@discount AS VARCHAR);
		FETCH NEXT FROM @orders_cursor INTO @order_id, @discount;
	END
CLOSE @orders_cursor;
DEALLOCATE @orders_cursor;
GO


-- 3. Создать хранимую процедуру, вызывающую процедуру
-- п.1., осуществляющую прокрутку возвращаемого
-- курсора и выводящую сообщения, сформированные из
-- записей при выполнении условия, заданного еще одной
-- пользовательской функцией.

DROP FUNCTION IF EXISTS dbo.filter_foo
DROP PROCEDURE IF EXISTS print_filtered_by_discount
GO

CREATE FUNCTION dbo.filter_foo(@num INT)
RETURNS INT as 
BEGIN
	DECLARE @ret INT;
	SET @ret = 0 
	IF (@num >= 7)
	SET @ret = 1
	RETURN @ret 
END;
GO

CREATE PROCEDURE print_filtered_by_discount
AS 
	DECLARE @my_cur CURSOR;
	EXEC get_orders @cursor = @my_cur OUTPUT;
	DECLARE @order_id VARCHAR(100), @payment_status VARCHAR(100), @discount INT;
	FETCH NEXT FROM @my_cur INTO @order_id, @payment_status, @discount;
	WHILE (@@FETCH_STATUS = 0)
		BEGIN
			IF (dbo.filter_foo(@discount) = 1)
			PRINT @order_id + ' -> '+ @payment_status;
			FETCH NEXT FROM @my_cur INTO @order_id, @payment_status, @discount;
		END
GO

EXEC print_filtered_by_discount;
GO



-- 4. Модифицировать хранимую процедуру п.2. таким
-- образом, чтобы выборка формировалась с помощью
-- табличной функции.

DROP FUNCTION IF EXISTS dbo.random_discount;
DROP PROCEDURE IF EXISTS randomize_discount;
GO

CREATE FUNCTION dbo.random_discount (@num FLOAT)
RETURNS table AS
RETURN (
	SELECT order_id, CAST((@num*100) AS INT) % 100 as discount
	FROM Orders
)
GO

-- CREATE FUNCTION dbo.random_discount (@num FLOAT)
-- RETURNS @ret TABLE 
-- (
--     order_id Varchar(100) NOT NULL Primary KEY,
--     discount Numeric NOT NULL
-- )
-- AS
-- BEGIN
-- 	INSERT @ret
-- 	SELECT order_id, CAST((@num*100) AS INT) % 100 as discount 
-- 	FROM Orders
-- RETURN
-- END;
-- GO

CREATE PROCEDURE randomize_discount
    @cur CURSOR VARYING OUTPUT
AS
    SET @cur = CURSOR FORWARD_ONLY STATIC FOR
        SELECT *
        FROM dbo.random_discount(RAND(CAST(CAST(NEWID() AS binary(3)) AS INT)));
    OPEN @cur;
go

DECLARE @orders_cursor CURSOR;
EXEC randomize_discount @cur = @orders_cursor OUTPUT;
DECLARE @order_id VARCHAR(100), @discount INT;

FETCH NEXT FROM @orders_cursor INTO @order_id, @discount;
WHILE (@@FETCH_STATUS = 0)
	BEGIN
		PRINT @order_id + ' -> '+ CAST(@discount AS VARCHAR);
		FETCH NEXT FROM @orders_cursor INTO @order_id, @discount;
	END
CLOSE @orders_cursor;
DEALLOCATE @orders_cursor;
GO







