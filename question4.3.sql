/*

Consider the following table named “GYM” with details about Fitness products being sold in the
store. Table Name : GYM
prcode int Primary Key , prname varchar(20) , Price int , manufacturer varchar(20)
Insert 10 records ( Note the records must cater to all requirements of the queries given below)

Write SQL statements to do the following:
a) Display the names and price of all the products in the store
b) Display the names of all the products with price less than Rs.20000.00
c) Display details of all the products with price in the range 20000 to 30000
d) Display names of all products by the manufacturer “Fit Express”
e) Add a new row for product with the details:
“P106”, “Vibro Exerciser”, 23000, null.
f) Change the price of all the records by applying a 10% discount reduction on all the products.
g) Display details of all products with manufacturer name starting with “A”
h) Display details of all products with manufacturer name not ending with “s”
i) Display all rows sorted in descending order of price.
j) Display the name and price where manufacturer is null
k) Display the name and price where manufacturer is not null
l) Display manufacturer, whose name has 10 characters
m) Display manufacturer, whose name not starting with A alphabet.
n) Display the price of items where manufacturer is Avon fitness . Give an alias name to price as
“unit price of the product”. Arrange data in descending order of price.

*/

-- Create table GYM
CREATE TABLE GYM (prcode int PRIMARY KEY , prname varchar(20) , Price int , manufacturer varchar(20));

-- Insert Records
INSERT INTO GYM VALUES (1, 'Vibro Exerciser', 23000, 'Fit Express');
-- TODO: Add more records

-- a) Display the names and price of all the products in the store
SELECT prname, Price FROM GYM;

-- b) Display the names of all the products with price less than Rs.20000.00
SELECT prname, Price FROM GYM WHERE Price < 20000;

-- c) Display details of all the products with price in the range 20000 to 30000
SELECT prname, Price FROM GYM WHERE Price BETWEEN 20000 AND 30000;

-- d) Display names of all products by the manufacturer “Fit Express”
SELECT prname FROM GYM WHERE manufacturer = 'Fit Express';

-- e) Add a new row for product with the details:
-- “P106”, “Vibro Exerciser”, 23000, null.
INSERT INTO GYM VALUES (106, 'Vibro Exerciser', 23000, NULL);

-- f) Change the price of all the records by applying a 10% discount reduction on all the products.
UPDATE GYM SET Price = Price * 0.9;

-- g) Display details of all products with manufacturer name starting with “A”
SELECT prname, Price FROM GYM WHERE manufacturer LIKE 'A%';

-- h) Display details of all products with manufacturer name not ending with “s”
SELECT prname, Price FROM GYM WHERE manufacturer NOT LIKE '%s';

-- i) Display all rows sorted in descending order of price.
SELECT * FROM GYM ORDER BY Price DESC;

-- j) Display the name and price where manufacturer is null
SELECT prname, Price FROM GYM WHERE manufacturer IS NULL;

-- k) Display the name and price where manufacturer is not null
SELECT prname, Price FROM GYM WHERE manufacturer IS NOT NULL;

-- l) Display manufacturer, whose name has 10 characters
SELECT manufacturer FROM GYM WHERE LENGTH(manufacturer) = 10;

-- m) Display manufacturer, whose name not starting with A alphabet.
SELECT manufacturer FROM GYM WHERE manufacturer NOT LIKE 'A%';

-- n) Display the price of items where manufacturer is Avon fitness . Give an alias name to price as
-- “unit price of the product”. Arrange data in descending order of price.
SELECT manufacturer, Price AS 'unit price of the product' FROM GYM WHERE manufacturer = 'Avon fitness';

