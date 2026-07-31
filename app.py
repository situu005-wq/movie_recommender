import requests
import streamlit as st
import pickle
import time
movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values
print(movies_list)
st.title("Movie Recommender System")
options = st.selectbox(
   "Choose a movie from the list:",
   movies_list
)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=cd2afdefcd4227751adc16a7f240fc72&language=en-US"
    try:
        print("Fetching:", movie_id)
        response = requests.get(url, timeout=10)
        print("Status:", response.status_code)
        print("Response:", response.text)
        data = response.json()
        print(data)
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
            
    except Exception as e:
        print(e)
        return "https://via.placeholder.com/500x750?text=Unavailable"

def recommended(selected_movies):
    movie_index = movies[movies['title'] == selected_movies].index[0]
    distances =similarity[movie_index]
    m_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []
    for i in m_list:
        #fetch poster from API
        movie_id = movies.iloc[i[0]].movie_id   
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        time.sleep(0.5)  # Add a small delay to avoid hitting the API too quickly
    return recommended_movies, recommended_posters

similarity = pickle.load(open('similarity.pkl', 'rb'))


if st.button('Recommend'):
    recommended_movies, recommended_posters = recommended(options)
    col1, col2, col3, col4, col5 = st.columns(5)
    for i in range(5):
        with [col1, col2, col3, col4, col5][i]:
            st.text(recommended_movies[i])

            if recommended_posters[i]:
                st.image(recommended_posters[i])
            else:
                st.write("Poster not available")
        