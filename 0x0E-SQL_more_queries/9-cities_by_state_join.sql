-- Script that Lists all cities in db 'hbtn_0d_usa'
-- Each record should display cities.id, cities.name, and states.name
-- only one SELECT statement can be used
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id;
