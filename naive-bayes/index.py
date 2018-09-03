import sklearn.datasets as datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

x_tr, x_test, y_tr, y_test = train_test_split(df, iris.target)

bayes = GaussianNB()
bayes.fit(x_tr, y_tr)
print(bayes.score(x_tr, y_tr))
predictions = bayes.predict(x_test)
count = 0
for i in range(0, len(predictions)):
    if predictions[i] == y_test[i]:
        count += 1

print(float(count)/len(predictions))
