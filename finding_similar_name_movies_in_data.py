import download_movies_data_base
import json


def finding_movies_by_word(input_word):
    search_result = []
    with open('movie_list', 'r') as file:
        movies_base_list = json.load(file)
    for movie_title in movies_base_list:
        if movie_title['original_title'].lower().find(input_word) != -1:
            search_result.append(movie_title)
    return search_result


if __name__ == '__main__':
    print('Enter key word:', end=' ')
    input_word = input().lower()
    print(finding_movies_by_word(input_word))
