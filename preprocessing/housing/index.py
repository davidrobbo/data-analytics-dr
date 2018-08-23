import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix

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
print(bedrooms_median)
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
