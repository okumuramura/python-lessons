-- SELECT
-- 	sum(i.Total)
-- FROM invoices AS i
-- WHERE date('2010-01-01') < i.InvoiceDate
-- 	AND i.InvoiceDate < date('2011-01-01');

-- SELECT strftime('%d.%m.%Y %H:%M:%S', datetime('now', 'localtime'));

SELECT
	sum(i.Total)
FROM invoices AS i
WHERE strftime('%Y', i.InvoiceDate) = '2010';
