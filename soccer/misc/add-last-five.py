import sqlite3

conn = sqlite3.connect('./database.sqlite')
cur = conn.cursor()

'''
add_column_home = "ALTER TABLE Match ADD COLUMN home_last_five INT(11)"
add_column_away = "ALTER TABLE Match ADD COLUMN away_last_five INT(11)"
conn.executescript(add_column_away)
conn.executescript(add_column_home)
'''
def get_points_last_five_for_team_api_id_less_than_match_id(api_id, match_id):
    get_last_five = "SELECT id, home_team_goal, away_team_goal, home_team_api_id, away_team_api_id FROM Match WHERE (home_team_api_id = %s OR away_team_api_id = %s) AND id < %s ORDER BY date desc LIMIT 5" % (
    api_id, api_id, match_id)
    cur.execute(get_last_five)
    rows_last_five_home = cur.fetchall()
    count = 0
    for row_last_five in rows_last_five_home:
        team_index = 1 if row_last_five[3] == api_id else 2
        opposing_index = 1 if team_index == 2 else 1
        team_goals = row_last_five[team_index]
        opposing_goals = row_last_five[opposing_index]
        if team_goals > opposing_goals:
            count += 3
        elif opposing_goals == team_goals:
            count += 1
    return count

def update_last_five_for_match(match_id, home_points, away_points):
    sql = "UPDATE Match SET home_last_five=%s, away_last_five=%s WHERE id=%s" % (home_points, away_points, match_id)
    cur.executescript(sql)

all = "SELECT id, home_team_api_id, away_team_api_id, home_last_five, away_last_five FROM Match ORDER BY id desc"
#cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
cur.execute(all)
rows = cur.fetchall()
for row in rows:
    print(row)
    id = row[0]
    home = row[1]
    away = row[2]
    points_home = get_points_last_five_for_team_api_id_less_than_match_id(home, id)
    points_away = get_points_last_five_for_team_api_id_less_than_match_id(away, id)
    print(points_home)
    update_last_five_for_match(id, points_home, points_away)
