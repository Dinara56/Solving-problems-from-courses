/*
FILTER работает как обычное условие WHERE, но фильтрует не все записи запроса, а только фрейм для конкретной оконной функции. 

В общем случае конструкция CASE выглядит так:

CASE
  WHEN условие1 THEN результат1
  WHEN условие2 THEN результат2
  ...
  WHEN условиеN THEN результатN
  ELSE результат_иначе
END
*/

/*
Задача: Xотим посчитать, сколько процентов составляет зарплата сотрудника от средней по Москве и средней по Самаре. 
*/

select
  id, name, salary,
  round(salary * 100 / avg(salary) over ()) as "perc",
  round(salary * 100 / avg(salary) filter(where city = 'Москва') over ()) as msk,
  round(salary * 100 / avg(salary) filter(where city = 'Самара') over ()) as sam
from employees
order by id;

/*
Задача: Есть запрос, который считает зарплатный фонд города без учета IT-отдела:

select
  name, city,
  sum(salary) over w as base,
  sum(salary) filter(where department <> 'it') over w as no_it
from employees
window w as (partition by city)
order by city, id;

Перепишите запрос так, чтобы он использовал case вместо filter.
*/

select
  name, city,
  sum(salary) over w as base,
  sum(case when department != 'it' then salary end) over w as no_it
from employees
window w as (
    partition by city
)
order by city, id;

/*
Есть запрос, который считает зарплатный фонд города:

select
  name, city,
  sum(salary) over w as base
from employees
window w as (partition by city)
order by city, id;

Добавьте столбец alt с зарплатным фондом, рассчитанным по следующим правилам:

- для сотрудников отдела hr умножаем зарплату на 2;
- для сотрудников отдела it делим зарплату на 2;
- для сотрудников отдела sales не меняем зарплату.
*/

select
  name, city,
  sum(salary) over w as base, 
sum(case
    when department = 'hr' then salary*2
    when department = 'it' then salary/2
    when department = 'sales' then salary 
end) over w as alt
from employees
window w as (
    partition by city
)
order by city, id;