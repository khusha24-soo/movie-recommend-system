import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse= True , key = lambda x: x[1])[1:6]


    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dist = pickle.load(open("movie_dict.pkl" , "rb"))
movies = pd.DataFrame(movies_dist)

similarity = pickle.load(open("similarity.pkl" , 'rb'))



st.title("Movie recommend system ")

selected_movie = st.selectbox("enter the movie title",
                      movies['title'].values)

if st.button('Recommend movie'):
    recommendation = recommend(selected_movie)
    for i in recommendation:
        st.write(i)



