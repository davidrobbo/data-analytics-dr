from Util import get_clean_df
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
import pydotplus
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier

df, y = get_clean_df(limit=20000)

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=0)
X_test_odds = X_test['best_win_odds']
X_train.drop(columns=['best_win_odds'], inplace=True)
X_test.drop(columns=['best_win_odds'], inplace=True)
print(X_train.columns)
models = {
    "bayes": GaussianNB(),
    "svm": svm.SVC(),
    "knn": KNeighborsClassifier(),
    "decision_tree": DecisionTreeClassifier(),
    "sgd": SGDClassifier(),
    "rf": RandomForestClassifier()
}
print(X_test.describe().to_string())
for key in models:
    model = models[key]
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    y_vals = y_test.tolist()
    odds_list = X_test_odds.tolist()
    count = 0
    odds = 0
    for i in range(0, len(preds)):
        if preds[i] == y_vals[i]:
            count += 1
            odds += odds_list[i]
    print('model=', key, 'count2000=', count, '1unitreturn=', odds, 'score=', model.score(X_train, y_train))
    '''
    if key == 'decision_tree':
        dot_data = StringIO()
        export_graphviz(model, out_file=dot_data,
                        filled=True, rounded=True,
                        special_characters=True, feature_names=X_test.columns)
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
        graph.write_png('./output/test.png')
    '''

