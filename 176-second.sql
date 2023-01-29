USE mysql;
Create table If Not Exists Employee (id int, salary int);
Truncate table Employee;
insert into Employee (id, salary)
values ('1', '100');
insert into Employee (id, salary)
values ('2', '200');
insert into Employee (id, salary)
values ('3', '300');
-- Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary, the query should report null.
select (
        select distinct salary
        from Employee
        order by salary desc
        limit 1, 1
    ) as SecondHighestSalary;