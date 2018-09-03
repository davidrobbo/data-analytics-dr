import sqlite3

conn = sqlite3.connect('./database.sqlite')
cur = conn.cursor()
def update(match_id, home, away, home_x, away_x):
    conn = sqlite3.connect('./database.sqlite')
    cur = conn.cursor()
    sql = "UPDATE Match set home_last_five=%i,away_last_five=%i,home_last_x=%i,away_last_x=%i where id=%i"
    sql = sql % (home, away, home_x, away_x, match_id)
    #print(sql)
    cur.executescript(sql)

def update_a(match_id, home, away):
    conn = sqlite3.connect('./database.sqlite')
    cur = conn.cursor()
    sql = "UPDATE Match set home_season_points=%s, away_season_points=%s where id=%i"
    sql = sql % (home, away, match_id)
    # print(sql)
    cur.executescript(sql)
'''
c = """
    UPDATE Match SET home_points = 
        case when home_team_goal > away_team_goal then 3
        when away_team_goal > home_team_goal then 0
        else 1
        end,
        away_points = 
        case when home_team_goal < away_team_goal then 3
        when away_team_goal < home_team_goal then 0
        else 1
        end;
"""


c = """
    SELECT id, home_team_api_id, away_team_api_id, home_points, away_points FROM Match order by id desc;
"""
cur.execute(c)
rows = cur.fetchall()
for row in rows:
    s = "SELECT case when home_team_api_id=%s then home_points else away_points end as points, home_last_five, home_last_x, home_team_api_id from Match WHERE (home_team_api_id=%s OR away_team_api_id=%s) and id < %s order by id desc limit 5"
    sql_home = s % (row[1], row[1], row[1], row[0])
    sql_away = s % (row[2], row[2], row[2], row[0])
    cur.execute(sql_home)
    home_5 = cur.fetchall()
    cur.execute(sql_away)
    away_5 = cur.fetchall()
    count_home = 0
    count_away = 0
    for t in home_5:
        count_home += t[0]
    for t in away_5:
        count_away += t[0]
    update(row[0], count_home, count_away, len(home_5), len(away_5))

'''
'''
sql = "SELECT case when home_team_api_id=10192 then home_points else away_points end as points, case when home_team_api_id=10192 then home_last_five else away_last_five end as last FROM Match where (home_team_api_id=10192 OR away_team_api_id=10192) order by id desc limit 100"
cur.execute(sql)
print(cur.fetchall())
'''
c = """
    SELECT id, season, home_team_api_id, away_team_api_id, home_points, away_points FROM Match order by id desc;
"""
cur.execute(c)
all = cur.fetchall()
for row in all:
    s = "SELECT case when home_team_api_id=%s then home_points else away_points end as points FROM Match where (home_team_api_id=%s OR away_team_api_id=%s) AND season='%s' AND id < %s;"
    ss = s % (row[2], row[2], row[2], row[1], row[0])
    cur.execute(ss)
    all_s = cur.fetchall()
    count = 0
    for t in all_s:
        count += t[0]
    ssa = s % (row[3], row[3], row[3], row[1], row[0])
    cur.execute(ssa)
    all_sa = cur.fetchall()
    counta = 0
    for t in all_sa:
        counta += t[0]
    update_a(row[0], count, counta)
