CREATE TABLE student(
    student_id INT,
    name varchar(20),
    major varchar(20),
    PRIMARY KEY(student_id)
);


/*
Drop the table
*/
DROP TABLE student;


/*
Add one more column to the table
*/
ALTER TABLE student 
ADD gpa DECIMAL(3,2);



/*
Insert values into the table
*/
INSERT INTO student VALUES(1, 'Jack', 'Biology');
INSERT INTO student VALUES(2, 'Kate', 'Sociology');
INSERT INTO student(student_id, name) VALUES(3, 'Claire');
INSERT INTO student VALUES(4, 'Stanley', 'Physics');
INSERT INTO student VALUES(5, 'Mike', 'Computer Science');

/*
Select everything
*/
SELECT * FROM student;


/*
Describe the table
*/
DESCRIBE student;



/*###############################################################*/
/*
Create student table so that it will be easier for us to insert stuff
Add some constrain
1. name cannot be NULL
2. Major must be unique: ER_DUP_ENTRY: Duplicate entry 'Physics' for key 'major'
3. A primary key is both not NULL and unique
*/

DROP TABLE student;

CREATE TABLE student(
    student_id INT,
    name varchar(20) NOT NULL,
    major varchar(20) UNIQUE,
    PRIMARY KEY(student_id)
);

INSERT INTO student(student_id, ) VALUES(1, 'Jack', 'Biology');
INSERT INTO student VALUES(2, 'Kate', 'Sociology');
INSERT INTO student VALUES(3, 'Tim', 'Chemistry');
INSERT INTO student VALUES(4, 'Stanley', 'Physics');
INSERT INTO student VALUES(5, 'Mike', 'Computer Science');
INSERT INTO student VALUES(6, 'Jim', 'Physics');


/*###############################################################*/
/*
Default value for unfilled fields
*/
DROP TABLE student;

CREATE TABLE student(
    student_id INT,
    name varchar(20),
    major varchar(20) DEFAULT 'undecided',
    PRIMARY KEY(student_id)
);

INSERT INTO student(student_id, name) VALUES(1, 'Jack');
INSERT INTO student VALUES(2, 'Kate', 'Sociology');
INSERT INTO student VALUES(3, 'Tim', 'Chemistry');
INSERT INTO student VALUES(4, 'Stanley', 'Physics');
INSERT INTO student VALUES(5, 'Mike', 'Computer Science');
INSERT INTO student VALUES(6, 'Jim', 'Physics');

SELECT * FROM student;
SELECT name FROM student;

/*###############################################################*/
/*
Set primary key as auto-increment
*/
DROP TABLE student;

CREATE TABLE student(
    student_id INT AUTO_INCREMENT,
    name varchar(20),
    major varchar(20) DEFAULT 'undecided',
    PRIMARY KEY(student_id)
);

INSERT INTO student(name, major) VALUES('Jack', 'Math');
INSERT INTO student(name, major) VALUES('Kate', 'Sociology');
INSERT INTO student(name, major) VALUES('Tim', 'Biology');
INSERT INTO student(name, major) VALUES('Stanley', 'Physics');
INSERT INTO student(name, major) VALUES('Mike', 'Computer Science');
INSERT INTO student(name, major) VALUES('Jim', 'Biology');

SELECT * FROM student;


/*###############################################################*/
/*
Update database rows inisde a table
*/
SELECT * FROM student;

UPDATE student
SET major = 'Bio'
WHERE major = 'Biology';

UPDATE student
SET major = 'CS'
WHERE major = 'Computer Science';

UPDATE student
SET major = 'Shit'
WHERE student_id = 6;

UPDATE student
SET major = 'Bio-chemistry'
WHERE major = 'Bio' OR major = 'Chemistry';

UPDATE student
SET name = 'Tom', major = 'undecided'
WHERE student_id = 1;

UPDATE student
SET major = 'undecided';

SELECT * FROM student;


/*###############################################################*/
/*
Delete database rows inisde a table
*/
DELETE FROM student
WHERE name = 'Tim' AND major = 'undecided';

SELECT * FROM student;

/*
Delete everything from the table
*/
DELETE FROM student;

SELECT * FROM student;



/*###############################################################*/
/*
Basic Queries: getting information from the database
*/
DROP TABLE student;

CREATE TABLE student(
    student_id INT AUTO_INCREMENT,
    name varchar(20),
    major varchar(20) DEFAULT 'undecided',
    PRIMARY KEY(student_id)
);

INSERT INTO student(name, major) VALUES('Jack', 'Math');
INSERT INTO student(name, major) VALUES('Kate', 'Sociology');
INSERT INTO student(name, major) VALUES('Tim', 'Biology');
INSERT INTO student(name, major) VALUES('Stanley', 'Physics');
INSERT INTO student(name, major) VALUES('Mike', 'Computer Science');
INSERT INTO student(name, major) VALUES('Jim', 'Biology');

SELECT * FROM student;

SELECT name, major FROM student;

SELECT student.name, student.major
FROM student
ORDER BY student_id DESC; /*Select by descending order*/

SELECT *
FROM student
ORDER BY student_id ASC; /*Select by ascending order*/

SELECT *
FROM student
ORDER by student_id ASC
LIMIT 3; /*Select only with a limit*/


/*Selecting and filtering with where*/
SELECT *
FROM student
WHERE major = 'Biology';

SELECT name, major
FROM student
WHERE major = 'Biology' OR major = 'Math';

/*
Some symbols used in SQL:
-- comment
<, >, <=, >=, =, AND, OR
<> not equal
*/

SELECT *
FROM student
WHERE major <> 'Biology'; /*select all with major not equal to biology*/

SELECT *
FROM student
WHERE student_id < 4; /*select all with major not equal to biology*/

/*select with IN*/
SELECT *
FROM student
WHERE name IN ('Stanley', 'Kate', 'Mike');

SELECT *
FROM student
WHERE name IN ('Stanley', 'Kate', 'Mike') AND student_id > 2;














/*###############################################################*/
/*
Company datasase into
*/
SELECT * FROM employee;
DELETE FROM employee;

SELECT * FROM branch;
DELETE FROM branch;

DROP TABLE student;
DROP TABLE employee;
DROP TABLE branch;
DROP TABLE client;
DROP TABLE works_with;
DROP TABLE branch_supplier;




CREATE TABLE employee (
  emp_id INT PRIMARY KEY,
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  birth_day DATE,
  sex VARCHAR(1),
  salary INT,
  super_id INT,
  branch_id INT
);

SELECT * FROM employee;

CREATE TABLE branch (
  branch_id INT PRIMARY KEY,
  branch_name VARCHAR(40),
  mgr_id INT,
  mgr_start_date DATE,
  FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
  /*
  ON DELETE SET NULL: Once emp_id deleted in employee table, mgr_id will be set as NULL in branch table
  */
);
/*
Whenever we set foreign key, we may need to set as 'ON DELETE SET NULL'
*/
SELECT * FROM branch;

ALTER TABLE employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;


ALTER TABLE employee
ADD FOREIGN KEY(super_id)
REFERENCES employee(emp_id)
ON DELETE SET NULL;


CREATE TABLE client (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40),
  branch_id INT,
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);
SELECT * FROM client;



CREATE TABLE works_with (
  emp_id INT,
  client_id INT,
  total_sales INT,
  PRIMARY KEY(emp_id, client_id),
  FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
  FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE
);
SELECT * FROM works_with;


CREATE TABLE branch_supplier (
  branch_id INT,
  supplier_name VARCHAR(40),
  supply_type VARCHAR(40),
  PRIMARY KEY(branch_id, supplier_name),
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);
SELECT * FROM branch_supplier;


-- -----------------------------------------------------------------------------

-- Corporate
INSERT INTO employee VALUES(100, 'David', 'Wallace', '1967-11-17', 'M', 250000, NULL, NULL);

INSERT INTO branch VALUES(1, 'Corporate', 100, '2006-02-09');

UPDATE employee
SET branch_id = 1
WHERE emp_id = 100;

INSERT INTO employee VALUES(101, 'Jan', 'Levinson', '1961-05-11', 'F', 110000, 100, 1);

-- Scranton
INSERT INTO employee VALUES(102, 'Michael', 'Scott', '1964-03-15', 'M', 75000, 100, NULL);

INSERT INTO branch VALUES(2, 'Scranton', 102, '1992-04-06');

UPDATE employee
SET branch_id = 2
WHERE emp_id = 102;

INSERT INTO employee VALUES(103, 'Angela', 'Martin', '1971-06-25', 'F', 63000, 102, 2);
INSERT INTO employee VALUES(104, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, 102, 2);
INSERT INTO employee VALUES(105, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, 2);

-- Stamford
INSERT INTO employee VALUES(106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, 100, NULL);

INSERT INTO branch VALUES(3, 'Stamford', 106, '1998-02-13');

UPDATE employee
SET branch_id = 3
WHERE emp_id = 106;

INSERT INTO employee VALUES(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3);
INSERT INTO employee VALUES(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);


-- BRANCH SUPPLIER
INSERT INTO branch_supplier VALUES(2, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Patriot Paper', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
INSERT INTO branch_supplier VALUES(3, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(3, 'Stamford Lables', 'Custom Forms');

-- CLIENT
INSERT INTO client VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO client VALUES(401, 'Lackawana Country', 2);
INSERT INTO client VALUES(402, 'FedEx', 3);
INSERT INTO client VALUES(403, 'John Daly Law, LLC', 3);
INSERT INTO client VALUES(404, 'Scranton Whitepages', 2);
INSERT INTO client VALUES(405, 'Times Newspaper', 3);
INSERT INTO client VALUES(406, 'FedEx', 2);

-- WORKS_WITH
INSERT INTO works_with VALUES(105, 400, 55000);
INSERT INTO works_with VALUES(102, 401, 267000);
INSERT INTO works_with VALUES(108, 402, 22500);
INSERT INTO works_with VALUES(107, 403, 5000);
INSERT INTO works_with VALUES(108, 403, 12000);
INSERT INTO works_with VALUES(105, 404, 33000);
INSERT INTO works_with VALUES(107, 405, 26000);
INSERT INTO works_with VALUES(102, 406, 15000);
INSERT INTO works_with VALUES(105, 406, 130000);



/*###############################################################*/
/*
More basic queries
*/
SELECT *
FROM employee;

-- Find all employee ordered by salary
SELECT *
FROM employee
ORDER BY salary DESC;


-- Find all employee ordered by sex then name
SELECT *
FROM employee
ORDER BY sex, first_name, last_name;


-- Find all employee ordered by limit
SELECT *
FROM employee
LIMIT 5;


-- Find all employee by first name and last name
SELECT first_name, last_name
FROM employee;


-- Find the forename and surname names of all employee
SELECT first_name as forename, last_name as surname
FROM employee;


-- Find all the different branch_id
SELECT DISTINCT branch_id
FROM employee;


/*###############################################################*/
/*
Functions
*/
SELECT *
FROM employee;

-- Find the number of employees
SELECT COUNT(emp_id)
FROM employee;

-- Find the number of supervisor
SELECT COUNT(super_id)
FROM employee
WHERE sex = 'F' AND birth_day > '1971-01-01';

-- Find the average of all employee salaries
SELECT AVG(salary)
FROM employee
WHERE sex = 'F';

-- Find the sum of all employee salaries
SELECT SUM(salary)
FROM employee;


-- Find out how many males and females there are
SELECT COUNT(sex), sex
FROM employee
GROUP BY sex;


-- Find total sales of each salesman
SELECT *
FROM works_with;
SELECT SUM(total_sales), emp_id
FROM works_with
GROUP BY emp_id;

-- Find total sales from each client
SELECT *
FROM works_with;
SELECT SUM(total_sales), client_id
FROM works_with
GROUP BY client_id;



/*###############################################################*/
/*
Wildcards: a way of defining different patterns that we want to match specific pieces of data
*/
-- % = any number of characters, _ = one character

-- Find any clients who are an LLC
SELECT *
FROM client
WHERE client_name LIKE '%LLC';

-- Find any branch suppliers who are in the label business
SELECT *
FROM branch_supplier
WHERE supplier_name LIKE '% Label%';

-- Find any employee born in October
SELECT *
FROM employee
-- WHERE birth_day LIKE '%-10-%';
WHERE birth_day LIKE '____-10-__';

-- Find any clients  are schools
SELECT *
FROM client
WHERE client_name LIKE '%school%';



/*###############################################################*/
/*
Union
*/
-- Find a list of employee name and branch name
SELECT first_name
FROM employee
UNION
SELECT branch_name
FROM branch
UNION
SELECT client_name
FROM client;


-- Find a list of all clients & branch suppliers' names
SELECT client_name, client.branch_id
FROM client
UNION
SELECT supplier_name, branch_supplier.branch_id
FROM branch_supplier;



/*###############################################################*/
/*
Joins
*/

SELECT *
FROM branch;

INSERT INTO branch VALUES(4, 'Buffalo', NULL, NULL);

-- Find all branchs and names of their managers
SELECT *
FROM employee;

SELECT *
FROM branch;

/* 
general inner join: combine rows of two tables, and join on the common stuff
*/
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
JOIN branch
ON employee.emp_id = branch.mgr_id;


/* 
left join: join based on employee
*/
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
LEFT JOIN branch
ON employee.emp_id = branch.mgr_id
ORDER BY branch_name DESC;


/* 
right join: join based on branch
*/
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
RIGHT JOIN branch
ON employee.emp_id = branch.mgr_id
ORDER BY branch_name DESC;




/*###############################################################*/
/*
Nested qeuries: multipe select statements
*/
-- Find names of all employees who have 
-- sold over 30,000 to a single client
SELECT *
FROM employee;

SELECT *
FROM works_with;

SELECT employee.first_name, employee.last_name
FROM employee
WHERE employee.emp_id IN (
    SELECT works_with.emp_id
    FROM works_with
    WHERE works_with.total_sales > 30000
);


-- Find all clients who are handled by the branch
-- that Micheal Scott manages
-- Assume you know Micheal's ID
SELECT * FROM branch;
SELECT * FROM employee;
SELECT * FROM client;

SELECT client.client_name
FROM client
WHERE client.branch_id = (
    SELECT branch.branch_id
    FROM branch
    WHERE branch.mgr_id = (
        SELECT employee.emp_id
        FROM employee
        WHERE employee.first_name = 'Michael' AND employee.last_name = 'Scott'
        LIMIT 1 /*in case Michael Scott manages multiple branches*/
        )
);



/*###############################################################*/
/*
Delete entries when they have foreign keys in them:
1. ON DELETE NULL: once delete, set as NULL in the foreign table
2. ON DELETE CASCADE: once delete, delete entire row in foreign table
*/
SELECT * FROM employee;
SELECT * FROM branch;

DELETE FROM employee
WHERE emp_id = 102;




/*###############################################################*/
/*
Triggers trigger before/after actions like update, delete, insert 
*/
CREATE TABLE trigger_test(
    message VARCHAR(100)
);

DELIMITER $$
CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES('added new employee');
        /*
        Since we have no () here, we need to end the insert code with ;
        */
    END $$
DELIMITER ;

/*
It changes the statement delimiter from ; to $$. 
This is so you can write ; in your trigger definition without 
the MySQL client misinterpreting that as meaning you're done with it.
Note that when changing back, it's DELIMITER ;, not DELIMITER; 
as I've seen people try to do.


In SQL you close each statement with a delimiter, 
which is by default a semicolon (;). 
In a trigger you need to write multiple statements, 
each ending in a semicolon. To tell MySQL that those 
semicolons are not the end of your trigger statement, 
you temporarily change the delimiter from ; to $$, 
so MySQL will know that the trigger statement only ends when it econunters a $$.

NOTICE: we need to run the trigger in a terminal / CML
*/

SELECT * FROM employee;

INSERT INTO employee
VALUES(109, 'Oscar', 'Martines', '1968-02-19', 'M', 69000, 106, 3);

SELECT * FROM trigger_test;



/*
When trigger, add in specific information
*/
DELIMITER $$
CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES(NEW.first_name);
    END $$
DELIMITER ;


/*
Conditional trigger
*/
DELIMITER $$
CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        IF NEW.sex = 'M' THEN
            INSERT INTO trigger_test VALUES('added male employee');
        ELSEIF NEW.sex = 'F' THEN
            INSERT INTO trigger_test VALUES('added female employee');
        ELSE
            INSERT INTO trigger_test VALUES('added another employee');
        END IF
    END $$
DELIMITER ;


/*
Drop trigger: need to run the code in terminal / CML
*/
DROP TRIGGER my_trigger;









/*###############################################################*/
/*
ER Diagrams
ER = Entity Relationship
Entity - An object we want to model & store information
*/

