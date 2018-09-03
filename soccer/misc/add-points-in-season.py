import sqlite3

conn = sqlite3.connect('./database.sqlite')
cur = conn.cursor()

def get_season_points(season, match_id, team_api_id):
    season_matches = "SELECT id, home_team_goal, away_team_goal, home_team_api_id, away_team_api_id FROM Match WHERE (home_team_api_id = %s OR away_team_api_id = %s) AND season = '%s' AND id < %s ORDER BY id desc" % (team_api_id, team_api_id, season, match_id)
    #print(season_matches)
    cur.execute(season_matches)
    matches = cur.fetchall()
    #print(matches)
    count = 0
    for match in matches:
        team_index = 1 if match[3] == id else 2
        opposing_index = 1 if team_index == 2 else 1
        team_goals = match[team_index]
        opposing_goals = match[opposing_index]
        if team_goals > opposing_goals:
            count += 3
        elif opposing_goals == team_goals:
            count += 1
    return count

def update_season_points(match_id, home_team, away_team):
    update = "UPDATE Match SET home_points=%s, away_points=%s WHERE id=%s" % (home_team, away_team, match_id)
    cur.executescript(update)

'''
alter_home_points = "ALTER TABLE Match ADD COLUMN home_points INT(11)"
alter_away_points = "ALTER TABLE Match ADD COLUMN away_points INT(11)"
'''
all = "SELECT id, home_team_goal, away_team_goal, season, home_team_api_id, away_team_api_id, home_points FROM Match ORDER BY id desc"
cur.execute(all)
rows = cur.fetchall()
for row in rows:
    id = row[0]
    home_points = get_season_points(row[3], id, row[4])
    away_points = get_season_points(row[3], id, row[5])
    print(home_points)
    update_season_points(id, home_points, away_points)
