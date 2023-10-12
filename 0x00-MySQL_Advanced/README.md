# 0x00. MySQL advanced

## Resources
- [MySQL cheatsheet](https://intranet.alxswe.com/rltoken/8w9di_hk19DIMSBEV3EayQ)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://intranet.alxswe.com/rltoken/2GJbZ48zRPA70o2YhTdH7g)
- [Stored Procedure](https://intranet.alxswe.com/rltoken/K180X2OCzb6gzPngjn-EIg)
- [Triggers](https://intranet.alxswe.com/rltoken/cJ1qA4o-rRm4rWIsqYKSZg)
- [Views](https://intranet.alxswe.com/rltoken/vHg1z3UAOcWMvOt8xZHeiA)
- [Functions and Operators](https://intranet.alxswe.com/rltoken/g-c1m6iljScpi4LeqxBRqQ)
- [Trigger Syntax and Examples](https://intranet.alxswe.com/rltoken/gLVwKjQfRL0Jr_nWqAS7VQ)
- [CREATE TABLE Statement](https://intranet.alxswe.com/rltoken/X789nJ22H6HVh1uCQPl0lg)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://intranet.alxswe.com/rltoken/mfrWMt1KL3NHXblJykMgZg)
- [CREATE INDEX Statement](https://intranet.alxswe.com/rltoken/oCu8Rg9WfKyF4BhTt8dZGQ)
- [CREATE VIEW Statement](https://intranet.alxswe.com/rltoken/FEZNlZFKZmD1ISnLINkCwQ)

## Learning Objectives
```
    How to create tables with constraints
    How to optimize queries by adding indexes
    What is and how to implement stored procedures and functions in MySQL
    What is and how to implement views in MySQL
    What is and how to implement triggers in MySQL
```

## Requirements
```
    All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
    All your files should end with a new line
    All your SQL queries should have a comment just before (i.e. syntax above)
    All your files should start by a comment describing the task
    All SQL keywords should be in uppercase (SELECT, WHERE…)
    A README.md file, at the root of the folder of the project, is mandatory
    The length of your files will be tested using wc
```

## How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

### Project Tasks

0. We are all unique! 
```
Write a SQL script that creates a table users following these requirements:

    With these attributes:
        id, integer, never null, auto increment and primary key
        email, string (255 characters), never null and unique
        name, string (255 characters)
    If the table already exists, your script should not fail
    Your script can be executed on any database

Context: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application
```

1. In and not out 
```
Write a SQL script that creates a table users following these requirements:

    With these attributes:
        id, integer, never null, auto increment and primary key
        email, string (255 characters), never null and unique
        name, string (255 characters)
        country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
    If the table already exists, your script should not fail
    Your script can be executed on any database
```

2. Best band ever! 
```
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

Requirements:

    Import this table dump: metal_bands.sql.zip
    Column names must be: origin and nb_fans
    Your script can be executed on any database

Context: Calculate/compute something is always power intensive… better to distribute the load!
```

3. Old school band 
```
Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

Requirements:

    Import this table dump: metal_bands.sql.zip
    Column names must be: band_name and lifespan (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
    You should use attributes formed and split for computing the lifespan
    Your script can be executed on any database
```

4. Buy buy buy
```
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table items can be negative.

Context: Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!
```

5. Email validation to sent 
```
Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

Context: Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!
```

6. Add bonus 
```
Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

Requirements:

    Procedure AddBonus is taking 3 inputs (in this order):
        user_id, a users.id value (you can assume user_id is linked to an existing users)
        project_name, a new or already exists projects - if no projects.name found in the table, you should create it
        score, the score value for the correction

Context: Write code in SQL is a nice level up!
```

7. Average score 
```
Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

Requirements:

    Procedure ComputeAverageScoreForUser is taking 1 input:
        user_id, a users.id value (you can assume user_id is linked to an existing users)
```

8. Optimize simple search 
```
Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.

Requirements:

    Import this table dump: names.sql.zip
    Only the first letter of name must be indexed

Context: Index is not the solution for any performance issue, but well used, it’s really powerful!
```

9. Optimize search and score 
```
Write a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.

Requirements:

    Import this table dump: names.sql.zip
    Only the first letter of name AND score must be indexed
```

10. Safe divide 
```
Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

Requirements:

    You must create a function
    The function SafeDiv takes 2 arguments:
        a, INT
        b, INT
    And returns a / b or 0 if b == 0
```

11. No table for a meeting 
```
Write a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.

Requirements:

    The view need_meeting should return all students name when:
        They score are under (strict) to 80
        AND no last_meeting date OR more than a month
```

12. Average weighted score 
```
Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

Requirements:

    Procedure ComputeAverageScoreForUser is taking 1 input:
        user_id, a users.id value (you can assume user_id is linked to an existing users)
```

- [Tip](https://intranet.alxswe.com/rltoken/QHx92mlF43zF6GTEil-Cyw)

13. Average weighted score for all! 
```
Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

Requirements:

    Procedure ComputeAverageWeightedScoreForUsers is not taking any input.
```
