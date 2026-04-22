USE northwind;
-- Write a query to list the product id, product name, and unit price of every product. This
-- time, display them in ascending order by price.
SELECT ProductID , ProductName, UnitPrice
FROM Products    
ORDER BY UnitPrice ASC

-- Q2 . What are the products that we carry where we have at least 100 units on hand? Order
them in descending order by price.
SELECT ProductID , ProductName, UnitPrice
FROM Products 
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC

--Q3  What are the products that we carry where we have at least 100 units on hand? Order
them in descending order by price. If two or more have the same price, list those in
ascending order by product name.

SELECT ProductID , ProductName, UnitPrice
FROM Products 
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC,ProductName ASC

--Q4 Write a query against the orders table that displays the total number of distinct
customers who have placed orders, based on customer ID. Use an alias to label the
count calculation as CustomerCounT

SELECT COUNT(DISTINCT CustomerID) AS Customer_count
FROM Orders  --89 

--Q5Write a query against the orders table that displays the total number of distinct
customers who have placed orders, by customer ID, for each country where orders
have been shipped. Again, use an alias to label the count as CustomerCount. Order
the list by the CustomerCount, largest to smallest

SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS Customer_count
FROM  Orders
GROUP BY ShipCountry
ORDER BY Customer_count DESC

-- Q6 What are the products that we carry where we have less than 25 units on hand, but 1
or more units of them are on order? Write a query that orders them by quantity on
order (high to low), then by product name

SELECT ProductID, ProductName,UnitPrice, UnitsInStock, UnitsOnOrder
FROM Products
WHERE UnitsInStock < 25
	AND UnitsOnOrder >= 1
ORDER BY UnitsOnOrder DESC, ProductName ASC;

-- Q7 Write a query to list each of the job titles in employees, along with a count of how
many employees hold each job title

SELECT Title, COUNT(EmployeeID) AS Employee_count
FROM Employees
GROUP BY  Title
ORDER BY Employee_count DESC


--Q8 What employees have a monthly salary that is between $2000 and $2500? Write a
query that orders them by job title

SELECT EmployeeID, FirstName, LastName, Title, Salary
FROM Employees                
WHERE  Salary BETWEEN 2000 AND 2500
ORDER BY  Title