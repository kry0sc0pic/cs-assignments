/*
Create Table Shoes and insert records 10 records.
Write SQL query for the following:
Table name : shoes
Attributes : size (int) , type (varchar2 20) can be school,office,sports, qty(int), cost(int)

1. Display the type, minimum, maximum and average size of each type of shoes.
2. Display type and total quantity of each type of shoes. Arrange it by descending order of total
quantity .
3. Display type and total quantity of each type of shoes. And display only those type where total
qty is more than 1500.
4. Display type and total quantity of each type of shoes and display only those type where average
size is greater than 5.5.
5. Display type and total quantity of each type of shoes where size is not equal to 6 and total
quantity is greater than 1500.
6. Display the type, size, total count from shoes for each type and with that each size.
(group by multiple columns)
7. Display the total stock value(cost*qty) of each type of shoes. Arrange it in ascending order of
total stock value . Give alias name as „Total stock value‟.
8. Display the count of total number of different types of shoes available in shoes table.
*/

-- create table shoes

CREATE TABLE shoes (size int, type varchar(20), qty int, cost int);


-- 1) Display the type, minimum, maximum and average size of each type of shoes.
SELECT type, MIN(size), MAX(size), AVG(size) FROM shoes GROUP BY type;

-- 2) Display type and total quantity of each type of shoes. Arrange it by descending order of total quantity.
SELECT type, SUM(qty) FROM shoes GROUP BY type ORDER BY SUM(qty) DESC;

-- 3) Display type and total quantity of each type of shoes. And display only those type where total qty is more than 1500.
SELECT type, SUM(qty) FROM shoes GROUP BY type HAVING SUM(qty) > 1500;

-- 4) Display type and total quantity of each type of shoes and display only those type where average size is greater than 5.5.
SELECT type, SUM(qty), AVG(size) FROM shoes GROUP BY type HAVING AVG(size) > 5.5;

-- 5) Display type and total quantity of each type of shoes where size is not equal to 6 and total quantity is greater than 1500.
SELECT type,SUM(qty) FROM shoes GROUP BY type HAVING SUM(qty) > 1500 AND size != 6;

-- 6) Display the type, size, total count from shoes for each type and with that each size. (group by multiple columns)
SELECT type, size, COUNT(*) FROM shoes GROUP BY type, size;

-- 7) Display the total stock value(cost*qty) of each type of shoes. Arrange it in ascending order of total stock value. Give alias name as „Total stock value‟.
SELECT SUM(cost*qty) AS "Total stock value" FROM shoes GROUP BY type ORDER BY SUM(cost*qty) ASC;

-- 8) Display the count of total number of different types of shoes available in shoes table.
SELECT COUNT(DISTINCT type) FROM shoes;

