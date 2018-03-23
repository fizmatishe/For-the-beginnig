if __name__ == '__main__':
    input_list = ['v1', 'v2', 'v3']
    for index, value in enumerate(input_list):
        print(index, value)
    names = ('J', 'K', 'I')
    number = ["111", '22', '3']
    for i, name in zip(names, number):
        print(i, name)
    A = dict(zip(["Russia", "UK", "USA"],["MSC", "KIV", "WNG"]))
    for i in A:


    a = '{}://{}/{}'.format(
        'https',
        'google.com',
        'search'
    )
    print(a)