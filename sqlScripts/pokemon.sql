CREATE TABLE Pokemon (	name varchar,
	id int,
	height varchar,
	weight int,
	ability varchar,
	species varchar,
	primary_type varchar,
	secondary_type varchar
);
ALTER TABLE Pokemon ADD PRIMARY KEY (name);
INSERT INTO Pokemon VALUES ('bulbasaur', 1, 7, 69, 'overgrow', 'Seed Pokémon', 'grass', 'poison');