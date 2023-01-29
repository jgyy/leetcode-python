USE mysql;
Create table If Not Exists Logs (id int, num int);
Truncate table Logs;
insert into Logs (id, num)
values ('1', '1');
insert into Logs (id, num)
values ('2', '1');
insert into Logs (id, num)
values ('3', '1');
insert into Logs (id, num)
values ('4', '2');
insert into Logs (id, num)
values ('5', '1');
insert into Logs (id, num)
values ('6', '2');
insert into Logs (id, num)
values ('7', '2');
-- Write an SQL query to find all numbers that appear at least three times consecutively.
select distinct l1.num AS 'ConsecutiveNums'
from Logs l1,
    Logs l2,
    Logs l3
where l1.id + 1 = l2.id
    and l2.id + 1 = l3.id
    and l1.num = l2.num
    and l2.num = l3.num;