/*
Напишите SQL запрос для формирования списка рассылки. Всего планируется три тестовых письма, которые следует пронумеровать от 1 до 3-х с 
равномерным распределением чисел между пользователями таблицы users. Распределять письма будем в порядке следования идентификаторов, то есть 
первый блок пользователей получит единицу, следующий двойку и последний тройку.
Номер варианта следует вывести в первой колонке с названием mail_variant, далее выведите id пользователя, его email и имя. Итоговые данные отсортируйте по id.
*/

select ntile(3) over(order by id) as mail_variant, id, email, first_name
from users
order by id

/*
Перепишите SQL запрос из прошлого урока. Сделайте, чтобы функция NTILE распределяла пользователей на 4 группы, а данные обрабатывались в порядке следования 
MD5 хэшей от email пользователей.
Порядок и состав полей оставьте как в прошлой задаче, а итоговые данные отсортируйте по id.
*/

select ntile(4) over(order by MD5(email)) as mail_variant, id, email, first_name
from users
order by id

/*
Напишите SQL запрос, который выведет 5 колонок: name — название магазина, first_name — имя покупателя, last_name — фамилия покупателя, amount — общая сумма 
выполненных заказов (status="success") покупателя в текущем магазине, c_level — группа (уровень) покупателя.
Всех покупателей магазин делит на четыре равные группы, нумеруя их от 1 (потратили больше всего) до 4 (потратили меньше всего). При этом для каждого магазина 
группы считаются по отдельности.
Итоговые данные отсортируйте по названию магазина, а после по группам в возрастающем порядке.
*/

select s.name, u.first_name, u.last_name, sum(o.amount) as amount, 
NTILE(4) over(partition by s.name ORDER BY SUM(amount) DESC) as c_level
from orders o join users u on o.user_id = u.id
join shops s on o.shop_id = s.id
where o.status = 'success'
group by s.id, u.id
order by s.name, c_level

/*
Напишите SQL запрос, который выведет 4 колонки: month — номер месяца, first_name — имя покупателя, last_name — фамилия покупателя, amount — общая сумма 
выполненных заказов (status="success") покупателя в текущем месяце. c_level выводить не нужно, так как нам интересны только покупатели из первой группы.
Итоговые данные отсортируйте по месяцу, а после по сумме заказа в возрастающем порядке.
*/

select month, first_name, last_name, amount
from (
    select month(date) as month, u.first_name, u.last_name, sum(o.amount) as amount,
    NTILE(4) over(partition by month(date) ORDER BY SUM(amount) DESC) as c_level
    from orders o join users u on o.user_id = u.id
    join shops s on o.shop_id = s.id
    where o.status = 'success'
    group by month, u.id
    order by month, amount
) temp_table
where c_level = 1