/*
Оконные функции для расчета статистик:

- cume_dist()	процент строк, которые меньше либо равны текущей
- percent_rank()	процент строк, которые строго меньше текущей
- percentile_disc(N)	N-й процентиль дискретного распределения
- percentile_cont(N)	N-й процентиль непрерывного распределения

percentile_disc рассматривает набор данных как дискретный (то есть состоящий из отдельных значений). Всегда возвращает конкретное значение из тех, что есть в таблице.
percentile_cont рассматривает набор данных как непрерывный (как будто значения в наборе — это выборка из некоторого непрерывного распределения данных). Рассчитывает процентиль аналитически по формуле.

Процентиль как функция агрегации задается так:

percentile_disc(PERCENT) within group (order by COLUMN) over (partition by OTHER_COLUMNS)
Где PERCENT — порог процентиля (десятичная дробь от 0 до 1), а COLUMN — столбец, по которому считается процентиль.
*/

/*
Задача: Напишите запрос, который рассчитает cume_dist (cd) и percent_rank (pr) по температуре для всех дней марта, 
и вернет пять дней с самой высокой температурой
*/

select wdate, wtemp, 
round(cume_dist() over w, 2) as cd, 
round(percent_rank() over w, 2) as pr
from (
    select * from weather where month(wdate) = 3
) temp_table
window w as (order by wtemp)
order by wtemp desc
limit 5

/*
Задача: Хотим для каждого из дней с 1 по 5 марта определить, какой процент дней в марте имеют такую же или меньшую температуру.
*/

select wdate, wtemp, perc
from (
  select wdate, wtemp, round(cume_dist() over w, 2) as perc
  from weather 
  window w as (order by wtemp)
  where month(wdate) = 3 
) temp_table
where day(wdate) between 1 and 5
order by wdate

/*
Задача: Хотим для седьмого числа каждого месяца (7 января, 7 февраля, 7 марта ...) определить, какой процент дней в 
соответствующем месяце имеют такую же или меньшую температуру
*/

select *
from (
  select wdate, wtemp, 
  round(cume_dist() over w, 2) as perc
  from weather 
  window w as (
      partition by month(wdate)
      order by wtemp
  )
) temp_data
where day(wdate) = 7

/*
Задача: Напишите запрос, который рассчитает среднее арифметическое, медиану и 90-й процентиль температуры по каждому месяцу.
*/

select extract(month from wdate) as wmonth,
round(avg(wtemp)::decimal, 2) as t_avg,
percentile_disc(0.50) within group (order by wtemp) as t_med,
percentile_disc(0.90) within group (order by wtemp) as t_p90
from weather
group by extract(month from wdate)
