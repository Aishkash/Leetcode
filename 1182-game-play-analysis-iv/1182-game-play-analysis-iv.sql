select round((count(c.player_id))/(count(distinct d.player_id)),2) as fraction
from (
         select player_id,
                min(event_date) as d_date
         from activity   
         group by player_id
     ) as d
left join activity c
       on d.player_id = c.player_id
      and datediff(c.event_date, d.d_date) = 1;