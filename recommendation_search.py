import json


def recommend_movies(key_word):
    search_result = []
    with open('movies_base', 'r') as file:
        movies_base_list = json.load(file)
    original_popularity = 0
    original_vote = 0

    for similar_films in movies_base_list:
        if similar_films['original_title'] == key_word:
            original_popularity = float(similar_films['popularity'])
            original_vote = float(similar_films['vote_average'])
    if original_vote == 0:
        search_result.append('No movies were found by your search')
        return search_result
    else:
        for films in movies_base_list:
            popularity = float(films['popularity'])
            vote = float(films['vote_average'])
            if ((popularity - 50 <= original_popularity <=
                popularity + 50) or
                    (vote - 0.3 <= original_vote <= vote + 0.3)):
                search_result.append(films)
        return search_result


if __name__ == '__main__':
    input_word = input('Enter key word:  ')
    print(recommend_movies(input_word))
