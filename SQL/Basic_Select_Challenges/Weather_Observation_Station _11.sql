select distinct city from station
where SUBSTR(city, 1, 1) not in ('a', 'e', 'i', 'o', 'u')
or SUBSTR(city, -1) not in ('a', 'e', 'i', 'o', 'u');