from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
import pydotplus
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

df = pd.read_csv('./data/data.csv')
print(df.shape)
print(df.head().to_string())
print(df.describe().to_string())
scatter_matrix(df)
plt.savefig('./output/scatter.png')
y = df['status']
print(y.value_counts())
df.drop(columns=['name', 'status'], inplace=True)
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=0)

models = {
    "bayes": GaussianNB(),
    "svm": svm.SVC(),
    "knn": KNeighborsClassifier(),
    "decision_tree": DecisionTreeClassifier(),
    "sgd": SGDClassifier(),
    "rf": RandomForestClassifier(),
    "log_reg": LogisticRegression()
}
for key in models:
    model = models[key]
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    y_vals = y_test.tolist()
    count = 0
    for i in range(0, len(preds)):
        if preds[i] == y_vals[i]:
            count += 1
    print('model=', key, 'score=', model.score(X_train, y_train), float(count) / len(preds))
    if key == 'decision_tree':
        dot_data = StringIO()
        export_graphviz(model, out_file=dot_data,
                        filled=True, rounded=True,
                        special_characters=True, feature_names=X_test.columns)
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
        graph.write_png('./output/parkinsons-decision.png')
