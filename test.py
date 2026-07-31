# import requests
# import time

# session = requests.Session()
# API_KEY = "cd2afdefcd4227751adc16a7f240fc72"


# for movie_id in [58, 1865]:
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

#     try:
#         response = session.get(url, timeout=10)
#         print(movie_id, response.status_code)
#     except Exception as e:
#         print(movie_id, e)

