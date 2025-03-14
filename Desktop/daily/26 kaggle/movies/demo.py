import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("movies.csv")

d = {'Unnamed: 0', 'id'}
df = df.drop(columns=d)


#top rated movies code

top = df.sort_values(by="popularity",ascending=False).head(10)
sns.barplot(y=top['title'],x=top['popularity'],palette="Set1")
plt.title("Top rated Movies")
plt.ylabel("Movie Names")
plt.xlabel("Popularity Score")
plt.show()

#top voting movies

top_rated = df[df['vote_count']>500].sort_values(by="vote_average",ascending=False).head(10)
sns.barplot(y=top_rated['title'],x=top_rated['vote_average'],palette = "coolwarm")
plt.title("top 10 highest rated movies")
plt.ylabel('Movie title')
plt.xlabel("rating")
plt.show()

#year wise release movies
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')


df['release_year'] = df['release_date'].dt.year

plt.figure(figsize=(12,10))
sns.lineplot(x=df['release_year'].value_counts().index,
		y = df['release_year'].value_counts().values,
		marker = "*",color="red")
plt.title("Number of Movies Released per year")
plt.xlabel("Year")
plt.ylabel("Number of movies")
plt.show()