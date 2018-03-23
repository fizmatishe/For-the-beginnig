import tmdb_api


if __name__ == '__main__':
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

    with open('data_movies_text', 'w', encoding='utf-8') as file:
        file.write(str(data_movies))


