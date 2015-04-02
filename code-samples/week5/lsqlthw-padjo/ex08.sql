DELETE FROM pet WHERE id in (
	SELECT pet.id
	FROM pet, person, person_pet
	WHERE
	person_pet.person_id = person.id AND
	pet.id = person_pet.pet_id AND
	person.first_name = "Anton"
);

SELECT * FROM pet;
SELECT * FROM person_pet;

DELETE FROM person_pet
	WHERE pet_id NOT IN (
		SELECT id FROM pet
	);

SELECT * FROM person_pet;