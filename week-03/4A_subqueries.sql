USE northwind;
-- Q1 What is the product name(s) of the most expensive products?
SELECT ProductName
FROM  Products
WHERE UnitPrice = (
	SELECT MAX(UnitPrice)
    FROM Products
);
-- Cte de Blaye
-- Q2 What is the product name(s) and categories of the least expensive products?
SELECT ProductName
FROM Products
WHERE UnitPrice = (
	SELECT MIN(UnitPrice)
    FROM Products
);
-- Geitost

-- Q3 What is the order id, shipping name and shipping address of all orders shipped via
-- "Federal Shipping"?

SELECT OrderID, ShipName, ShipAddress 
FROM Orders
WHERE ShipVia = (
	SELECT ShipperID
    FROM Shippers 
    WHERE CompanyName = 'Federal Shipping'
);


-- Q4 What are the order ids of the orders that included "Sasquatch Ale"?
SELECT OrderID
FROM `Order Details`
WHERE ProductID = (
	SELECT ProductID
    FROM Products
    WHERE ProductName = 'Sasquatch Ale'
);

--Q5 What is the name of the employee that sold order 10266?
SELECT FirstName,LastName 
FROM Employees
WHERE EmployeeID  = (
	SELECT EmployeeID
    FROM Orders 
    WHERE OrderID = 10266
);
-- JanetLeverling

-- Q6 What is the name of the customer that bought order 10266

SELECT ContactName
FROM Customers
WHERE CustomerID = (
    SELECT CustomerID
    FROM Orders
    WHERE OrderID = 10266
);
-- Pirkko Koskitalo
