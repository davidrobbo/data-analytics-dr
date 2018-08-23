import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import time
import datetime

DATA_DIR = '../data/movies/'
OUTPUT_DIR = '../output/movies/'

df = pd.read_csv(DATA_DIR + 'movies.csv')

#print(df.head().to_string())
#print(df.describe().to_string())

df.homepage = df.homepage.fillna('')
df.overview = df.overview.fillna('')
print(df[df.id > 380095].sort_values(by=['id']).to_string())
#print(df.isnull().sum())


def to_timestamp(date_string):

    if date_string is False:
        return 0
    return time.mktime(datetime.datetime.strptime(date_string, "%Y-%m-%d").timetuple())


df['release_date_time'] = df['release_date'].map(to_timestamp)
scatter_matrix(df)
plt.savefig(OUTPUT_DIR + "scatter.png", bbox_inches='tight')
plt.close()



