use lab10;
go 

-- dirty read
-- BEGIN TRANSACTION
-- go
--     SELECT order_id, payment_status FROM Orders
--     UPDATE Orders SET payment_status = 'PAID' WHERE order_id = '1'
--     SELECT order_id, payment_status FROM Orders
--     WAITFOR DELAY '00:00:10'
--     ROLLBACK
--     SELECT order_id, payment_status FROM Orders
--     SELECT request_session_id, request_type, request_mode, resource_database_id FROM sys.dm_tran_locks
-- go

-- -- nonrepeatable read
-- BEGIN TRANSACTION
--     SELECT order_id, payment_status FROM Orders
--     UPDATE Orders SET payment_status = 'PAID' WHERE order_id = '1'
--     SELECT order_id, payment_status FROM Orders
--     SELECT request_session_id, request_type, request_mode, resource_database_id FROM sys.dm_tran_locks
--     COMMIT TRANSACTION
-- go


-- -- phantom read
BEGIN TRANSACTION
    SELECT order_id, payment_status FROM Orders
    INSERT INTO Orders  (order_id, discount, payment_type, payment_status) VALUES ('NEW', 3, 'NEW', 'NEW')
    SELECT order_id, payment_status FROM Orders
    SELECT resource_type, resource_description, request_mode FROM sys.dm_tran_locks
    COMMIT TRANSACTION
go