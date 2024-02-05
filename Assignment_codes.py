# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:24:06 2024

@author: LAHAI IRADUKUNDA
"""
import matplotlib.pyplot as plt
import pandas as pd

df =pd.read_csv("C:/Users/LAHAI IRADUKUNDA/Desktop/Coding summer school/Coding summer school/movie_dataset.csv")

print(df.describe())

print(df['Rating'].max())


movies_2016= df[(df['Year'] >= 2016)]

num_movies_2016 = len(movies_2016)

print( '{num_movies_2016}')


#movies directed by Chris
movies_chris= df[df['Director'] == 'Christopher Nolan']

num_movies_chris =len(movies_chris)

print( '{num_movies_chris}')


movies_Rated= df[(df['Rating'] >= 8)]

num_movies_Rated = len(movies_Rated)

print( '{num_movies_rated}')

# Split genres and create a list of all genres
all_genres = [genre.split(', ') for genre in df['Genre']]
flat_genres = [item for sublist in all_genres for item in sublist]

# Get unique genres
unique_genres = set(flat_genres)

# Count the number of unique genres
num_unique_genres = len(unique_genres)

# Print the result
print(' {num_unique_genres}')


median_rating = movies_chris['Rating'].median()

# Print the result
print(f"The median rating of movies directed by Chris is: {median_rating}")


average_ratings_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
max_avg_year = average_ratings_by_year.idxmax()
max_avg_rating = average_ratings_by_year.max()

print(f'The year with the highest average rating is {max_avg_year} with an average rating of {max_avg_rating:.2f}')


# Replace 'Release_Year' with the actual column name in your dataset
movies_between_2006_2016 = df[(df['Year'] >= 2006) & (df['Year'] <= 2016)]

# Get the number of movies released between 2006 and 2016
num_movies_2006_2016 = len(movies_between_2006_2016)

print("{num_movies_2006_2016}")


# Split the actors in the "Actors" column and create a new DataFrame with one actor per row
actors_df = df['Actors'].str.split(', ', expand=True).stack().reset_index(level=0, drop=True).reset_index(name='Actor')

# Find the most common actor
most_common_actor = actors_df['Actor'].value_counts().idxmax()

# Print the result
print(f"The most common actor in all movies is: {most_common_actor}")

# Drop rows with missing values in the 'Revenue' column
df = df.dropna(subset=['Revenue (Millions)'])

# Calculate the average revenue
average_revenue = df['Revenue (Millions)'].mean()

# Print the result
print(f"The average revenue of all movies in the dataset is: {average_revenue}")


filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Drop rows with missing values in the 'Revenue' column
filtered_df = filtered_df.dropna(subset=['Revenue (Millions)'])

# Calculate the average revenue for the filtered data
average_revenue_2015_2017 = filtered_df['Revenue (Millions)'].mean()

# Print the result
print(f"The average revenue of movies from 2015 to 2017 is: {average_revenue_2015_2017}")

df = df.dropna(subset=['Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore'])

# Create a scatter plot
fig, ax = plt.subplots()
ax.set_title("Rating vs Year")
ax.set_xlabel('Runtime (Minutes)')
ax.set_ylabel('Rating')
ax.grid()

# Scatter plot using specified columns
ax.scatter(df['Runtime (Minutes)'], df['Rating'])
plt.show()


correlation_matrix = df[['Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']].corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)












