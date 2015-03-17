#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
# Method:
# Utility functions connect to the tournament database, and adds, delete, and count players and matches
# Standings function returns a list of players sorted by number of wins
# Swisspairings function returns a list of players who will play in next match based on win records
#
# function names and initial descriptions provided by Udacity
# function definitions written by Sarah L. Duncan 3/17/2015
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    tournamentDB=connect()
    cursor=tournamentDB.cursor()
    cursor.execute("DELETE FROM matches;")
    tournamentDB.commit()
    tournamentDB.close()

def deletePlayers():
    """Remove all the player records from the database."""
    tournamentDB=connect()
    cursor=tournamentDB.cursor()
    cursor.execute("DELETE FROM players;")
    tournamentDB.commit()
    tournamentDB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    tournamentDB=connect()
    cursor=tournamentDB.cursor()
    cursor.execute("SELECT COUNT (*) FROM players;")
    player_count=cursor.fetchall()[0][0]
    tournamentDB.close()
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    Method: Inserting the player name into the database causes it to assign a unique serial id number for the player.
  
    Args:
      name: the player's full name (need not be unique).
    """
    tournamentDB=connect()
    cursor=tournamentDB.cursor()
    cursor.execute("INSERT INTO players (player_name) VALUES (%s);", (name,))
    tournamentDB.commit()
    tournamentDB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list is the player in first place, or a player
    tied for first place if there is currently a tie.
    Method:
      Use standings view to count the number of wins and matches for each player
      Sort them by the number of wins
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    tournamentDB=connect()
    cursor=tournamentDB.cursor()
    cursor.execute("SELECT player_id, player_name, wins, matches_played FROM standings ORDER BY wins DESC;")
    standings=cursor.fetchall()
    tournamentDB.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Method: 
      For each match that is played, insert a set of winner and loser ids from the players table into the matches table
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    tournamentDB=connect()
    cursor=tournamentDB.cursor()
    cursor.execute("INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s);", (winner, loser))
    tournamentDB.commit()
    tournamentDB.close()

 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Method:
      Get a list of tuples sorted by number of wins from the standings function
      Each tuple contains (id, name, wins, matches) 
      Loop through the list two tuples at a time, creating a new tuple of 2 names and ids who will play 
      each other in the next set of matches
      Append the new tuple to the list of pairings
      Return the list of pairings when all standings have been processed
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    standings = playerStandings()
    npairings=len(standings)/2
    np=0
    pairings=[]
    while np < npairings:
        p=(standings[2*np][0],standings[2*np][01],standings[(2*np) +1][0],standings[(2*np) + 1][1])
        pairings.append(p)
        np += 1
    return pairings

    