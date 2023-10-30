import datetime
import logging
import azure.functions as func
import pyodbc
from time import sleep

app = func.FunctionApp()

@app.schedule(schedule="*/15 * * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def TimerTrigger(myTimer: func.TimerRequest) -> None:

    # Define SQL connection
    connection_string = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=<SERVER-NAME>.database.windows.net;"
        "Database=<DATABASE-NAME>;"
        "UID=<USERNAME>;"
        "PWD=<PASSWORD>"
    )


    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    customer_query = "SELECT c.FirstName, c.EmailAddress FROM SalesLT.Customer AS c;"
    cursor.execute(customer_query)

    for customer in cursor.fetchall():
        first_name = customer.FirstName

        sales_info_query = f"""
        SELECT c.CustomerID, c.FirstName, c.LastName, c.CompanyName, soh.AccountNumber, soh.OrderDate, soh.TotalDue
        FROM SalesLT.Customer AS c
        JOIN SalesLT.SalesOrderHeader AS soh
        ON soh.CustomerID = c.CustomerID
        WHERE c.FirstName = '{first_name}'
        """
        cursor.execute(sales_info_query)
        first_entry = cursor.fetchone()
        print('#### Sales Info ### \n')
        print(first_entry)

        customer_info_query = f"""
        SELECT c.CustomerID, c.FirstName, c.LastName, c.CompanyName, a.City, a.CountryRegion
        FROM SalesLT.Customer AS c
        JOIN SalesLT.CustomerAddress AS ca
        ON ca.CustomerID = c.CustomerID
        JOIN SalesLT.Address AS a
        ON a.AddressID = ca.AddressID
        WHERE c.FirstName = '{first_name}'
        """
        cursor.execute(customer_info_query)
        first_entry = cursor.fetchone()
        print('#### Customer Info ### \n')
        print(first_entry)

        sales_order_query = f"""
        SELECT c.CustomerID, c.FirstName, c.LastName, c.CompanyName, soh.AccountNumber, soh.OrderDate, soh.TotalDue
        FROM SalesLT.Customer AS c
        JOIN SalesLT.SalesOrderHeader AS soh
        ON soh.CustomerID = c.CustomerID
        WHERE c.EmailAddress = '{customer.EmailAddress}'
        """
        cursor.execute(sales_order_query)
        first_entry = cursor.fetchone()
        print('#### Sales Order Info ### \n')
        print(first_entry)

    conn.close()

    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logging.info('Python timer trigger function ran at %s', utc_timestamp)