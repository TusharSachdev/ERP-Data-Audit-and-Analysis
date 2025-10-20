CREATE DATABASE ERPDataAudit;
GO
USE ERPDataAudit;
GO
CREATE TABLE Invoices (
    InvoiceID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT,
    InvoiceDate DATE,
    Amount DECIMAL(10,2),
    Paid BIT,
    DueDate DATE
);
INSERT INTO Invoices (CustomerID, InvoiceDate, Amount, Paid, DueDate)
VALUES
(101, '2025-10-01', 1200.00, 1, '2025-10-10'),
(102, '2025-09-20', 500.00, 0, '2025-09-30'),
(103, NULL, NULL, 0, '2025-10-05'),  -- missing invoice date and amount
(104, '2025-10-05', 750.00, 1, NULL), -- missing due date
(105, '2025-08-15', 1000.00, 0, '2025-09-01'); -- overdue unpaid
