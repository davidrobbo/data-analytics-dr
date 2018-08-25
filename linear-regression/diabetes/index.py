import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
from pandas.plotting import scatter_matrix
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data = datasets.load_diabetes()
#print(data.keys())
#print(data.feature_names)

X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=0)
model = LinearRegression()
model.fit(X_train, y_train)
#print(model.predict(X_test))
#print(y_test)

df = pd.DataFrame(data=data.data, columns=data.feature_names)
'''
scatter_matrix(df)
plt.savefig('../output/diabetes-scatter.png')
plt.close()

plt.scatter(X_train[:, 2], y_train, color='black')
plt.title('Training Diabetes Data')
plt.xlabel('BMI')
plt.ylabel('Progression')
plt.savefig('../output/diabetes-scatter-bmi.png')
plt.close()
'''
'''
for i in range(0, 9):
    slope, intercept, r_value, p_value, std_err = stats.linregress(X_train[:, i], y_train)
    print(p_value)
    line = slope * X_train[:, i] + intercept
    print(line)
    plt.plot(X_train[:, i], y_train, 'o', X_train[:, i], line)
    plt.title('Training Diabetes Data - R (R2) = %f (%f)' % (r_value, r_value*r_value))
    plt.xlabel(data.feature_names[i])
    plt.ylabel('Progression')
    plt.savefig('../output/diabetes-%s.png' % data.feature_names[i])
    plt.close()
'''
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)
#r2 below
print(regressor.score(X_train, y_train))
#print(str(data.data[0]))
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

