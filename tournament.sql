-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE players (player_id serial PRIMARY KEY, player_name text);


CREATE TABLE matches (match_id serial PRIMARY KEY, winner_id int references players (player_id), loser_id int references players (player_id));

CREATE VIEW standingsjoin AS 
SELECT 
players.player_id, 
players.player_name, 
count(matches.winner_id) 
AS wins 
FROM players LEFT JOIN matches 
ON players.player_id = matches.winner_id
GROUP BY players.player_id;


CREATE VIEW standingssubselect AS 
SELECT players.player_id, players.player_name,
(SELECT count(*)
FROM matches
where players.player_id = matches.winner_id)
AS wins,
(SELECT count(*)
FROM matches
where players.player_id = matches.loser_id)
AS losses
FROM players
ORDER BY wins DESC;

