import streamlit as st
import pickle
import pandas as pd
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
data = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

def recommend(movie):
    movie_index = data[data["title"] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:10]
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(data.iloc[i[0]].title)
    return recommended_movies
selected_movie_name = st.selectbox("how old are you",data['title'].values)

if st.button('Recommend'):
    recom=recommend(selected_movie_name)
    for i in recom:
        print(i)
        st.write(i)
