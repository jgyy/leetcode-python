USE mysql;
Create table If Not Exists Weather (id int, recordDate date, temperature int);
Truncate table Weather;
insert into Weather (id, recordDate, temperature)
values ('1', '2015-01-01', '10');
insert into Weather (id, recordDate, temperature)
values ('2', '2015-01-02', '25');
insert into Weather (id, recordDate, temperature)
values ('3', '2015-01-03', '20');
insert into Weather (id, recordDate, temperature)
values ('4', '2015-01-04', '30');
-- Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
SELECT weather.id AS 'Id'
FROM weather
    JOIN weather w ON DATEDIFF(weather.recordDate, w.recordDate) = 1
    AND weather.Temperature > w.Temperature;