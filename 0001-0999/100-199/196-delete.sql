USE mysql;
Create table If Not Exists Person (Id int, Email varchar(255));
Truncate table Person;
insert into Person (id, email)
values ('1', 'john@example.com');
insert into Person (id, email)
values ('2', 'bob@example.com');
insert into Person (id, email)
values ('3', 'john@example.com');
-- Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.
DELETE p1
FROM Person p1
    INNER JOIN Person p2
WHERE p1.email = p2.email
    AND p1.id > p2.id;