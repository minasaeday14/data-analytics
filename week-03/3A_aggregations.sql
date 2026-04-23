-- Q1. Write a query to find the price of the cheapest item that Northwind sells.
SELECT MIN(UnitPrice) AS CheapestPrice
FROM Products;
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice = (
    SELECT MIN(UnitPrice)
    FROM Products
);

--Q2  Write a query to find the average price of all items that Northwind sells
SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM Products;

-- Q3 Write a query to find the price of the most expensive item that Northwind sells. Then
write a second query to find the name of the product with that price, plus the name of
the supplier for that product
SELECT MAX(UnitPrice) AS MostExpensivePrice
FROM Products;

SELECT p.ProductName, s.CompanyName, p.UnitPrice
FROM Products AS p
JOIN Suppliers AS s
ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (
    SELECT MAX(UnitPrice)
    FROM Products
);

-- Q4 Write a query to find total monthly payroll (the sum of all the employees’ monthly
salaries)

SELECT SUM(Salary) AS monthly_salaries
FROM Employees
-- 20362.929931640625
--Q5 Write a query to identify the highest salary and the lowest salary amounts which any
employee makes. (Just the amounts, not the specific employees!

SELECT MIN(Salary) AS lowest_salary, MAX(Salary) AS highest_salary
FROM Employees
-- lowest = 1744.21 highest = 3119.15

--Q6 Write a query to find the name and supplier ID of each supplier and the number of
items they supply. Hint: Join is your friend here
SELECT s.SupplierID, s.CompanyName, COUNT(p.ProductID) AS ItemCount
FROM Suppliers AS s
JOIN Products AS p
ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName

-- Q7 Write a query to find the list of all category names and the average price for items in
each category

SELECT c.CategoryName, AVG(p.UnitPrice) AS Average_price
FROM Categories AS c
JOIN Products AS p
ON c.CategoryID = p.ProductID
GROUP BY c.CategoryName

--Q8 Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
is the name of each supplier and the number of items they supply.

USE northwind;
SELECT s.CompanyName,COUNT(p.ProductId) AS Item_count
FROM Suppliers AS s
JOIN Products AS p
ON s.SupplierID =p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

-- Write a query to list products currently in inventory by the product id, product name,
and inventory value (calculated by multiplying unit price by the number of units on
hand). Sort the results in descending order by value. If two or more have the same
value, order by product name. If a product is not in stock, leave it off the list.

SELECT ProductID, ProductName, (UnitPrice * UnitsInStock) AS inventory_value
FROM Products
WHERE UnitsInStock > 0
ORDER BY inventory_value DESC, ProductName ASC


