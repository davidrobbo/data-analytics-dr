import pandas as pd
import sqlite3

conn = sqlite3.connect('./database.sqlite')
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
'''
rows = cur.fetchall()
print(rows)
player_desc = "SELECT * FROM Player"
cur.execute(player_desc)
players = cur.fetchall()
for p in players:
    print(p)
print(cur.description)
'''
player_attr_desc = "SELECT * FROM Player_attributes"
max = "SELECT count(*) as count FROM Player_attributes GROUP BY player_api_id ORDER BY count desc"
cur.execute(player_attr_desc)
for t in cur.description:
    print(t[0])
cur.execute(max)
print(cur.fetchall())
