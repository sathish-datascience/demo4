import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("movies.csv")

d = {'Unnamed: 0', 'id'}
df = df.drop(columns=d)
print(df.columns)


#top rated movies code

top = df.sort_values(by="popularity",ascending=False).head(12)
sns.barplot(y = top['title'] ,x = top['popularity'],palette='coolwarm')
plt.title("top ten popularity movies")
plt.ylabel("movie name")
plt.xlabel("popularity")
plt.show()

top_rated = df[df['vote_count']>500].sort_values(by="vote_average",ascending=False).head(10)
plt.title("voting per ")
sns.barplot(y = top_rated['title'],x=top_rated['vote_average'],palette='viridis')
plt.show()

df['release_date'] = pd.to_datetime(df['release_date'])
df['year'] = df['release_date'].dt.year

sns.lineplot(	x = df['year'].value_counts().index,
		y = df['year'].value_counts().values,
		marker = "*",color="red")
plt.title("year wise count")

plt.show()