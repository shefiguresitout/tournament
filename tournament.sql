-- Table definitions for the tournament project.
--
-- SQL configuration for a tournament database
-- Database has two tables
-- Players table has names and player id numbers
-- Matches table has match id numbers and references to players table, using player ids to denote winner
-- and loser of each match

-- Standings view is used to generate a table of standings from matches played
-- with the player's id, name, number of wins, and total number of matches played
-- Because it uses left joins, even when no matches have yet been played, it will return
-- 0 for number of wins and total number of matches played

--Author: Sarah L. Duncan 3/17/2015
--Written for Udacity Full Stack Developer Project 2

CREATE TABLE players (player_id serial PRIMARY KEY, player_name text);

CREATE TABLE matches (match_id serial PRIMARY KEY, winner_id int references players (player_id), loser_id int references players (player_id));

CREATE VIEW standings AS
SELECT
players.player_id,
players.player_name,
count(match_winner.winner_id) AS wins,
count(match_winner.winner_id) + count(match_loser.loser_id) as matches_played
FROM players
LEFT JOIN matches match_winner ON players.player_id = match_winner.winner_id
LEFT JOIN matches match_loser ON players.player_id = match_loser.loser_id
GROUP BY players.player_id;


