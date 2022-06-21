select distinct city from station
where SUBSTR(city, -1) not in ('a', 'e', 'i', 'o', 'u');