import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer

DATA_DIR = '../data/housing/'
OUTPUT_DIR = '../output/housing/'

df = pd.read_csv(DATA_DIR + 'index.csv')
print(df.head().to_string())
# df.reset_index(inplace=True)
df['id'] = df.index + 1
print(df.head().to_string())
df.set_index('id')

train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
print(train_data.head())
train_data.plot(kind="scatter", x="longitude", y="latitude", alpha="0.1",
                c="median_house_value", cmap=plt.get_cmap('jet'))
#plt.show()
#plt.close()
print(train_data.corr().to_string())
#scatter_matrix(train_data)
#plt.show()
x = train_data.drop("median_house_value", axis=1)
y = train_data["median_house_value"]
print(x.head())
print(y.head())

bedrooms_median = x.total_bedrooms.median()
train_data["total_bedrooms"].fillna(bedrooms_median, inplace=True)
test_data["total_bedrooms"].fillna(bedrooms_median, inplace=True)
'''
label_encode = LabelEncoder()
ocean_prox_label = label_encode.fit_transform(train_data.ocean_proximity)

one_hot = OneHotEncoder()
one_hot_label = one_hot.fit_transform(ocean_prox_label.reshape(len(ocean_prox_label), 1))
print(one_hot_label.toarray())

label_bin = LabelBinarizer()
labels_ocean_prox = label_bin.fit_transform(train_data.ocean_proximity)
print(train_data.ocean_proximity.value_counts())
print(train_data.ocean_proximity.head())
print(labels_ocean_prox)

print(label_bin.inverse_transform(labels_ocean_prox))
'''
train_data = pd.get_dummies(train_data, columns=['ocean_proximity'])
print(train_data.head().to_string())

'''
print(df.describe().to_string())
print(df.head().to_string())
print(df.isnull().sum().to_string())
print(df.ocean_proximity.value_counts())


df.hist(bins=50)
plt.tight_layout()
plt.savefig(OUTPUT_DIR + 'housing-hist.png')
plt.close()
'''
