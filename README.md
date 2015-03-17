Swiss Pairing Tournament Project

Files:
configure_tournament_db.psql
configure_tournament.sh
tournament.py
tournament.sql

To use this software, run configure_tournament.sh.  This will use plsql commands in configure_tournament_db.psql, which in turn runs sql commands in tournament.sql, to create and configure a sql database for a tournament run with the Swiss Pairing system.  For more information on Swiss Pairings, see this [Wikipedia page:](http://en.wikipedia.org/wiki/Swiss-system_tournament)

tournament.py has all necessary functions for adding players, reporting matches, and generating lists, based on players' win records, of players who should play each other in subsequent rounds.


