select customers.name, count(transactions.id)
from customers left join transactions