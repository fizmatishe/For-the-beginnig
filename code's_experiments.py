#if __name__ == '__main__':
#     input_list = ['v1', 'v2', 'v3']
#     for index, value in enumerate(input_list):
#         print(index, value)
#     names = ('J', 'K', 'I')
#     number = ["111", '22', '3']
#     for i, name in zip(names, number):
#         print(i, name)
#     A = dict(zip(["Russia", "UK", "USA"],["MSC", "KIV", "WNG"]))
a = '{}://{}/{}'.format(
    'https',
    'google.com',
    'search'
)
print(a)
s = [{"A": "B"}, {"c": "d"}]
for iterate_list in s:
    print(s)
    for iterate_book in iterate_list.values():
        iterate_book = iterate_book.lower()
print(s)