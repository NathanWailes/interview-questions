-- https://stackoverflow.com/a/1037702/4115031
select customers.name, count(transactions.id)
from customers left join transactions
on customers.id = transactions.customerId
group by customers.id