/*
Create table member
mid varchar(5),
fname varchar(10)
contractduration char(1)
Do the following after creating above table:
1. add primary key to mid column
2. add new columns as lname,caddress
3. drop the column caddress
4. drop the primary key of the table.
*/

-- Create member table 
CREATE TABLE member (mid varchar(5),fname varchar(10),contractduration char(1));

--  Add Primary key to mid column
ALTER TABLE member ADD PRIMARY KEY (mid);

-- Add new columns as lname,caddress
ALTER TABLE member ADD lname varchar(10);
ALTER TABLE member ADD caddress varchar(20);

-- Adrop Column caddress
ALTER TABLE member DROP COLUMN caddress;

-- drop the primary key of the table
ALTER TABLE member DROP PRIMARY KEY;