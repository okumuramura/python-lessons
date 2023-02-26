SELECT
	i.CustomerId,
	count(1) AS Purchases,
	sum(i.Total) AS TotalSpent,
	c.FirstName,
	c.LastName
FROM invoices AS i
JOIN customers AS c ON i.CustomerId = c.CustomerId
GROUP BY i.CustomerId
ORDER BY TotalSpent DESC
LIMIT 1;
