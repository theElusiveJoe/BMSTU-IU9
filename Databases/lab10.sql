use master;
go

DROP DATABASE IF EXISTS lab10
go

CREATE DATABASE lab10
on (
	NAME = lab10dat,
	FILENAME = '/home/lab10dat.mdf',
	SIZE = 10,
	MAXSIZE = UNLIMITED,
	FILEGROWTH = 5
)
log on (
	NAME = lab10log,
	FILENAME = '/home/lab10log.ldf',
	SIZE = 5,
	MAXSIZE = 20,
	FILEGROWTH = 5
);
go 

use lab10;
go 

DROP TABLE if EXISTS Orders
go 

CREATE TABLE Orders
(
    order_num_in_table int IDENTITY(1,1) NOT NULL,
    order_id Varchar(100) NOT NULL Primary KEY,
    discount Numeric NOT NULL CHECK (discount >= 0),
    payment_type Varchar(100) NOT NULL,
    payment_status Varchar(100) NOT NULL,
    status Varchar(100) NOT NULL DEFAULT 'new',
);
go 

DELETE FROM Orders

INSERT INTO Orders
    (order_id, discount, payment_type, payment_status)
VALUES
    ('1', 2, 'cache', 'not paid'),
    ('2', 3, 'cache', 'not paid')
go 

SELECT * FROM Orders