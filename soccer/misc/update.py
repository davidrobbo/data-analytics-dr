import sqlite3

conn = sqlite3.connect('./database.sqlite')

#conn.executescript('ALTER TABLE Match ADD COLUMN outcome VARCHAR(255);')

#conn.executescript("UPDATE Match SET outcome = CASE WHEN home_team_goal > away_team_goal THEN 'home' WHEN home_team_goal < away_team_goal THEN 'away' ELSE 'draw' END");
