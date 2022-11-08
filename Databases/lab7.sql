use lab6;
go

-- 1. Создать представление на основе одной из таблиц задания 6.
DROP VIEW IF EXISTS OrdersView
go 

CREATE VIEW OrdersView AS
    SELECT * 
    FROM Orders
    WHERE Orders.creation_date >= CONVERT(date,N'10-27-2022')
go 

SELECT * FROM Orders
SELECT * FROM OrdersView
go 


-- 2. Создать представление на основе полей обеих связанных таблиц задания 6.
DROP VIEW IF EXISTS ClientServerView 
go 

CREATE View ClientServerView AS
    SELECT s.os, c.name, s.ram
    FROM Servers as s INNER JOIN Clients as c on s.server_num = c.server_id
go

SELECT * from Clients
SELECT * FROM Servers
SELECT * from ClientServerView
go


-- 3. Создать индекс для одной из таблиц задания 6, включив в него дополнительные неключевые поля.
DROP INDEX IF EXISTS ProductsIX 
ON Products
go

CREATE INDEX ProductsIX ON 
    Products(product_id)
INCLUDE
    (weight_kg, price)
go

-- 4. Создать индексированное представление.
DROP VIEW IF EXISTS ProductsView
go

CREATE VIEW ProductsView
WITH SCHEMABINDING  -- чтобы гарантировать связь представления и табицы
AS
    SELECT product_id, name, price, description
    FROM dbo.Products
    WHERE Products.price < 1000
go

CREATE UNIQUE CLUSTERED INDEX ProductsIXV_product_id
    ON ProductsView (product_id)
go

Select * FROM ProductsView

