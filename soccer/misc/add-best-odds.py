import sqlite3
from Util import get_df

def update_best_odds(id, odds):
    conn = sqlite3.connect('./database.sqlite')
    cur = conn.cursor()
    sql = "UPDATE Match SET best_win_odds=%f WHERE id = %i" % (odds, id)
    cur.executescript(sql)
    if id % 1000 == 0:
        print(id)

#sql = "ALTER TABLE Match ADD COLUMN best_win_odds decimal(19,2)"

df = get_df("SELECT * FROM Match")
bookies = ['B365', 'BW', 'IW', 'LB', 'PS', 'WH', 'SJ', 'VC', 'GB', 'BS']
dicti = {
    "home": "H",
    "away": "A",
    "draw": "D"
}
for idx, row in df.iterrows():
    #print(row.best_win_odds)
    val = 0
    outcome = row.outcome
    #print(outcome)
    suffix = dicti[outcome]
    for bookie in bookies:
        bookie_prop = bookie + suffix
        #print(row[bookie_prop])
        if row[bookie_prop] > val:
            val = row[bookie_prop]

    update_best_odds(row.id, val)

