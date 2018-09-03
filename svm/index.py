import sklearn.datasets as datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

svm = svm.SVC(kernel='linear')

x_tr, x_test, y_tr, y_test = train_test_split(df, iris.target, test_size=0.2, random_state=0)
svm.fit(x_tr, y_tr)
print(svm.score(x_tr, y_tr))
scores = cross_val_score(svm, iris.data, iris.target, cv=5)
print(scores)

prediction = svm.predict(x_test)

count = 0
for i in range(0, len(prediction)):
    if prediction[i] == y_test[i]:
        count += 1

print(float(count) / len(prediction))
