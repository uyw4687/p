select *
from (select name "users.name", distance_traveled from (select user_id, sum(distance) AS distance_traveled from rides group by user_id) grouped_distance join users on(users.id=grouped_distance.user_id) order by distance_traveled desc, name) relation
where rownum<=100;