/*Find the ten oldest gorillas*/
select animals.species, animals.birthdate from animals where animals.species = 'gorilla' order by animals.birthdate desc limit 10;

select animals.name from animals order by animals.name limit 10;

select animals.species, count(animals.species) from animals group by animals.species order by count desc limit 1;


