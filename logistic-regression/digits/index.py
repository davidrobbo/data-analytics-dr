from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import matplotlib.pyplot as plt

dataset = load_digits()
x_train, x_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.20, random_state=0)

regressor = LogisticRegression()
regressor.fit(x_train, y_train)
#print(regressor.score(x_train, y_train))
predictions = regressor.predict(x_test)
count = 0
for i in range(0, len(predictions)):
    count = count+1 if predictions[i] == y_test[i] else count
print(count)
print(len(predictions))
cm = metrics.confusion_matrix(y_test, predictions)
plt.figure(figsize=(9,9))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
all_sample_title = 'Accuracy Score: {0}'.format(regressor.score(x_test, y_test))
plt.title(all_sample_title, size=15)
plt.show()
