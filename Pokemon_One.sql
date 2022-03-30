CREATE TABLE Pokemon (	name varchar,
	id int,
	height varchar,
	weight int,
	ability varchar,
	species varchar,
	primary_type varchar,
	secondary_type varchar,
	official_artwork varchar
);
ALTER TABLE Pokemon ADD PRIMARY KEY (name);
CREATE TABLE Stats (	name varchar,
	hp int,
	attack int,
	defense int,
	special-attack int,
	special-defense int,
	speed int
);
ALTER TABLE Stats ADD PRIMARY KEY (name);
INSERT INTO Pokemon VALUES ('clefairy', 35, 6, 75, 'cute-charm', 'Fairy Pokémon', 'fairy', 'none', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/35.png');
INSERT INTO Stats VALUES ('clefairy', 70, 45, 48, 60, 65, 35);
