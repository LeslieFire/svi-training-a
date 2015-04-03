ALTER TABLE person ADD COLUMN dead INTEGER;
ALTER TABLE person ADD COLUMN phone_number INTEGER;
ALTER TABLE person ADD COLUMN salary FLOAT;
ALTER TABLE person ADD COLUMN dob DATETIME;

ALTER TABLE pet ADD COLUMN parent INTEGER;

ALTER TABLE person_pet ADD COLUMN purchased_on DATETIME;

INSERT INTO person (id, first_name, last_name, age, dead, phone_number, salary, dob)
	VALUES (0, 'Antonio', 'Ortiz', '25', 0, '12345', 'programmer', '2000-10-03');

INSERT INTO person (id, first_name, last_name, age, dead, phone_number, salary, dob)
	VALUES (1, 'Kyle', 'Bringas', '26', 0, '12045', 'Sales', '2001-10-04');

INSERT INTO person (id, first_name, last_name, age, dead, phone_number, salary, dob)
	VALUES (2, 'Noel', 'Tolosa', '24', 0, '32345', 'Sales', '1997-07-03');

INSERT INTO pet (id, name, breed, age, dead, dob, parent)
	VALUES (0, 'Corby', 'labrador', 13, 0, '1990-12-12', NULL);

INSERT INTO pet (id, name, breed, age, dead, dob, parent)
	VALUES (1, 'Jack', 'labrador', 10, 0, '1990-12-12', 1);

INSERT INTO pet (id, name, breed, age, dead, dob, parent)
	VALUES (2, 'Saki', 'labrador', 9, 0, '1990-12-12', 1);

INSERT INTO person_pet (person_id, pet_id, purchased_on)
	VALUES (0,0, "2000-12-12");

INSERT INTO person_pet (person_id, pet_id, purchased_on)
	VALUES (1,1, "2000-12-12");

INSERT INTO person_pet (person_id, pet_id, purchased_on)
	VALUES (2,2, "2000-12-12");

SELECT person.first_name, pet.name
	FROM pet, person, person_pet
	WHERE
	pet.id = person_pet.pet_id AND
	person_pet.person_id = person.id AND
	person_pet.purchased_on > '2004';

SELECT name
	FROM pet
	WHERE
	pet.parent = 1;