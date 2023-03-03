import pandas as pd
import streamlit as st

import joblib
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=bbe6c62020b0db8cabf2ab89dc536c64&language=en-US'.format(movie_id))
    data=response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity1[index])),reverse=True,key = lambda x: x[1])
    recommeded_movies=[]
    recommended_poster=[]
    for i in distances[1:6]:
        movie_pic=movies.iloc[i[0]].movie_id
        recommeded_movies.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_pic))
    return recommeded_movies,recommended_poster


movies_dict=joblib.load('movies_dict1.pkl')
movies=pd.DataFrame(movies_dict)
similarity1=joblib.load('similarity.pkl')
st.title('Movie Recommendation system')


selcted_movie_name=st.selectbox('select the movie',movies['title'].values)

if st.button('Recommend'):
    names,poster=recommend(selcted_movie_name)

    col1,col2,col3,col4,col5 =st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
