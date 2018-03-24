import json


def recommend_movies(key_word):
    search_result = []
    with open('movies_base', 'r') as file:
        movies_base_list = json.load(file)
    for similar_films in movies_base_list:
        if similar_films['original_title'] == key_word:
            search_result.append(similar_films['popularity'])
            search_result.append(similar_films)

    for films in movies_base_list:
        popularity = float(films['popularity'])
        vote = float(films['vote_average'])
        if ((popularity - 100 <= float(search_result[0]) <= popularity + 100) or
                (vote - 0.3 <= search_result[1] <= vote + 0.3)):
            search_result.append(films)
    return set(search_result)


if __name__ == '__main__':
    input_word = input('Enter key word:  ').lower()
    print(recommend_movies(input_word))
