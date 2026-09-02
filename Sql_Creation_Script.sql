-- DB Creation
CREATE DATABASE Sales_DW;
GO

USE Sales_DW;
GO

-- Dim_Customers
CREATE TABLE Dim_Customers (
    Customer_ID INT PRIMARY KEY,
    Customer_Name VARCHAR(100) NOT NULL,
    City VARCHAR(50)
);
GO

-- Fact_Orders
CREATE TABLE Fact_Orders (
    Order_ID INT PRIMARY KEY,
    Customer_ID INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    Order_Date DATE NOT NULL,
    CONSTRAINT FK_FactOrders_DimCustomers FOREIGN KEY (Customer_ID) 
        REFERENCES Dim_Customers(Customer_ID)
);
GO