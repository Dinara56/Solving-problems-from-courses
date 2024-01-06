/*
Напишите SQL-запрос, который выведет пять столбцов: place — место спортсмена, last_name — фамилию, first_name — имя, time — 
время преодоления дистанции в формате ЧЧ:ММ:СС и champion_lag — время отставания от первого места в формате ЧЧ:ММ:СС
Данные отсортируйте по занятому месту — чемпионы сверху.
*/

select row_number() over() as place, last_name, first_name, time, 
TIME_FORMAT(TIMEDIFF(time, first_lag), '%H:%i:%s') as champion_lag
from (
    select last_name, first_name, 
    TIME_FORMAT(TIMEDIFF(end_time, start_time), '%H:%i:%s') as time,
    FIRST_VALUE(TIME_FORMAT(TIMEDIFF(end_time, start_time), '%H:%i:%s')) over(order by TIME_FORMAT(TIMEDIFF(end_time, start_time), '%H:%i:%s')) as first_lag
    from runners
) temp_table
order by place