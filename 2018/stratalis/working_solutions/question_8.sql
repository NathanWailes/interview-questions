select fathers.name as parent_name, min(children.age) from
(select name, id from people where id in (select distinct(fatherId) from people)) fathers
join (select * from people where fatherId is not null) children on fathers.id = children.fatherId
union
select mothers.name as parent_name, min(children.age) from
(select name, id from people where id in (select distinct(motherId) from people)) mothers
join (select * from people where motherId is not null) children on mothers.id = children.motherId