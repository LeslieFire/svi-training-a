SELECT * FROM pet;

UPDATE pet 
	SET name = "Anton's Pet" WHERE id IN (
	SELECT pet.id
	FROM pet, person, person_pet
	WHERE
	pet.id = person_pet.pet_id AND
	person_pet.person_id = person.id AND
	person.last_name = "Ortiz"
);
SELECT * FROM pet;

