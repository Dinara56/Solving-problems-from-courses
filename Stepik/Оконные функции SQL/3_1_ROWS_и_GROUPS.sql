/*
В общем виде определение фрейма выглядит так:

ROWS BETWEEN frame_start AND frame_end

Начало фрейма (frame_start) может быть:

- current row — начиная с текущей строки;
- N preceding — начиная с N-й строки перед текущей;
- N following — начиная с N-й строки после текущей;
- unbounded preceding — начиная с границы секции.

Аналогично, конец фрейма (frame_end) может быть:

- current row — до текущей строки;
- N preceding — до N-й строки перед текущей;
- N following — до N-й строки после текущей;
- unbounded following — до границы секции.

На самом деле, кроме фрейма по строкам (ROWS) бывают еще фреймы по группам (GROUPS) и диапазону (RANGE):

ROWS BETWEEN frame_start AND frame_end
GROUPS BETWEEN frame_start AND frame_end
RANGE BETWEEN frame_start AND frame_end

Инструкции для границ группового фрейма используются такие же, как для строкового, но смысл их отличается:

current row — текущая группа (а не текущая строка);
N preceding / following — N-я группа относительно текущей (а не N-я строка);
unbounded preceding / following — граница секции (как у строкового фрейма).
*/

/*
Задача: Есть таблица сотрудников employees. Напишите запрос, который для каждого сотрудника выведет:
размер з/п предыдущего по зарплате сотрудника (среди коллег по департаменту);
максимальную з/п по департаменту.
Если «предыдущего коллеги» нет (у сотрудника самая низкая зарплата в департаменте) — запрос должен возвращать зарплату самого сотрудника.
*/

select id, name, department, salary, 
lag(salary, 1, salary) over(partition by department) as prev_salary, 
max(salary) over w as max_salary
from employees
window w as (
    partition by department
    rows between unbounded preceding and unbounded following
)
order by department, salary, id

/*
Задача: Есть таблица сотрудников employees. Для каждого человека мы хотим посчитать количество сотрудников, 
которые получают такую же или большую зарплату (ge_cnt)
*/

select id, name, salary, round(cume_dist() over w * 10, 2) as ge_cnt
from employees
window w as (
    order by salary desc
)
order by salary, id

/*
Задача: Есть таблица сотрудников employees. Для каждого человека мы хотим увидеть ближайшую большую зарплату (next_salary)
*/

select id, name, salary, max(salary) over w as next_salary
from employees
window w as (
  order by salary desc
  groups between 1 preceding and 1 preceding
)
order by salary, id