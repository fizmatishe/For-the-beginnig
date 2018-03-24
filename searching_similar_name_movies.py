import json


def finding_movies_by_word(input_word):
    search_result = []
    with open('movies_base', 'r') as file:
        movies_base_list = json.load(file)
    for movie_title in movies_base_list:
        if movie_title['original_title'].lower().find(input_word) != -1:
            search_result.append(movie_title)
    if search_result:
        return search_result
    else:
        return 'No films were found'


if __name__ == '__main__':
    input_word = input('Enter key word: ').lower()
    print(finding_movies_by_word(input_word))
