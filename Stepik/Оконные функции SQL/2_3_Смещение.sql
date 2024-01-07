/*
Оконные функции смещения:

lag(value, offset) - значение value из строки, отстоящей на offset строк назад от текущей
lead(value, offset)	- значение value из строки, отстоящей на offset строк вперед от текущей
first_value(value) - значение value из первой строки фрейма
last_value(value) - значение value из последней строки фрейма
nth_value(value, n) - значение value из n-й строки фрейма

lag() и lead() действуют относительно текущей строки, заглядывая вперед или назад на указанное количество строк.
first_value(), last_value() и nth_value() действуют относительно границ фрейма, выбирая указанную строку в пределах фрейма.
*/

/*
Задача: Есть таблица сотрудников employees. Мы хотим для каждого сотрудника увидеть зарплаты предыдущего и следующего коллеги.
*/

select name, department, lag(salary, 1) over (order by salary, id) as prev, 
salary, lead(salary, 1) over (order by salary, id) as next
from employees
order by salary, id;

/*
Задача: Есть таблица сотрудников employees. Мы хотим для каждого сотрудника увидеть, сколько процентов составляет его зарплата от максимальной в городе.
*/

select name, city, salary, round(salary * 100 / hight) as percent
from(
    select *, last_value(salary) over w as hight
    from employees
    window w as (
        partition by city
        order by salary
        rows between unbounded preceding and unbounded following
    )
) temp_table
order by city, salary

