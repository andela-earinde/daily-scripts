select animals.name, animals.species, diet.food from animals inner join diet on animals.species = diet.species where food = 'plants';
