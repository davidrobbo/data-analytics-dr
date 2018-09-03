import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from Util import get_df

df = get_df("SELECT * FROM Match WHERE home_last_x = 5 AND away_last_x = 5 LIMIT 5000")
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
excludes = ['PSA', 'PSD', 'PSH', 'home_team_goal', 'away_team_goal', 'id', 'home_team_api_id', 'away_team_api_id', 'match_api_id', 'league_id', 'country_id']
df['home_away_last_five_dif'] = df['home_last_five'] - df['away_last_five']
df['home_away_season_dif'] = df['home_season_points'] - df['away_season_points']

df.drop(columns=excludes, inplace=True)
df.dropna(how='all', axis=1, inplace=True)
df = df[df.columns.drop(list(df.filter(regex="player")))]
df.fillna(df.mean(), inplace=True)
print(df.isnull().sum())
X = df.select_dtypes(include=numerics)
for col in X.columns:
    print col
y = df['outcome']
X_train, X_test, y_train, y_test = train_test_split(X[['B365A', 'B365H', 'B365D', 'home_last_five', 'away_last_five', 'home_away_season_dif', 'best_win_odds']], y, test_size=0.20, random_state=0)
bayes = GaussianNB()
bayes.fit(X_train[['B365A', 'B365H', 'B365D', 'home_last_five', 'away_last_five', 'home_away_season_dif']], y_train)
print(bayes.score(X_train[['B365A', 'B365H', 'B365D', 'home_last_five', 'away_last_five', 'home_away_season_dif']], y_train))

prediction = bayes.predict(X_test[['B365A', 'B365H', 'B365D', 'home_last_five', 'away_last_five', 'home_away_season_dif']])

y = tuple(y_test)
count = 0
for i in range(0, len(prediction)):
    if prediction[i] == y[i]:
        count += 1

count = 0
best_possible = 0
fav_only = 0
x_te = X_test.reset_index()

for i in range(0, len(y)):
    home = x_te.iloc[i].B365H
    away = x_te.iloc[i].B365A
    draw = x_te.iloc[i].B365D
    best_wind_odds = x_te.iloc[i].best_win_odds
    if y[i] == 'home':
        best_possible += best_wind_odds
        if (home < away) and (home < draw):
            fav_only += best_wind_odds
    elif y[i] == 'away':
        best_possible += best_wind_odds
        if (away < home) and (away < draw):
            fav_only += best_wind_odds
    else:
        best_possible += best_wind_odds
        if (draw < home) and (draw < away):
            fav_only += best_wind_odds

    if y[i] == prediction[i]:
        if prediction[i] == 'home':
            count += best_wind_odds
        elif prediction[i] == 'away':
            count += best_wind_odds
        else:
            count += best_wind_odds

print(count)
print(best_possible)
print(fav_only)

