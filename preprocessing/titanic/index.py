# Step 1 - Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
# IPython only (uncomment below)
# %matplotlib inline
DATA_DIR = '../data/titanic/'
OUTPUT_DIR = '../output/titanic/'

# Step 2 - Get data
training_set = pd.read_csv(DATA_DIR + 'train.csv')
test_set = pd.read_csv(DATA_DIR + 'test.csv')

# Step 3 - Handle missing data
print(training_set.isnull().sum())
print(test_set.isnull().sum())

# make a list of all the posible Decks, the last element is used when no cabin code is present
cabin_list = ['A', 'B', 'C', 'D', 'E', 'F', 'T', 'G', 'Unknown']
# define a function that replaces the cabin code with the deck character


def search_substring(big_string, substring_list):
    for substring in substring_list:
        if substring in big_string:
            return substring
    return substring_list[-1]

# replace passenger's name with his/her title (Mr, Mrs, Miss, Master)


def get_title(string):
    import re
    regex = re.compile(r'Mr|Don|Major|Capt|Jonkheer|Rev|Col|Dr|Mrs|Countess|Dona|Mme|Ms|Miss|Mlle|Master',
                       re.IGNORECASE)
    results = regex.search(string)
    if results is not None:
        return results.group().lower()
    else:
        return str(np.nan)

# dictionary to map to generate the new feature vector
title_dictionary = {
    "capt": "Officer",
    "col": "Officer",
    "major": "Officer",
    "dr": "Officer",
    "jonkheer": "Royalty",
    "rev": "Officer",
    "countess": "Royalty",
    "dona": "Royalty",
    "lady": "Royalty",
    "don": "Royalty",
    "mr": "Mr",
    "mme": "Mrs",
    "ms": "Mrs",
    "mrs": "Mrs",
    "miss": "Miss",
    "mlle": "Miss",
    "master": "Master",
    "nan": "Mr"
}
training_set['Deck'] = training_set['Cabin'].map(lambda x: search_substring(str(x), cabin_list))
test_set['Deck'] = test_set['Cabin'].map(lambda x: search_substring(str(x), cabin_list))
# delete the Cabin feature
training_set.drop('Cabin', 1, inplace=True)
test_set.drop('Cabin', 1, inplace=True)
training_set['Title'] = training_set['Name'].apply(get_title)
test_set['Title'] = test_set['Name'].apply(get_title)
training_set['Title'] = training_set['Title'].map(title_dictionary)
test_set['Title'] = test_set['Title'].map(title_dictionary)
# delete the Name feature
training_set.drop('Name', 1, inplace=True)
test_set.drop('Name', 1, inplace=True)

#dropping ticket column
training_set.drop('Ticket', 1, inplace=True)
test_set.drop('Ticket', 1, inplace=True)

means_title = training_set.groupby('Title')['Age'].mean()
title_list = ['Mr', 'Miss', 'Mrs', 'Master', 'Royalty', 'Officer']


def age_nan_replace(means, dframe, title_list):
    for title in title_list:
        temp = dframe['Title'] == title  # extract indices of samples with same title
        dframe.loc[temp, 'Age'] = dframe.loc[temp, 'Age'].fillna(means[title])  # replace nan values for mean


age_nan_replace(means_title, training_set, title_list)
age_nan_replace(means_title, test_set, title_list)
training_set['Embarked'].fillna('S', inplace=True)
test_set['Embarked'].fillna('S', inplace=True)
# fill the fare column in the test set
test_set['Fare'].fillna(test_set['Fare'].mean(), inplace=True)
training_set.groupby('Embarked').size().plot(kind='bar')
plt.savefig(OUTPUT_DIR + 'titanic.png')
plt.close()

index = training_set['Survived'].unique() # get the number of bars
grouped_data = training_set.groupby(['Survived', 'Sex'])
temp = grouped_data.size().unstack()
women_stats = (temp.iat[0,0], temp.iat[1,0])
men_stats = (temp.iat[0,1], temp.iat[1,1])
p1 = plt.bar(index, women_stats)
p2 = plt.bar(index, men_stats, bottom=women_stats)
plt.xticks(index, ('No', 'Yes'))
plt.ylabel('Number of People')
plt.xlabel('Survival')
plt.title('Survival of passengers')
plt.legend((p1[0], p2[0]), ('Women', 'Men'))
plt.tight_layout()

plt.savefig(OUTPUT_DIR + 'titanic-men-v-wmn.png')
plt.close()

training_set.pivot_table('Survived',index='Sex',columns='Pclass').plot(kind='bar')
plt.savefig(OUTPUT_DIR + 'titanic-class.png', bbox_inches='tight')
plt.close()

training_set.pivot_table('Survived', index='Title', columns='Pclass').plot(kind='bar')
plt.savefig(OUTPUT_DIR + 'titanic-title.png', bbox_inches='tight')
plt.close()

age_intervals = pd.qcut(training_set['Age'], 3)
training_set.pivot_table('Survived', ['Sex', age_intervals], 'Pclass').plot(kind='bar')
plt.savefig(OUTPUT_DIR + 'titanic-age-sex.png', bbox_inches='tight')
plt.close()

training_set['Family Size'] = training_set['Parch'] + training_set['SibSp']
test_set['Family Size'] = test_set['Parch'] + test_set['SibSp']
training_set.drop('Parch', axis=1, inplace=True)
training_set.drop('SibSp', axis=1, inplace=True)
test_set.drop('Parch', axis=1, inplace=True)
test_set.drop('SibSp', axis=1, inplace=True)

# Step x - Feature scale, handle categorical fields
numericals_list = ['Age', 'Fare']
for column in numericals_list:
    sc = StandardScaler(with_mean=True, with_std=True)
    sc.fit(training_set[column].values.reshape(-1, 1))
    training_set[column] = sc.transform(training_set[column].values.reshape(-1, 1))
    test_set[column] = sc.transform(test_set[column].values.reshape(-1, 1))

categorical_classes_list = ['Sex', 'Embarked', 'Deck', 'Title']
# Pclass is already encoded
# encode features that are categorical classes
encoding_list = []
for column in categorical_classes_list:
    le = LabelEncoder()
    le.fit(training_set[column])
    encoding_list.append(training_set[column].unique())
    encoding_list.append(list(le.transform(training_set[column].unique())))
    training_set[column] = le.transform(training_set[column])
    test_set[column] = le.transform(test_set[column])

print(training_set.head())
training_set = pd.get_dummies(training_set, columns=['Embarked', 'Pclass', 'Title', 'Deck'])
print(training_set.head())
test_set = pd.get_dummies(test_set, columns=['Embarked', 'Pclass', 'Title', 'Deck'])

training_set, test_set = training_set.align(test_set, axis=1)
print(training_set['Survived'].head())
print(test_set['Survived'].head())
test_set.drop('Survived', axis=1, inplace=True)
test_set.fillna(0, axis=1, inplace=True)
# test_set.fillna(0, inplace=True)
y = training_set['Survived'].values
X = training_set.drop(['Survived','PassengerId'], axis=1).values
X_test = test_set.drop('PassengerId', axis=1).values
print(X)
