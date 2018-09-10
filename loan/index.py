import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('./data/data.csv')

print(df.head().to_string())
education_dummies = pd.get_dummies(df['education'])
joined = pd.concat([df, education_dummies], axis=1)
joined.past_due_days.fillna(value=0)
is_paid_off = []
for index, row in df.iterrows():
    status = row.loan_status
    is_paid_off.append(1 if status == "PAIDOFF" else 0)
joined['Gender'].replace(['female', 'male'], [0, 1], inplace=True)
joined['paid_off'] = is_paid_off
#print(joined.isnull().sum())
print(joined.head().to_string())
#print(joined.describe().to_string())
x_ex = ['Loan_ID', 'loan_status', 'Principal', 'effective_date', 'due_date', 'paid_off_time', 'past_due_days', 'education', 'paid_off']
y = joined['paid_off']
joined.drop(columns=x_ex, inplace=True)
X_train, X_test, y_train, y_test = train_test_split(joined, y, test_size=0.2, random_state=0)

models = {
    "bayes": GaussianNB(),
    "svm": svm.SVC(),
    "knn": KNeighborsClassifier(),
    "decision_tree": DecisionTreeClassifier(),
    "sgd": SGDClassifier(),
    "rf": RandomForestClassifier()
}
print(X_train.head().to_string())
for key in models:
    model = models[key]
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    y_vals = y_test.tolist()
    count = 0
    for i in range(0, len(y_vals)):
        if preds[i] == y_vals[i]:
            count += 1
    print(key, count)