import sqlite3

sql = "SELECT case when home_team_api_id=10000 then home_points else away_points end as points, case when home_team_api_id=10000 then home_season_points else away_season_points end as pointss FROM Match where (home_team_api_id=10000 OR away_team_api_id=10000) AND season='2015/2016' order by id desc"

con = sqlite3.connect('./database.sqlite')
cur = con.cursor()
cur.execute(sql)
print(cur.fetchall())
