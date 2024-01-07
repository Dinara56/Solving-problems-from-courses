/*
Функции ранжирования:

row_number() - порядковый номер строки
dense_rank() - ранг строки
rank() - тоже ранг, но с пропусками
ntile(n) - разбивает все строки на n групп и возвращает номер группы, в которую попала строка
*/

/*
Задача: Есть таблица сотрудников employees. В компании работают сотрудники из Москвы и Самары. 
Мы хотим разбить их на две группы по зарплате в каждом из городов.
*/

select ntile(2) over(partition by city order by salary) as tile, name, city, salary
from employees
order by city, salary

/*
Задача: Есть таблица сотрудников employees. Мы хотим узнать самых высокооплачиваемых людей по каждому департаменту.
*/

select id, name, department, salary
from (
    select dense_rank() over(partition by department order by salary desc) as rn, id, name, department, salary
    from employees
) table_temp
where rn = 1