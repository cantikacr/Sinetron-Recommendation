import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_data = pd.read_csv("listsinetron.csv")

selected_features = ['Pemeran', 'Genre', 'Produksi']

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

combined_features = movies_data['Genre'] + ' ' +movies_data['Pemeran'] + ' ' +movies_data['Produksi']

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

movie_name = input(' Enter Your Favourite Movie Name: ')

list_of_all_titles = movies_data['title'].tolist()
similarity = cosine_similarity(feature_vectors)
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match = find_close_match[0]
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
similarity_score = list(enumerate(similarity[index_of_the_movie]))

mauapa = movies_data['title'] + ' . ' +movies_data['Genre'] + ' . ' +movies_data['Pemeran'] + ' . ' +movies_data['Produksi']
print(mauapa)

movie_name = input("Enter your favourite Indonesian Series Movies: ")
list_of_all_titles = movies_data['title'].tolist()
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match = find_close_match[0]
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print('Movies suggested for you: \n')

i=1

for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index==index]['title'].values[0]
    if (i<11):
        print(i, ' .', title_from_index)
        i+=1