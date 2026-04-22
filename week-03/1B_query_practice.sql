USE Northwind
---Q1
SELECT ProductID, ProductName, UnitPrice
FROM  Products
--Q2 Write a query to identify the products where the unit price is $7.50 or les
SELECT ProductID, UnitPrice
FROM  Products
WHERE UnitPrice <= 7.50

-- Q3 What are the products that we carry where we have no units on hand, but 1 or more
units are on backorder?
SELECT ProductID,ProductName,UnitsInStock,UnitsInStock
FROM  Products
WHERE UnitsInStock = 0
	AND UnitsOnOrder >= 1
-- Q4  ending with a query that creates a list of all the seafood items we carry
SELECT *
FROM Products  
LIMIT 5
--So product table uses the FK 'CategoryID as the identifier to relate
-- Thid is know us 1 to1 relationship
SELECT CategoryID, CategoryName
FROM Categories -- This shows me which catgeory is seafood in

SELECT *
FROM Products
WHERE CategoryID = 8
	AND UnitsInStock >= 1;


-- q5              
SELECT *
FROM Suppliers
WHERE CompanyName ='Tokyo Traders';
-- FROM the above query I KNOW that tokyo traader's supplier ID is 4
SELECT *
FROM Products
WHERE SupplierID = 4
-- The Products table uses SupplierID to show which supplier each product comes from.
-- Using SupplierID 4, this query returns all products supplied by Tokyo Traders.


--q6How many employees work at northwind? What employees have "manager"
somewhere in their job title
SELECT COUNT(EmployeeID) AS employee_count
FROM  Employees -- this shows me a count of 9 employees

SELECT EmployeeID,FirstName, LastName, Title
FROM  Employees
WHERE Title LIKE '%manager%';