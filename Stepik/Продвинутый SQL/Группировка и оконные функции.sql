/*
Наша задача подготовить эти данные для составления налоговой декларации.
Особенность декларации в том, что данные в ней указываются поквартально нарастающим итогом.
Поможем предпринимателю с декларацией. Напишите SQL запрос, который выведет 4 столбца: quarter — номер квартала, 
income — суммарные поступления за этот квартал, income_acc — поступления за квартал нарастающим итогом и usn6 — величина 
налога нарастающим итогом. При системе налогообложения УСН 6% начисляется 6% налог на все доходы. Выведете налоги с двумя знаками после десятичной точки.
*/

select 
    QUARTER(date) AS quarter, 
    sum(income) AS income,
    sum(sum(income)) OVER(ORDER BY QUARTER(date)) AS income_acc,
    ROUND(0.06 * (sum(sum(income)) over (ORDER BY QUARTER(date))), 2) AS usn6
from 
    transactions
group by QUARTER(date)
ORDER BY QUARTER(date)

/*
Сгруппируйте данные в таблице users по полу и получите количество мужчин и женщин, а также их процентное соотношение к общему числу людей.
В первой колонке (sex) выведите пол, во второй (members) — количество , а в третьей (percent) — процент. Данные отсортируйте по последнему столбцу.
*/

select *, members * 100 / sum(members) over()  as percent 
from (
        select 'm' as sex, count(sex) as members
        from users
        where sex = 'm'
    union 
        select 'w' as sex, count(sex) as members
        from users
        where sex = 'w'
) temp_table
order by percent

/*
Сгруппируйте данные в таблице users по возрасту и получите количество и процент клиентов каждого возраста.
В первом столбце (age_num) выведете порядковый номер возраста, во втором (age) — сам возраст, в третьем (clients) — количество клиентов 
данного возраста, а в четвертом (percent) — процент клиентов данного возраста.
Данные отсортируйте по возрасту в возрастающем порядке.
*/

select row_number() over() as age_num, age, clients, clients * 100 / sum(clients) over() as percent
from (
    select age, count(age) as clients
    from users
    group by age
    order by age
) temp_table

/*
В таблице orders хранится список заказов компании. Напишите запрос, который в первом столбце (year) — выведет год, во втором (status) — статус заказа, 
в третьем (orders) — общее количество заказов данного статуса за соответствующий год, а в четвертом (percent) — процент в рамках соответствующего года.
Данные отсортируйте по году и по статусу в алфавитном порядке.
*/

select *, orders * 100 / sum(orders) over(partition by year) as percent
from (
    select *
    from (
        select year(date) as year, status, count(status) over(partition by status, year(date)) as orders
        from orders
        order by year, status
    ) temp_table
    group by year, status, orders
) new_temp_table

/*
В таблице orders хранится список заказов компании. Напишите запрос, который в первом столбце (year) — выведет год, во втором (user_id) — 
идентификатор пользователя, в третьем (amount) — сумму выполненных (success) заказов за текущий год для этого пользователя, а в четвертом (percent) — 
вклад пользователя в процентах в общую сумму доходов в рамках текущего года.
Данные отсортируйте по году и по вкладу пользователя в возрастающем порядке.
*/

select *, amount * 100 / sum(amount) over(partition by year) as percent
from (
    select year(date) as year, user_id, sum(sum(amount)) over(partition by user_id, year(date)) as amount
    from orders
    where status = 'success'
    group by year, user_id
) temp_table
order by year, percent