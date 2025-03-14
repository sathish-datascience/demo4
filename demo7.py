import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("movies.csv")
print(df.head())
print(df.columns)
top = df.sort_values(by="popularity",ascending=False).head(12)
sns.barplot(y = top['title'],x=top['popularity'])
plt.show()

top_rated = df[df['vote_count']>500].sort_values(by="vote_average",ascending=False).head(12)
sns.barplot(y=top_rated['title'],x=top_rated['vote_average'])
plt.show()

df['release_date'] = pd.to_datetime(df['release_date'])
df['year'] = df['release_date'].dt.year

sns.lineplot( x = df['year'].value_counts().index,
                    y = df['year'].value_counts().values,
                    marker="*",color="red")
plt.show()