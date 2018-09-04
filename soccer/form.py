import sqlite3
#a = "ALTER TABLE Match ADD COLUMN home_home_form_last_x int(11)"
#b = "ALTER TABLE Match ADD COLUMN home_home_form_last_x int(11)"
sql = "SELECT id, home_team_api_id, away_team_api_id, home_points, home_home_form_last_x, home_home_form_last_5, away_away_form_last_x, away_away_form_last_5 FROM Match order by id desc"

conn = sqlite3.connect('./database.sqlite')
cur = conn.cursor()
cur.execute(sql)

rows = cur.fetchall()
def or_zero(a):
    if a is None:
        return 0
    return a

for row in rows:
    a = "SELECT sum(home_points), count(home_points) FROM (SELECT home_points FROM Match WHERE home_team_api_id=%i AND id < %i ORDER BY id desc LIMIT 5)"
    b = "SELECT sum(away_points), count(away_points) as points FROM (SELECT away_points FROM Match WHERE away_team_api_id=%i AND id < %i ORDER BY id desc LIMIT 5)"
    cur.execute(a % (row[1], row[0]))
    h = cur.fetchall()[0]
    cur.execute(b % (row[2], row[0]))
    a = cur.fetchall()[0]
    sql = "UPDATE Match SET home_home_form_last_5=%i, home_home_form_last_x=%i, away_away_form_last_5=%i, away_away_form_last_x=%i WHERE id=%i"
    cur.executescript(sql % (or_zero(h[0]), or_zero(h[1]), or_zero(a[0]), or_zero(a[1]), or_zero(row[0])))
    if row[0] % 1000 == 0:
        print(row[0])


