use lab10;
go 

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET TRANSACTION ISOLATION LEVEL READ COMMITTED
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE


-- dirty read
-- BEGIN TRANSACTION
--     SELECT order_id, payment_status FROM Orders
--     SELECT request_session_id, request_type, request_mode, resource_database_id FROM sys.dm_tran_locks
-- COMMIT TRANSACTION
-- go

-- -- nonrepeatable read
-- BEGIN TRANSACTION
--     SELECT order_id, payment_status FROM Orders
--     WAITFOR DELAY '00:00:05'
--     SELECT order_id, payment_status FROM Orders
--     SELECT request_session_id, request_type, request_mode, resource_database_id FROM sys.dm_tran_locks
-- COMMIT TRANSACTION
-- go

-- -- phantom read
BEGIN TRANSACTION
    SELECT order_id, payment_status FROM Orders
    WAITFOR DELAY '00:00:05'
    SELECT order_id, payment_status FROM Orders
    SELECT request_session_id, request_type, request_mode, resource_database_id FROM sys.dm_tran_locks
COMMIT TRANSACTION
go