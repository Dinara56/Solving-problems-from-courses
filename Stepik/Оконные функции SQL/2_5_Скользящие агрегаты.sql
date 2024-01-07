/*
Фрейм. В общем случае определение фрейма выглядит так:

rows between X preceding and Y following

- Где X — количество строк перед текущей, а Y — количество строк после текущей
- Если указать вместо X или Y значение unbounded — это значит «граница секции»
- Если указать вместо X preceding или Y following значение current row — это значит «текущая запись»

Скользящие агрегаты используют те же самые функции, что и агрегаты обычные:

- min() и max()
- count(), avg() и sum()
- group_concat()
*/

/*
Задача: Есть таблица доходов-расходов expenses. 
Мы хотим рассчитать скользящее среднее по доходам за предыдущий и текущий месяц
*/

select
  year, month, income,
  round(avg(income) over w) as roll_avg
from expenses
window w as (
  order by year, month
  rows between 1 preceding and current row
)
order by year, month;

/*
Задача: Мы хотим посчитать фонд оплаты труда нарастающим итогом независимо для каждого департамента.
*/

select
  id, name, department, salary,
  sum(salary) over w as total
from employees
window w as (
  partition by department
  rows between unbounded preceding and current row
)
order by department, salary, id