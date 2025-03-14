import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("movies.csv")

print(df.head())

print(df.columns)

top = df.sort_values(by="popularity",ascending=False).head(10)
print(top)
print(top.iloc[:,0:3])

sns.barplot(y=top['title'],x=top['popularity'],palette='viridis')
plt.title("Top ten movies")
plt.xlabel("popularity score")
plt.ylabel("movie name")
plt.show()


top_rated = df[df['vote_count']>500].sort_values(by="vote_average",ascending=False).head(13)
print("top_rated")
print(top_rated)

sns.barplot(y=top_rated['title'],x=top_rated['vote_average'],palette="coolwarm")
plt.title("top rating movies")
plt.xlabel("voting score")
plt.ylabel("Movie Name")
plt.show()




