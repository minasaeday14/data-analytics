USE northwind;
--Q1 Create a single query to list the product id, product name, unit price and category
name of all products. Order by category name and within that, by product name
SELECT ProductID, ProductName, UnitPrice, CategoryName
FROM Products AS p
JOIN Categories AS c
	ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName ASC, p.ProductName ASC;
-- Q2 Create a single query to list the product id, product name, unit price and supplier
name of all products that cost more than $75. Order by product name

SELECT p.ProductID, p.ProductName, p.UnitPrice, s.CompanyName 
FROM Products AS p
JOIN  Suppliers AS s
	ON   p.SupplierID = s.SupplierID
WHERE p.UnitPrice > 75
ORDER BY  p.ProductName ASC;

-- Q3 Create a single query to list the product id, product name, unit price, category name,
and supplier name of every product. Order by product name. --

SELECT p.ProductID, p.ProductName,  p.UnitPrice, c.CategoryName, s.CompanyName
FROM  Products AS p
JOIN Categories AS c
	ON p.ProductID = c.CategoryID
JOIN Suppliers AS s
	ON p.SupplierID = s.SupplierID
ORDER BY p.ProductName ASC;

-- Q4 Create a single query to list the order id, ship name, ship address, and shipping
-- company name of every order that shipped to Germany. Assign the shipping company
-- shipped to.
 
SELECT o.OrderID,o.ShipName, o.ShipAddress, s.CompanyName AS Shipper
FROM Orders AS o
JOIN Shippers AS s
	ON  o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY Shipper ASC, o.ShipName ASC;

--Q5 Start from the same query as above (#4), but omit OrderID and add logic to group by
ship name, with a count of how many orders were shipped for that ship name
SELECT o.ShipName, COUNT(*) AS OrderCount
FROM Orders AS o
JOIN Shippers AS s
ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName
ORDER BY o.ShipName ASC;

-- Q6Create a single query to list the order id, order date, ship name, ship address of all
orders that included Sasquatch Ale.
SELECT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
FROM Orders AS o
JOIN `Order Details` AS od
ON o.OrderID = od.OrderID
JOIN Products AS p
ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale';


