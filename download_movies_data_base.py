import tmdb_api
import json
import urllib.request


def download_most_popular_movies():
    data_movies = []
    films_number = 1000
    current_page = 1
    while len(data_movies) < films_number:
        response = tmdb_api.make_tmdb_api_request(
            method='/discover/movie',
            extra_params={
                'sort_by': 'popularity.desc',
                'page': current_page
            },
            api_key=tmdb_api.API_KEY
        )
        data_movies += response['results']
        current_page += 1
    return data_movies


if __name__ == '__main__':
    movie_list_file = open('movies_base', 'w', encoding='utf-8')
    try:
        json.dump(
            download_most_popular_movies(),
            movie_list_file,
        )
    except urllib.error.URLError:
        print('Something wrong with connection')
    finally:
        movie_list_file.close()
        print('File "movies_base" closed')
