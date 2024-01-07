/*
Оконные функции агрегации:

min(value) - минимальное value среди строк, входящих в окно
max(value) - максимальное value
count(value) - количество value , не равных null
avg(value) - среднее значение по всем value
sum(value) - сумма значений value
group_concat(value, separator) - строка, которая соединяет значения value через разделитель separator (только SQLite)
string_agg(value, separator) - аналог group_concat() в PostgreSQL

Порядок выполнения операций:

1) Взять нужные таблицы (from) и соединить их при необходимости (join).
2) Отфильтровать строки (where).
3) Сгруппировать строки (group by).
4) Отфильтровать результат группировки (having).
5) Взять конкретные столбцы из результата (select).
6) Рассчитать значения оконных функций (function() over window).
7) Отсортировать то, что получилось (order by).
*/

/*
Задача: Есть таблица сотрудников employees. Мы хотим для каждого сотрудника увидеть, сколько процентов составляет его зарплата от общего фонда труда по городу.
*/

select name, city, salary, sum(salary) over w as fund,
round(salary * 100 / sum(salary) over w) as perc
from employees
window w as (
    partition by city
)
order by city, salary

/*
Задача: Есть таблица сотрудников employees. Мы хотим для каждого сотрудника увидеть:
- сколько человек трудится в его отделе (emp_cnt);
- какая средняя зарплата по отделу (sal_avg);
- на сколько процентов отклоняется его зарплата от средней по отделу (diff).
*/

select name, department, salary, 
count(name) over w as emp_cnt, 
round(avg(salary) over w) as sal_avg, 
round((salary - round(avg(salary) over w)) * 100.0 / round(avg(salary) over w)) as diff
from employees
window w as (
    partition by department
)
order by department, salary, id

/*
Задача: Оставить в отчете только самарских сотрудников
*/

with emp as (
  select
    name, city, salary,
    sum(salary) over w as fund
  from employees
  window w as (partition by department)
  order by department, salary, id
)
select name, salary, fund
from emp
where city = 'Самара'