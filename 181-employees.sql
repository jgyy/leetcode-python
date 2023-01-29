USE mysql Create table If Not Exists Employee (
    id int,
    name varchar(255),
    salary int,
    managerId int
);
Truncate table Employee;
insert into Employee (id, name, salary, managerId)
values ('1', 'Joe', '70000', '3');
insert into Employee (id, name, salary, managerId)
values ('2', 'Henry', '80000', '4');
insert into Employee (id, name, salary, managerId)
values ('3', 'Sam', '60000', 'None');
insert into Employee (id, name, salary, managerId)
values ('4', 'Max', '90000', 'None');
-- Write an SQL query to find the employees who earn more than their managers.
select e1.name as Employee
from Employee e1,
    Employee e2
where e1.managerId = e2.id
    and e1.salary > e2.salary;