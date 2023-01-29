USE mysql;
Create table If Not Exists Employee (
    id int,
    name varchar(255),
    salary int,
    departmentId int
);
Create table If Not Exists Department (id int, name varchar(255));
Truncate table Employee;
insert into Employee (id, name, salary, departmentId)
values ('1', 'Joe', '70000', '1');
insert into Employee (id, name, salary, departmentId)
values ('2', 'Jim', '90000', '1');
insert into Employee (id, name, salary, departmentId)
values ('3', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId)
values ('4', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId)
values ('5', 'Max', '90000', '1');
Truncate table Department;
insert into Department (id, name)
values ('1', 'IT');
insert into Department (id, name)
values ('2', 'Sales');
-- Write an SQL query to find employees who have the highest salary in each of the departments.
select d.name as Department,
    e.name as Employee,
    e.salary as Salary
from Employee e
    join Department d on e.departmentId = d.id
where e.salary = (
        select max(salary)
        from Employee
        where departmentId = e.departmentId
    );