test_dict_list = [
    {"name": "Taro", "age": 37},
    {"name": "Hanako", "age": 37},
    {"name": "Ken", "age": 9},
    {"name": "Dai", "age": 20},
]

extract_list = list(
    filter(
        lambda item: item['age'] == 37,
        test_dict_list))
print(extract_list)
