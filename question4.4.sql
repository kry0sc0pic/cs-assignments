/*
Create tables with following constraints AND insert 10 records in emp table and 4 records in
dept table(one for each department).
Table emp
empno int Primary key
ename char(20)
deptno int foreign key
sal int
Table dept
deptno int primary key
dname char(10) can be FIN, MKT, ADMIN, SALES
location char(30)
1. Display the cartisean product.
2. Display ename,dname and dno .
3. Display ename,dno,location where sal is between 1000 and 40000
4. Display ename,dname and dno where sal is >30000 and location is “Navi Mumbai”.
5. Display ename,dno,location where sal is between 1000 and 40000.Arrange sal in descending
order.
6. Display ename,dname and dno where sal is <= 30000 and location is “delhi” and dept is 10 or
20.
7. Display all details from both the tables using natural join
8. Display all details from both tables using equi join.
*/

-- Create table emp
CREATE TABLE emp (empno int PRIMARY KEY, ename char(20), deptno int, sal int);

-- Cteate Table dept
CREATE TABLE dept (deptno int PRIMARY KEY, dname char(10), location char(30));

-- 1) Display the cartisean product.
SELECT * FROM emp, dept;

-- 2) Display ename,dname and dno .
SELECT emp.ename, dept.dname, dept.deptno FROM emp, dept WHERE emp.deptno = dept.deptno;

-- 3) Display ename,dno,location where sal is between 1000 and 40000
SELECT emp.ename, dept.deptno, dept.location FROM emp, dept WHERE emp.deptno = dept.deptno AND emp.sal BETWEEN 1000 AND 40000;

-- 4) DISPLAY ename,dno,location where sal is >30000 and location is “Navi Mumbai”.
SELECT emp.ename, dept.deptno, dept.location FROM emp, dept WHERE emp.deptno = dept.deptno AND emp.sal > 30000 AND dept.location = 'Navi Mumbai';

--5) Display ename,dno,location where sal is between 1000 and 40000.Arrange sal in descending order.
SELECT emp.ename, dept.deptno, dept.location FROM emp, dept WHERE emp.deptno = dept.deptno AND emp.sal BETWEEN 1000 AND 40000 ORDER BY emp.sal DESC;

--6) Display ename,dno,location where sal is <= 30000 and location is “delhi” and dept is 10 or 20.
SELECT emp.ename, dept.deptno, dept.location FROM emp, dept WHERE emp.deptno = dept.deptno AND emp.sal <= 30000 AND dept.location = 'delhi' AND (emp.deptno = 10 OR emp.deptno = 20);

-- 7) Display all details from both the tables using natural join
SELECT * FROM emp NATURAL JOIN dept;

-- 8) Display all details from both tables using equi join.
SELECT * FROM emp JOIN dept ON emp.deptno = dept.deptno;


