import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

DATA_DIR = '../data/iris/'
OUTPUT_DIR = '../output/iris/'
df = pd.read_csv(DATA_DIR + 'Iris.csv')

print(df.shape)
# to_string enables more columns to fit into output
print(df.head().to_string())
print(df.describe().to_string())
columns = {
    "SepalLengthCm": "sepal_length",
    "SepalWidthCm": "sepal_width",
    "PetalLengthCm": "petal_length",
    "PetalWidthCm": "petal_width",
    "Species": "species"
}
df.rename(columns=columns, inplace=True)
df.drop(columns=["Id"], inplace=True)

print(df.groupby("species").size())

df.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.savefig(OUTPUT_DIR + "box.png")
plt.close()

df.hist()
plt.savefig(OUTPUT_DIR + "hist.png")
plt.close()

scatter_matrix(df)
plt.savefig(OUTPUT_DIR + "scatter.png")
plt.close()

array = df.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Spot Check Algorithms
models = [('LR', LogisticRegression()), ('LDA', LinearDiscriminantAnalysis()), ('KNN', KNeighborsClassifier()),
          ('CART', DecisionTreeClassifier()), ('NB', GaussianNB()), ('SVM', SVC())]
# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

# Make predictions on validation dataset
for name, model in models:
    mdl = model
    mdl.fit(X_train, Y_train)
    predictions = mdl.predict(X_validation)
    print(name)
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation, predictions))
    print(classification_report(Y_validation, predictions))
