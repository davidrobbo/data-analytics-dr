import sqlite3
import pandas as pd

def get_df(sql):
    conn = sqlite3.connect('./database.sqlite')
    cur = conn.cursor()
    #cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    cur.execute(sql)
    rows = cur.fetchall()
    blank = []
    for t in cur.description:
        blank.append(t[0])
    data = []
    for row in rows:
        obj = {}
        for i in range(0, len(row)):
            obj[blank[i]] = row[i]
        data.append(obj)
    return pd.DataFrame(data)

def get_clean_df(limit = 2500):
    conn = sqlite3.connect('./database.sqlite')
    cur = conn.cursor()
    sql = "SELECT * FROM Match WHERE home_last_x = 5 AND away_last_x = 5 LIMIT %i" % limit
    cur.execute(sql)
    rows = cur.fetchall()
    blank = []
    for t in cur.description:
        blank.append(t[0])
    data = []
    for row in rows:
        obj = {}
        for i in range(0, len(row)):
            obj[blank[i]] = row[i]
        data.append(obj)
    df = pd.DataFrame(data)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    excludes = ['PSA', 'PSD', 'PSH', 'home_team_goal', 'away_team_goal', 'id', 'home_team_api_id', 'away_team_api_id',
                'match_api_id', 'league_id', 'country_id', 'home_points', 'away_points']
    df['home_away_last_five_dif'] = df['home_last_five'] - df['away_last_five']
    df['home_away_season_dif'] = df['home_season_points'] - df['away_season_points']
    df['home_form_away_form_dif'] = df['home_home_form_last_5'] - df['away_away_form_last_5']
    df.drop(columns=excludes, inplace=True)
    df.dropna(how='all', axis=1, inplace=True)
    df = df[df.columns.drop(list(df.filter(regex="player")))]
    df.fillna(df.mean(), inplace=True)
    return df.select_dtypes(include=numerics), df['outcome']
