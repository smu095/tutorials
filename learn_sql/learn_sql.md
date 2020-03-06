# Codecademy: Learn SQL

This document contains notes from the [Codecademy course Learn SQL](https://www.codecademy.com/learn/learn-sql).

[TOC]

## Lesson 1: Manipulations

### Introduction to SQL

SQL, **S**tructured **Q**uery **L**anguage, is a programming language designed to manage data stored in relational databases. SQL operates through simple, declarative statements. This keeps data accurate and secure, and helps maintain the integrity of databases, regardless of size.

The SQL language is widely used today across web frameworks and database applications. Knowing SQL gives you the freedom to explore your data, and the power to make better decisions. By learning SQL, you will also learn concepts that apply to nearly every data storage system.

The statements covered in this course use SQLite Relational Database Management System [(RDBMS)](https://www.codecademy.com/articles/what-is-rdbms-sql). You can also access a glossary of all the [SQL commands](https://www.codecademy.com/articles/sql-commands) taught in this course.

### Relational Databases

A *relational database* is a database that organizes information into one or more tables.

A *table* is a collection of data organized into rows and columns. Tables are sometimes referred to as *relations*.

A *column* is a set of data values of a particular type.

A *row* is a single record in a table.

All data stored in a relational database is of a certain data type. Some of the most common data types are:

- `INTEGER`, a positive or negative whole number
- `TEXT`, a text string
- `DATE`, the date formatted as YYYY-MM-DD
- `REAL`, a decimal value

### Statements

The code below is a SQL statement. A *statement* is text that the database recognizes as a valid command. Statements always end in a semicolon `;`.

```
CREATE TABLE table_name (
   column_1 data_type, 
   column_2 data_type, 
   column_3 data_type
);
```

Let’s break down the components of a statement:

1. `CREATE TABLE` is a *clause*. Clauses perform specific tasks in SQL. By convention, clauses are written in capital letters. Clauses can also be referred to as commands.
2. `table_name` refers to the name of the table that the command is applied to.
3. `(column_1 data_type, column_2 data_type, column_3 data_type)` is a *parameter*. A parameter is a list of columns, data types, or values that are passed to a clause as an argument. Here, the parameter is a list of column names and the associated data type.

The structure of SQL statements vary. The number of lines used does not matter. A statement can be written all on one line, or split up across multiple lines if it makes it easier to read. In this course, you will become familiar with the structure of common statements.

### Create

`CREATE` statements allow us to create a new table in the database. You can use the `CREATE` statement anytime you want to create a new table from scratch. The statement below creates a new table named `celebs`.

```
CREATE TABLE celebs (
   id INTEGER, 
   name TEXT, 
   age INTEGER
);
```

1. `CREATE TABLE` is a clause that tells SQL you want to create a new table.
2. `celebs` is the name of the table.
3. `(id INTEGER, name TEXT, age INTEGER)` is a list of parameters defining each column, or attribute in the table and its data type:

- `id` is the first column in the table. It stores values of data type `INTEGER`
- `name` is the second column in the table. It stores values of data type `TEXT`
- `age` is the third column in the table. It stores values of data type `INTEGER`

### Insert

The `INSERT` statement inserts a new row into a table. You can use the `INSERT` statement when you want to add new records. The statement below enters a record for Justin Bieber into the `celebs` table.

```
INSERT INTO celebs (id, name, age) 
VALUES (1, 'Justin Bieber', 22);
```

1. `INSERT INTO` is a clause that adds the specified row or rows.
2. `celebs` is the name of the table the row is added to.
3. `(id, name, age)` is a parameter identifying the columns that data will be inserted into.
4. `VALUES` is a clause that indicates the data being inserted.
   `(1, 'Justin Bieber', 22)` is a parameter identifying the values being inserted.

- `1` is an integer that will be inserted into the `id` column
- `'Justin Bieber'` is text that will be inserted into the `name` column
- `22` is an integer that will be inserted into the `age` column

### Select

`SELECT` statements are used to fetch data from a database. In the statement below, `SELECT` returns all data in the `name` column of the `celebs` table.

```
SELECT name FROM celebs;
```

1. `SELECT` is a clause that indicates that the statement is a query. You will use `SELECT` every time you query data from a database.
2. `name` specifies the column to query data from.
3. `FROM celebs` specifies the name of the table to query data from. In this statement, data is queried from the `celebs` table.

You can also query data from all columns in a table with `SELECT`.

```
SELECT * FROM celebs;
```

`*` is a special wildcard character that we have been using. It allows you to select every column in a table without having to name each one individually. Here, the result set contains every column in the `celebs` table.

`SELECT` statements always return a new table called the *result set*.

### Alter

The `ALTER TABLE` statement adds a new column to a table. You can use this command when you want to add columns to a table. The statement below adds a new column `twitter_handle` to the `celebs` table.

```
ALTER TABLE celebs 
ADD COLUMN twitter_handle TEXT;
```

1. `ALTER TABLE` is a clause that lets you make the specified changes.
2. `celebs` is the name of the table that is being changed.
3. `ADD COLUMN` is a clause that lets you add a new column to a table:
   1. `twitter_handle` is the name of the new column being added
   2. `TEXT` is the data type for the new column

4. `NULL` is a special value in SQL that represents missing or unknown data. Here, the rows that existed before the column was added have `NULL` (∅) values for `twitter_handle`.

### Update

The `UPDATE` statement edits a row in a table. You can use the `UPDATE` statement when you want to change existing records. The statement below updates the record with an `id` value of `4` to have the `twitter_handle` `@taylorswift13`.

```
UPDATE celebs 
SET twitter_handle = '@taylorswift13' 
WHERE id = 4; 
```

1. `UPDATE` is a clause that edits a row in the table.
2. `celebs` is the name of the table.
3. `SET` is a clause that indicates the column to edit:
   1. `twitter_handle` is the name of the column that is going to be updated
   2. `@taylorswift13` is the new value that is going to be inserted into the `twitter_handle` column.

4. `WHERE` is a clause that indicates which row(s) to update with the new column value. Here the row with a `4` in the `id` column is the row that will have the `twitter_handle` updated to `@taylorswift13`.

### Delete

The `DELETE FROM` statement deletes one or more rows from a table. You can use the statement when you want to delete existing records. The statement below deletes all records in the `celeb` table with no `twitter_handle`:

```
DELETE FROM celebs 
WHERE twitter_handle IS NULL;
```

1. `DELETE FROM` is a clause that lets you delete rows from a table.
2. `celebs` is the name of the table we want to delete rows from.
3. `WHERE` is a clause that lets you select which rows you want to delete. Here we want to delete all of the rows where the twitter_handle column `IS NULL`.
4. `IS NULL` is a condition in SQL that returns true when the value is `NULL` and false otherwise.

### Constraints

*Constraints* that add information about how a column can be used are invoked after specifying the data type for a column. They can be used to tell the database to reject inserted data that does not adhere to a certain restriction. The statement below sets *constraints* on the `celebs` table.

```
CREATE TABLE celebs (
   id INTEGER PRIMARY KEY, 
   name TEXT UNIQUE,
   date_of_birth TEXT NOT NULL,
   date_of_death TEXT DEFAULT 'Not Applicable'
);
```

1. `PRIMARY KEY` columns can be used to uniquely identify the row. Attempts to insert a row with an identical value to a row already in the table will result in a *constraint violation* which will not allow you to insert the new row.

2. `UNIQUE` columns have a different value for every row. This is similar to `PRIMARY KEY` except a table can have many different `UNIQUE` columns.

3. `NOT NULL` columns must have a value. Attempts to insert a row without a value for a `NOT NULL` column will result in a constraint violation and the new row will not be inserted.

4. `DEFAULT` columns take an additional argument that will be the assumed value for an inserted row if the new row does not specify a value for that column.

### Review

We’ve learned six commands commonly used to manage data stored in a relational database and how to set constraints on such data. What can we generalize so far?

SQL is a programming language designed to manipulate and manage data stored in relational databases.

- A *relational database* is a database that organizes information into one or more tables.
- A *table* is a collection of data organized into rows and columns.

A *statement* is a string of characters that the database recognizes as a valid command.

- `CREATE TABLE` creates a new table.
- `INSERT INTO` adds a new row to a table.
- `SELECT` queries data from a table.
- `ALTER TABLE` changes an existing table.
- `UPDATE` edits a row in a table.
- `DELETE FROM` deletes rows from a table.

*Constraints* add information about how a column can be used

Download the [Manipulation: Cheat Sheet](https://www.codecademy.com/learn/learn-sql/modules/learn-sql-manipulation/reference) to help you remember the content covered in this lesson.



## Lesson 2: Queries

### Introduction

In this lesson, we will be learning different SQL commands to **query** a single table in a database.

One of the core purposes of the SQL language is to retrieve information stored in a database. This is commonly referred to as querying. Queries allow us to communicate with the database by asking questions and having the result set return data relevant to the question.

We will be querying a database with one table named `movies`.

*Fun fact:* IBM started out SQL as SEQUEL (**S**tructured **E**nglish **QUE**ry **L**anguage) in the 1970’s to query databases.



### Select

Previously, we learned that `SELECT` is used every time you want to query data from a database and `*` means *all* columns.

Suppose we are only interested in two of the columns. We can select individual columns by their names (separated by a comma):

```
SELECT column1, column2 
FROM table_name;
```

To make it easier to read, we moved `FROM` to another line.

Line breaks don’t mean anything specific in SQL. We could write this entire query in one line, and it would run just fine.



### As

Knowing how `SELECT` works, suppose we have the code below:

```
SELECT name AS 'Titles'
FROM movies;
```

Can you guess what `AS` does?

`AS` is a keyword in SQL that allows you to *rename* a column or table using an alias. The new name can be anything you want as long as you put it inside of single quotes. Here we renamed the `name` column as `Titles`.

Some important things to note:

- Although it’s not always necessary, it’s best practice to surround your aliases with single quotes.
- When using `AS`, the columns are not being renamed in the table. The aliases only appear in the result.



### Distinct

When we are examining data in a table, it can be helpful to know what *distinct* values exist in a particular column.

`DISTINCT` is used to return unique values in the output. It filters out all duplicate values in the specified column(s).

For instance,

```
SELECT tools 
FROM inventory;
```

might produce:

| tools  |
| ------ |
| Hammer |
| Nails  |
| Nails  |
| Nails  |

By adding `DISTINCT` before the column name,

```
SELECT DISTINCT tools 
FROM inventory;
```

the result would now be:

| tools  |
| ------ |
| Hammer |
| Nails  |

Filtering the results of a query is an important skill in SQL. It is easier to see the different possible `genre`s in the `movie` table after the data has been filtered than to scan every row in the table.



### Where

We can restrict our query results using the `WHERE` clause in order to obtain only the information we want.

Following this format, the statement below filters the result set to only include top rated movies (IMDb ratings greater than 8):

```
SELECT *
FROM movies
WHERE imdb_rating > 8;
```

How does it work?

1. `WHERE` clause filters the result set to only include rows where the following *condition* is true.
2. `imdb_rating > 8` is the condition. Here, only rows with a value greater than 8 in the `imdb_rating` column will be returned.

The `>` is an *operator*. Operators create a condition that can be evaluated as either *true* or *false*.

Comparison operators used with the `WHERE` clause are:

- `=` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

There are also some special operators that we will learn more about in the upcoming exercises.



### Like (part I)

`LIKE` can be a useful operator when you want to compare similar values.

The `movies` table contains two films with similar titles, ‘Se7en’ and ‘Seven’.

How could we select all movies that start with ‘Se’ and end with ‘en’ and have exactly one character in the middle?

```
SELECT * 
FROM movies
WHERE name LIKE 'Se_en';
```

- `LIKE` is a special operator used with the `WHERE` clause to search for a specific pattern in a column.
- `name LIKE 'Se_en'` is a condition evaluating the `name` column for a specific pattern.
- `Se_en` represents a pattern with a *wildcard* character.

The `_` means you can substitute any individual character here without breaking the pattern. The names `Seven` and `Se7en` both match this pattern.



### Like (part II)

The percentage sign `%` is another wildcard character that can be used with `LIKE`.

This statement below filters the result set to only include movies with names that begin with the letter ‘A’:

```
SELECT * 
FROM movies
WHERE name LIKE 'A%';
```

`%` is a wildcard character that matches zero or more missing letters in the pattern. For example:

- `A%` matches all movies with names that begin with letter ‘A’
- `%a` matches all movies that end with ‘a’

We can also use `%` both before and after a pattern:

```
SELECT * 
FROM movies 
WHERE name LIKE '%man%';
```

Here, any movie that *contains* the word ‘man’ in its name will be returned in the result.

`LIKE` is not case sensitive. ‘Batman’ and ‘Man of Steel’ will both appear in the result of the query above.



### Is Null

By this point of the lesson, you might have noticed that there are a few missing values in the `movies` table. More often than not, the data you encounter will have missing values.

Unknown values are indicated by `NULL`.

It is not possible to test for `NULL` values with comparison operators, such as `=` and `!=`.

Instead, we will have to use these operators:

- `IS NULL`
- `IS NOT NULL`

To filter for all movies *with* an IMDb rating:

```
SELECT name
FROM movies 
WHERE imdb_rating IS NOT NULL;
```



### Between

The `BETWEEN` operator is used in a `WHERE` clause to filter the result set within a certain *range*. It accepts two values that are either numbers, text or dates.

For example, this statement filters the result set to only include movies with `year`s from 1990 up to, *and including* 1999.

```
SELECT *
FROM movies
WHERE year BETWEEN 1990 AND 1999;
```

When the values are text, `BETWEEN` filters the result set for within the alphabetical range.

In this statement, `BETWEEN` filters the result set to only include movies with `name`s that begin with the letter ‘A’ up to, *but not including* ones that begin with ‘J’.

```
SELECT *
FROM movies
WHERE name BETWEEN 'A' AND 'J';
```

However, if a movie has a name of simply ‘J’, it would actually match. This is because `BETWEEN` goes *up to* the second value — up to ‘J’. So the movie named ‘J’ would be included in the result set but not ‘Jaws’.



### And

Sometimes we want to *combine multiple conditions* in a `WHERE` clause to make the result set more specific and useful.

One way of doing this is to use the `AND` operator. Here, we use the `AND` operator to only return 90’s romance movies.

```
SELECT * 
FROM movies
WHERE year BETWEEN 1990 AND 1999
   AND genre = 'romance';
```

- `year BETWEEN 1990 AND 1999` is the 1st condition.
- `genre = 'romance'` is the 2nd condition.
- `AND` combines the two conditions.

![AND Venn Diagram](https://s3.amazonaws.com/codecademy-content/courses/learn-sql/queries/AND.svg)

With `AND`, *both* conditions must be true for the row to be included in the result.



### Or

Similar to `AND`, the `OR` operator can also be used to combine multiple conditions in `WHERE`, but there is a fundamental difference:

- `AND` operator displays a row if *all* the conditions are true.
- `OR` operator displays a row if *any* condition is true.

Suppose we want to check out a new movie or something action-packed:

```
SELECT *
FROM movies
WHERE year > 2014
   OR genre = 'action';
```

- `year > 2014` is the 1st condition.
- `genre = 'action'` is the 2nd condition.
- `OR` combines the two conditions.

![OR Venn Diagram](https://s3.amazonaws.com/codecademy-content/courses/learn-sql/queries/OR.svg)

With `OR`, if *any* of the conditions are true, then the row is added to the result.



### Order By

It is often useful to list the data in our result set in a particular order.

We can *sort* the results using `ORDER BY`, either alphabetically or numerically. Sorting the results often makes the data more useful and easier to analyze.

For example, if we want to sort everything by the movie’s title from A through Z:

```
SELECT *
FROM movies
ORDER BY name;
```

- `ORDER BY` is a clause that indicates you want to sort the result set by a particular column.
- `name` is the specified column.

Sometimes we want to sort things in a decreasing order. For example, if we want to select all of the well-received movies, sorted from highest to lowest by their year:

```
SELECT *
FROM movies
WHERE imdb_rating > 8
ORDER BY year DESC;
```

- `DESC` is a keyword used in `ORDER BY` to sort the results in *descending order* (high to low or Z-A).
- `ASC` is a keyword used in `ORDER BY` to sort the results in *ascending* order (low to high or A-Z).

The column that we `ORDER BY` doesn’t even have to be one of the columns that we’re displaying.

Note: `ORDER BY` always goes after `WHERE` (if `WHERE` is present).



### Limit

Most SQL tables contain hundreds of thousands of records. In those situations, it becomes important to cap the number of rows in the result.

For instance, imagine that we just want to see a few examples of records.

```
SELECT *
FROM movies
LIMIT 10;
```

`LIMIT` is a clause that lets you specify the maximum number of rows the result set will have. This saves space on our screen and makes our queries run faster.

Here, we specify that the result set can’t have more than 10 rows.

`LIMIT` always goes at the very end of the query. Also, it is **not supported in all SQL databases**.



### Case

A `CASE` statement allows us to create different outputs (usually in the `SELECT` statement). It is SQL’s way of handling [if-then](https://en.wikipedia.org/wiki/Conditional_(computer_programming)) logic.

Suppose we want to condense the ratings in `movies` to three levels:

- *If the rating is above 8, then it is Fantastic.*
- *If the rating is above 6, then it is Poorly Received.*
- *Else, Avoid at All Costs.*

```
SELECT name,
 CASE
  WHEN imdb_rating > 8 THEN 'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid at All Costs'
 END
FROM movies;
```

- Each `WHEN` tests a condition and the following `THEN` gives us the string if the condition is true.
- The `ELSE` gives us the string if *all* the above conditions are false.
- The `CASE` statement must end with `END`.

In the result, you have to scroll right because the column name is very long. To shorten it, we can rename the column to ‘Review’ using `AS`:

```
SELECT name,
 CASE
  WHEN imdb_rating > 8 THEN 'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid at All Costs'
 END AS 'Review'
FROM movies;
```



### Review

We just learned how to query data from a database using SQL. We also learned how to filter queries to make the information more specific and useful.

Let’s summarize:

- `SELECT` is the clause we use every time we want to query information from a database.
- `AS` renames a column or table.
- `DISTINCT` return unique values.
- `WHERE` is a popular command that lets you filter the results of the query based on conditions that you specify.
- `LIKE` and `BETWEEN` are special operators.
- `AND` and `OR` combines multiple conditions.
- `ORDER BY` sorts the result.
- `LIMIT` specifies the maximum number of rows that the query will return.
- `CASE` creates different outputs.

Download the [Queries: Cheat Sheet](https://www.codecademy.com/learn/learn-sql/modules/learn-sql-queries/reference) to help you remember the content covered in this lesson.



## Lesson 3: Aggregate functions

### Introduction

We’ve learned how to write queries to retrieve information from the database. Now, we are going to learn how to perform calculations using SQL.

Calculations performed on multiple rows of a table are called **aggregates**.

Here is a quick preview of some important aggregates that we will cover in the next five exercises:

- `COUNT()`: count the number of rows
- `SUM()`: the sum of the values in a column
- `MAX()`/`MIN()`: the largest/smallest value
- `AVG()`: the average of the values in a column
- `ROUND()`: round the values in the column

Note that the functions **take the name of a column as an argument**. Also note that functions can be composed.



### Count

The fastest way to calculate how many rows are in a table is to use the `COUNT()` function.

`COUNT()` is a function that takes the name of a column as an argument and counts the number of non-empty values in that column.

```
SELECT COUNT(*)
FROM table_name;
```

Here, we want to count every row, so we pass `*` as an argument inside the parenthesis.



### Sum

SQL makes it easy to add all values in a particular column using `SUM()`.

`SUM()` is a function that takes the name of a column as an argument and returns the sum of all the values in that column.



### Max / Min

The `MAX()` and `MIN()` functions return the highest and lowest values in a column, respectively.

`MAX()` takes the name of a column as an argument and returns the largest value in that column.

`MIN()` works the same way but it does the exact opposite; it returns the smallest value.



### Average

SQL uses the `AVG()` function to quickly calculate the average value of a particular column.

The `AVG()` function works by taking a column name as an argument and returns the average value for that column.



### Round

By default, SQL tries to be as precise as possible without rounding. We can make the result table easier to read using the `ROUND()` function.

`ROUND()` function takes two arguments inside the parenthesis:

1. a column name
2. an integer

It rounds the values in the column to the number of decimal places specified by the integer.



### Group By (part I)

Oftentimes, we will want to calculate an aggregate for data with certain characteristics.

For instance, we might want to know the mean IMDb ratings for all movies each year. We could calculate each number by a series of queries with different `WHERE` statements, like so:

```
SELECT AVG(imdb_rating)
FROM movies
WHERE year = 1999;

SELECT AVG(imdb_rating)
FROM movies
WHERE year = 2000;

SELECT AVG(imdb_rating)
FROM movies
WHERE year = 2001;
```

and so on.

Luckily, there’s a better way!

We can use `GROUP BY` to do this in a single step:

```
SELECT year,
   AVG(imdb_rating)
FROM movies
GROUP BY year
ORDER BY year;
```

`GROUP BY` is a clause in SQL that is used with aggregate functions. It is used in collaboration with the `SELECT` statement to arrange identical data into *groups*.

**Important:** The `GROUP BY` statement comes after any `WHERE` statements, but before `ORDER BY` or `LIMIT`.



### Group By (part II)

Sometimes, we want to `GROUP BY` a calculation done on a column.

For instance, we might want to know how many movies have IMDb ratings that round to 1, 2, 3, 4, 5. We could do this using the following syntax:

```
SELECT ROUND(imdb_rating),
   COUNT(name)
FROM movies
GROUP BY ROUND(imdb_rating)
ORDER BY ROUND(imdb_rating);
```

However, this query may be time-consuming to write and more prone to error.

SQL lets us use column reference(s) in our `GROUP BY` that will make our lives easier.

- `1` is the first column selected
- `2` is the second column selected
- `3` is the third column selected

and so on.

The following query is equivalent to the one above:

```
SELECT ROUND(imdb_rating),
   COUNT(name)
FROM movies
GROUP BY 1
ORDER BY 1;
```

Here, the `1` refers to the first column in our `SELECT` statement, `ROUND(imdb_rating)`.



### Having

In addition to being able to group data using `GROUP BY`, SQL also allows you to filter which groups to include and which to exclude.

For instance, imagine that we want to see how many movies of different genres were produced each year, but we only care about years and genres with at least 10 movies.

**We can’t use `WHERE` here because we don’t want to filter the rows; we want to *filter groups*.**

**This is where `HAVING` comes in.**

`HAVING` is very similar to `WHERE`. In fact, all types of `WHERE` clauses you learned about thus far can be used with `HAVING`.

We can use the following for the problem:

```
SELECT year,
   genre,
   COUNT(name)
FROM movies
GROUP BY 1, 2
HAVING COUNT(name) > 10;
```

- **When we want to limit the results of a query based on values of the individual rows, use `WHERE`.**
- **When we want to limit the results of a query based on an aggregate property, use `HAVING`.**

**`HAVING` statement always comes after `GROUP BY`, but before `ORDER BY` and `LIMIT`.**



### Review

You just learned how to use aggregate functions to perform calculations on your data. What can we generalize so far?

- `COUNT()`: count the number of rows
- `SUM()`: the sum of the values in a column
- `MAX()`/`MIN()`: the largest/smallest value
- `AVG()`: the average of the values in a column
- `ROUND()`: round the values in the column

*Aggregate functions* combine multiple rows together to form a single value of more meaningful information.

- `GROUP BY` is a clause used with aggregate functions to combine data from one or more columns.
- `HAVING` limit the results of a query based on an aggregate property.

Download the [Aggregate Functions: Cheat Sheet](https://www.codecademy.com/learn/learn-sql/modules/learn-sql-aggregate-functions/reference) to help you remember the content covered in this lesson.



## Lesson 4: Multiple tables

### Introduction

In order to efficiently store data, we often spread related information across multiple tables.

For instance, imagine that we’re running a magazine company where users can have different types of subscriptions to different products. Different subscriptions might have many different properties. Each customer would also have lots of associated information.

We could have one table with all of the following information:

- `order_id`
- `customer_id`
- `customer_name`
- `customer_address`
- `subscription_id`
- `subscription_description`
- `subscription_monthly_price`
- `subscription_length`
- `purchase_date`

However, a lot of this information would be repeated. If the same customer has multiple subscriptions, that customer’s name and address will be reported multiple times. If the same subscription type is ordered by multiple customers, then the subscription price and subscription description will be repeated. This will make our table big and unmanageable.

So instead, we can split our data into three tables:

1. `orders` would contain just the information necessary to describe what was ordered:

- `order_id`, `customer_id`, `subscription_id`, `purchase_date`

2. `subscriptions` would contain the information to describe each type of subscription:

- `subscription_id`, `description`, `price_per_month`, `subscription_length`

3. `customers` would contain the information for each customer:

- `customer_id`, `customer_name`, `address`

In this lesson, we’ll learn the SQL commands that will help us work with data that is stored in multiple tables.



### Combining Tables with SQL

Combining tables manually is time-consuming. Luckily, SQL gives us an easy sequence for this: it’s called a `JOIN`.

If we want to combine `orders` and `customers`, we would type:

```
SELECT *
FROM orders
JOIN customers
  ON orders.customer_id = customers.customer_id;
```

Let’s break down this command:

1. The first line selects all columns from our combined table. If we only want to select certain columns, we can specify which ones we want.
2. The second line specifies the first table that we want to look in, `orders`
3. The third line uses `JOIN` to say that we want to combine information from `orders` with `customers`.
4. The fourth line tells us how to combine the two tables. We want to match `orders` table’s `customer_id` column with `customers` table’s `customer_id` column.

Because column names are often repeated across multiple tables, we use the syntax `table_name.column_name` to be sure that our requests for columns are unambiguous. In our example, we use this syntax in the `ON` statement, but we will also use it in the `SELECT` or any other statement where we refer to column names.

For example: Instead of selecting *all* the columns using `*`, if we only wanted to select `orders` table’s `order_id` column and `customers` table’s `customer_name` column, we could use the following query:

```
SELECT orders.order_id,
   customers.customer_name
FROM orders
JOIN customers
  ON orders.customer_id = customers.customer_id;
```



### Inner Joins

Let’s revisit how we joined `orders` and `customers`. For every possible value of `customer_id` in `orders`, there was a corresponding row of `customers` with the same `customer_id`.

What if that wasn’t true?

For instance, imagine that our `customers` table was out of date, and was missing any information on customer 11. If that customer had an order in `orders`, what would happen when we joined the tables?

When we perform a simple `JOIN` (often called an *inner join*) our result only includes rows that match our `ON` condition.

Consider the following animation, which illustrates an inner join of two tables on `table1.c2 = table2.c2`:

![Animation of an Inner Join](https://s3.amazonaws.com/codecademy-content/courses/learn-sql/multiple-tables/inner-join.gif)

The first and last rows have matching values of `c2`. The middle rows do not match. The final result has all values from the first and last rows but does not include the non-matching middle row.



### Left Joins

What if we want to combine two tables and keep some of the un-matched rows?

SQL lets us do this through a command called `LEFT JOIN`. A *left join* will keep all rows from the first table, regardless of whether there is a matching row in the second table.

Consider the following animation:

![Animation of a Left Join](https://s3.amazonaws.com/codecademy-content/courses/learn-sql/multiple-tables/left-join.gif)

The first and last rows have matching values of `c2`. The middle rows do not match. The final result will keep all rows of the first table but will omit the un-matched row from the second table.

This animation represents a table operation produced by the following command:

```
SELECT *
FROM table1
LEFT JOIN table2
  ON table1.c2 = table2.c2;
```

1. The first line selects all columns from both tables.
2. The second line selects `table1` (the “left” table).
3. The third line performs a `LEFT JOIN` on `table2` (the “right” table).
4. The fourth line tells SQL how to perform the join (by looking for matching values in column `c2`).



### Primary Key vs Foreign Key

Let’s return to our example of the magazine subscriptions. Recall that we had three tables: `orders`, `subscriptions`, and `customers`.

Each of these tables has a column that uniquely identifies each row of that table:

- `order_id` for `orders`
- `subscription_id` for `subscriptions`
- `customer_id` for `customers`

These special columns are called **primary keys**.

**Primary keys have a few requirements**:

- None of the values can be `NULL`.
- Each value must be unique (i.e., you can’t have two customers with the same `customer_id` in the `customers` table).
- A table can not have more than one primary key column.

Let’s reexamine the `orders` table:

| order_id | customer_id | subscription_id | purchase_date |
| -------- | ----------- | --------------- | ------------- |
| 1        | 2           | 3               | 2017-01-01    |
| 2        | 2           | 2               | 2017-01-01    |
| 3        | 3           | 1               | 2017-01-01    |

Note that `customer_id` (the primary key for `customers`) and `subscription_id` (the primary key for `subscriptions`) both appear in this.

**When the primary key for one table appears in a different table, it is called a *foreign key***.

So `customer_id` is a primary key when it appears in `customers`, but a foreign key when it appears in `orders`.

In this example, our primary keys all had somewhat descriptive names. Generally, the primary key will just be called `id`. Foreign keys will have more descriptive names.

*Why is this important?* The most common types of joins will be joining a foreign key from one table with the primary key from another table. For instance, when we join `orders` and `customers`, we join on `customer_id`, which is a foreign key in `orders` and the primary key in `customers`.



### Cross Join

So far, we’ve focused on matching rows that have some information in common.

Sometimes, we just want to combine all rows of one table with all rows of another table.

For instance, if we had a table of `shirts` and a table of `pants`, we might want to know **all the possible combinations to create different outfits**.

Our code might look like this:

```
SELECT shirts.shirt_color,
   pants.pants_color
FROM shirts
CROSS JOIN pants;
```

- The first two lines select the columns `shirt_color` and `pants_color`.
- The third line pulls data from the table `shirts`.
- The fourth line performs a `CROSS JOIN` with `pants`.

**Notice that cross joins don’t require an `ON` statement**. You’re not really joining on any columns!

If we have 3 different shirts (white, grey, and olive) and 2 different pants (light denim and black), the results might look like this:

| shirt_color | pants_color |
| ----------- | ----------- |
| white       | light denim |
| white       | black       |
| grey        | light denim |
| grey        | black       |
| olive       | light denim |
| olive       | black       |



3 shirts × 2 pants = 6 combinations!

This clothing example is fun, but it’s not very practically useful.

**A more common usage of `CROSS JOIN` is when we need to compare each row of a table to a list of values.**

Let’s return to our `newspaper` subscriptions. This table contains two columns that we haven’t discussed yet:

- `start_month`: the first month where the customer subscribed to the print newspaper (i.e., `2` for February)
- `end_month`: the final month where the customer subscribed to the print newspaper

Suppose we wanted to know how many users were subscribed during each month of the year. For each month (`1`, `2`, `3`) we would need to know if a user was subscribed. We can use a `CROSS JOIN` to solve this problem.



### Union

Sometimes we just want to stack one dataset on top of the other. Well, the `UNION` operator allows us to do that.

Suppose we have two tables and they have the same columns.

`table1`:

| pokemon    | type  |
| ---------- | ----- |
| Bulbasaur  | Grass |
| Charmander | Fire  |
| Squirtle   | Water |

`table2`:

| pokemon | type   |
| ------- | ------ |
| Snorlax | Normal |

If we combine these two with `UNION`:

```
SELECT *
FROM table1
UNION
SELECT *
FROM table2;
```

The result would be:

| pokemon    | type   |
| ---------- | ------ |
| Bulbasaur  | Grass  |
| Charmander | Fire   |
| Squirtle   | Water  |
| Snorlax    | Normal |

SQL has strict rules for appending data:

- Tables must have the same number of columns.
- The columns must have the same data types in the same order as the first table.



### With

Often times, we want to combine two tables, but one of the tables is the result of another calculation.

Let’s return to our magazine order example. Our marketing department might want to know a bit more about our customers. For instance, they might want to know how many magazines each customer subscribes to. We can easily calculate this using our `orders` table:

```
SELECT customer_id,
   COUNT(subscription_id) AS 'subscriptions'
FROM orders
GROUP BY customer_id;
```

This query is good, but a `customer_id` isn’t terribly useful for our marketing department, they probably want to know the customer’s name.

We want to be able to join the results of this query with our `customers` table, which will tell us the name of each customer. We can do this by using a `WITH` clause.

```
WITH previous_results AS (
   SELECT ...
   ...
   ...
   ...
)
SELECT *
FROM previous_results
JOIN customers
  ON _____ = _____;
```

- The `WITH` statement allows us to perform a separate query (such as aggregating customer’s subscriptions)
- `previous_results` is the alias that we will use to reference any columns from the query inside of the `WITH` clause
- We can then go on to do whatever we want with this temporary table (such as join the temporary table with another table)

Essentially, we are putting a whole first query inside the parentheses `()` and giving it a name. After that, we can use this name as if it’s a table and write a new query *using* the first query.



### Review

In this lesson, we learned about relationships between tables in relational databases and how to query information from multiple tables using SQL.

Let’s summarize what we’ve learned so far:

- `JOIN` will combine rows from different tables if the join condition is true.
- `LEFT JOIN` will return every row in the *left* table, and if the join condition is not met, `NULL` values are used to fill in the columns from the *right* table.
- *Primary key* is a column that serves a unique identifier for the rows in the table.
- *Foreign key* is a column that contains the primary key to another table.
- `CROSS JOIN` lets us combine all rows of one table with all rows of another table.
- `UNION` stacks one dataset on top of another.
- `WITH` allows us to define one or more temporary tables that can be used in the final query.

Download the [Multiple Tables: Cheat Sheet](https://www.codecademy.com/learn/learn-sql/modules/learn-sql-multiple-tables/reference) to help you remember the content covered in this lesson.