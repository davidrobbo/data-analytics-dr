import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

conn = sqlite3.connect('./database.sqlite')

cur = conn.cursor()
#cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
cur.execute("SELECT * FROM Match WHERE home_last_x = 5 AND away_last_x = 5 LIMIT 5000")

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
df.reset_index(drop=True, inplace=True)
#print(df.head())
df['total_goals'] = df['home_team_goal'] + df['away_team_goal']
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
newdf = df.select_dtypes(include=numerics)
newdf['home_away_last_five_dif'] = newdf['home_last_five'] - newdf['away_last_five']
newdf['home_away_season_dif'] = newdf['home_season_points'] - newdf['away_season_points']
model = LinearRegression()
newdf = newdf[newdf.B365A.notnull()]
newdf = newdf[newdf.B365H.notnull()]
newdf = newdf[newdf.B365D.notnull()]
y = newdf['total_goals']
newdf.drop(columns=['away_team_goal', 'home_team_goal', 'total_goals', 'match_api_id', 'home_team_api_id', 'away_team_api_id', 'BSA', 'BSD', 'BSH'], inplace=True)

#newdf.dropna(how='all', inplace=True)
#print(newdf.describe().to_string())
#print(newdf.isnull().sum())
y.reset_index(drop=True, inplace=True)
X = newdf[['B365A', 'B365H', 'B365D', 'home_away_last_five_dif', 'home_away_season_dif']]
print(X.isnull().sum())

X_train, X_test, y_train, y_test = train_test_split(newdf[['B365A', 'B365H', 'B365D', 'home_away_last_five_dif', 'home_away_season_dif']], y, test_size=0.2, random_state=0)

model.fit(X_train, y_train)
print(model.score(X_train, y_train))
#print(model.coef_)
#print(model.intercept_)
predictions = model.predict(X_test)
data = []

y_test = tuple(y_test)
count = 0
for i in range(0, len(predictions)):
    if y_test[i] >= round(predictions[i], 0):
        count += 1

print(count)
