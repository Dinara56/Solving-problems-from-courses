/*
Стандарт SQL предусматривает четыре разновидности EXCLUDE:

EXCLUDE NO OTHERS. Ничего не исключать. Вариант по умолчанию: если явно не указать exclude, сработает именно он.
EXCLUDE CURRENT ROW. Исключить текущую запись (как мы сделали на предыдущем шаге с сотрудником).
EXCLUDE GROUP. Исключить текущую запись и все равные ей (по значению столбцов из order by).
EXCLUDE TIES. Оставить текущую запись, но исключить равные ей.
*/

/*
Задача: Допустим, мы хотим понять, как изменится средняя зарплата по организации, если уволить того или иного сотрудника. 
*/

select
  name, salary,
  round(avg(salary) over w) as "avg"
from employees
window w as (
  rows between unbounded preceding and unbounded following
  exclude current row
)
order by salary, id;

/*
Задача: Есть таблица сотрудников employees. Предположим, для каждого человека мы хотим посчитать среднюю зарплату сотрудников, 
которые получают столько же или больше, чем он — но не более чем +20 тыс. ₽ (p20_sal). При этом зарплату самого сотрудника учитывать не следует
*/

select id, name, salary, round(avg(salary) over w) as p20_sal
from employees
window w as (
  order by salary
  range between current row and 20 following
  exclude CURRENT ROW
)
order by salary, id