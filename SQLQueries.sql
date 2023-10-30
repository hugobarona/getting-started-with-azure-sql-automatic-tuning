-- Define initial customer selection query
DECLARE @CustomerQuery NVARCHAR(MAX) = N'SELECT c.FirstName, c.EmailAddress FROM SalesLT.Customer AS c;'

-- Create a table to store customer information
DECLARE @Customers TABLE (FirstName NVARCHAR(50), EmailAddress NVARCHAR(50))

-- Insert the customer data into the table
INSERT INTO @Customers EXEC (@CustomerQuery)

-- Declare variables to hold customer details for iteration
DECLARE @FirstName NVARCHAR(50), @EmailAddress NVARCHAR(50)

-- Cursor to iterate through the customers
DECLARE CustomerCursor CURSOR FOR 
SELECT FirstName, EmailAddress FROM @Customers

OPEN CustomerCursor
FETCH NEXT FROM CustomerCursor INTO @FirstName, @EmailAddress

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT 'Processing customer: ' + @FirstName

    -- Fetch Sales Info for the current customer
    PRINT 'Fetching Sales Info...'
    SELECT TOP 1 c.CustomerID, c.FirstName, c.LastName, c.CompanyName, soh.AccountNumber, soh.OrderDate, soh.TotalDue
    FROM SalesLT.Customer AS c
    JOIN SalesLT.SalesOrderHeader AS soh ON soh.CustomerID = c.CustomerID
    WHERE c.FirstName = @FirstName;

    -- Fetch Customer Address Info for the current customer
    PRINT 'Fetching Customer Address Info...'
    SELECT TOP 1 c.CustomerID, c.FirstName, c.LastName, c.CompanyName, a.City, a.CountryRegion
    FROM SalesLT.Customer AS c
    JOIN SalesLT.CustomerAddress AS ca ON ca.CustomerID = c.CustomerID
    JOIN SalesLT.Address AS a ON a.AddressID = ca.AddressID
    WHERE c.FirstName = @FirstName;

    -- Fetch Sales Order info based on the customer's email address
    PRINT 'Fetching Sales Order Info...'
    SELECT TOP 1 c.CustomerID, c.FirstName, c.LastName, c.CompanyName, soh.AccountNumber, soh.OrderDate, soh.TotalDue
    FROM SalesLT.Customer AS c
    JOIN SalesLT.SalesOrderHeader AS soh ON soh.CustomerID = c.CustomerID
    WHERE c.EmailAddress = @EmailAddress;

    FETCH NEXT FROM CustomerCursor INTO @FirstName, @EmailAddress
END

CLOSE CustomerCursor
DEALLOCATE CustomerCursor
