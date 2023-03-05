select
    p.id,
    p.name,
    pos.title as pos_title
from Persons as p
left join Positions as pos on p.pos_id = pos.id;
