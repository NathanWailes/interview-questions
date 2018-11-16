select parents.name as parent_name, min(children.age) from
(select name, id from people where id in (select distinct(fatherId) from people) or id in (select distinct(motherId) from people)) parents
join (select * from people where fatherId is not null or motherId is not null) children