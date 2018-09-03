from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

from Util import get_df

df = get_df("SELECT * FROM Match WHERE home_last_x = 5 AND away_last_x = 5 LIMIT 5000")
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
excludes = ['PSA', 'PSD', 'PSH', 'home_team_goal', 'away_team_goal', 'id', 'home_team_api_id', 'away_team_api_id', 'match_api_id', 'league_id', 'country_id']
df['home_away_last_five_dif'] = df['home_last_five'] - df['away_last_five']
df['home_away_season_dif'] = df['home_season_points'] - df['away_season_points']

for col in df.columns:
    print(col)
df.drop(columns=excludes, inplace=True)
df.dropna(how='all', axis=1, inplace=True)
df = df[df.columns.drop(list(df.filter(regex="player")))]
df.fillna(df.mean(), inplace=True)
print(df.isnull().sum())
X = df.select_dtypes(include=numerics)
for col in X.columns:
    print col
y = df['outcome']
X_train, X_test, y_train, y_test = train_test_split(X[['B365A', 'B365H', 'B365D', 'home_last_five', 'away_last_five', 'home_away_season_dif']], y, test_size=0.20, random_state=0)
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
#print(y_pred)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

#print(y_test)
y = tuple(y_test)

count = 0
best_possible = 0
fav_only = 0
x_te = X_test.reset_index()

for i in range(0, len(y)):
    home = x_te.iloc[i].B365H
    away = x_te.iloc[i].B365A
    draw = x_te.iloc[i].B365D
    if y[i] == 'home':
        best_possible += home
        if (home < away) and (home < draw):
            fav_only += home
    elif y[i] == 'away':
        best_possible += away
        if (away < home) and (away < draw):
            fav_only += away
    else:
        best_possible += draw
        if (draw < home) and (draw < away):
            fav_only += draw

    if y[i] == y_pred[i]:
        if y_pred[i] == 'home':
            count += home
        elif y_pred[i] == 'away':
            count += away
        else:
            count += draw

print(count)
print(best_possible)
print(fav_only)
