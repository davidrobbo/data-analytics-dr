from sklearn import datasets
import matplotlib
import matplotlib.pyplot as plt
import random
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, roc_curve, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

# Part 1 - Binary classifiers

OUTPUT_DIR = '../output/'
dataset = datasets.fetch_mldata('MNIST original')
X, y = dataset.data, dataset.target
#print(X.shape, y.shape)

random_number = random.randint(0, len(X) - 1)
#print(X[random_number])
#print(y[random_number])
digit = X[random_number]
reshape = digit.reshape(28, 28)
#print(reshape)

plt.imshow(reshape, cmap=matplotlib.cm.binary, interpolation="nearest")
plt.savefig(OUTPUT_DIR + 'mnist-rand.png')
plt.close()

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

'''
    Below classifies 'is y = i (0-9)' as opposed to 'what is y (0-9)'
'''
sgd_0 = SGDClassifier()
is_0 = y_train == 0

sgd_0.fit(x_train, is_0)

is_0_test = y_test == 0
predictions = sgd_0.predict(x_test)
count = 0
count_default_0 = 0
for i in range(0, len(predictions)):
    if predictions[i] == is_0_test[i]:
        count += 1
    if is_0_test[i]:
        count_default_0 += 1

#print(count)
#print(count_default_0)
#print(len(predictions))
per = float(count) / len(predictions)
#print(per)
per_default = float(count_default_0) / len(predictions)
#print(1 - per_default)

cross_val = cross_val_score(sgd_0, x_train, is_0, cv=10, scoring="accuracy")
#print(cross_val)
''''''
cross_val_pred_0 = cross_val_predict(sgd_0, x_train, is_0, cv=3)
confusion_matrix_0 = confusion_matrix(is_0, cross_val_pred_0)
recall_0 = recall_score(is_0, cross_val_pred_0)
precision_o = precision_score(is_0, cross_val_pred_0)
f1_0 = f1_score(is_0, cross_val_pred_0)
#print(predictions)
#print(y_test)
#print(cross_val_pred_0)
#print(recall_0)
#print(precision_o)
#print(f1_0)
'''
CONFUSIONMATRIX
            Predict
            -   +
Acutal  -   TN  FP
        +   FN  TP
        
Precision = TP / (TP+FP)
Measures amount of true positives found divided by all total positive predictions
Recall = TP / (TP/+FN)
Measures amount of true positives found divided by all actual positive
F1 - representation of both above
2 / (1 / precision) + (1 / recall) 
    OR
2 * ((precision * recall) / (precision + recall))
'''
#print(confusion_matrix_0)

'''
ROC - Receiver Operating Characteristic
y = TruePositiveRate = recall (see above)
x = FalsePositiveRate = specificity = 1 - TrueNegativeRate (TN / (FP + TN))
'''
fpr, tpr, thresholds = roc_curve(is_0, cross_val_pred_0)

plt.plot(fpr, tpr, linewidth=2)
plt.plot([0, 1], [0, 1], 'k--')
plt.axis([0, 1, 0, 1])
plt.savefig(OUTPUT_DIR + 'mnist-roc.png')
plt.close()

roc_score = roc_auc_score(is_0, cross_val_pred_0)
#print(roc_score)

forest = RandomForestClassifier(random_state=42)
y_probs_forest_0 = cross_val_predict(forest, x_train, is_0, cv=3, method="predict_proba")
#print(y_probs_forest_0)
y_scores_forest_0 = y_probs_forest_0[:, 1]
fpr_forest_0, tpr_forest_0, forest_thresholds = roc_curve(is_0, y_scores_forest_0)
plt.plot(fpr_forest_0, tpr_forest_0, linewidth=2)
plt.plot([0, 1], [0, 1], 'k--')
plt.axis([0, 1, 0, 1])
plt.savefig(OUTPUT_DIR + 'mnist-roc-random-forest.png')
plt.close()
roc_random_forest_score = roc_auc_score(is_0, y_scores_forest_0)
#print(roc_random_forest_score)

# Part 2 - Multiclass classifiers
sgd_all = SGDClassifier()
sgd_all.fit(x_train, y_train)
sgd_all_pred = sgd_all.predict(x_test)

cross_val_all = cross_val_score(sgd_all, x_train, y_train, cv=10, scoring="accuracy")
cross_val_pred_all = cross_val_predict(sgd_all, x_train, y_train, cv=3)
confusion_matrix_all = confusion_matrix(y_train, cross_val_pred_all)
recall_all = recall_score(y_train, cross_val_pred_all, average="weighted")
precision_all = precision_score(y_train, cross_val_pred_all, average="weighted")
f1_all = f1_score(y_train, cross_val_pred_all, average="weighted")
print(recall_all)
print(precision_all)
print(f1_all)
