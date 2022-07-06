/* 
Create table employee with following fields and constraints
eno int pk
ename varchar(20) not null
sal float(10,2)
comm float(10,2)
deptno int
job varchar(10)
doj date
Insert 5 records

Write the following queries
1. Delete the records where job is clerk.
2. Update all the records by increasing salary by 10%.
3. Update the job of empno 1 to mkt.
4. Modify the comm of employees in FIN job to 1000.
5. Display all the records.
6. Change the deptno to 50 and job as MKT for the employees where comm is null

*/

-- Creating Employee Table
CREATE TABLE employee (eno int primary key,ename varchar(20) not null,sal float(10,2),comm float(10,2),deptno int,job varchar(10), doj date);

-- Inserting Records
INSERT INTO employee values (1,'John',10000,1000,1,'Product Lead','2022-01-01');
INSERT INTO employee values (2,'Jim',20000,2000,4,'Design Lead','2021-03-05');
INSERT INTO employee values (3,'Jack',30000,3000,2,'Software Developer','2021-02-04');
INSERT INTO employee values (4,'Kate',40000,4000,1,'CTO','2021-03-02');
INSERT INTO employee values (5,'John',50000,5000,3,'CEO','2018-05-12');

-- Delete all records where job is clerk
DELETE FROM employee where job="clerk";

-- Update all records by increasing salary by 10%
UPDATE employee SET salary=salary+salary*0.1;

-- Update the job of empno 1 to mkt
UPDATE employee SET job='mkt' where empno=1;

-- Mofify the comm of employees in FIN job to 1000
UPDATE employee SET comm=1000 where job='FIN';

-- Display All The Records
SELECT * FROM employee;

-- Change the deptno to 50 and job as MKT for the employees where comm is null
UPDATE employee SET deptno=50,job='mkt' where comm is null;