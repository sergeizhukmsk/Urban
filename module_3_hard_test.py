data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# list1, dict1, tuple1, str1, tuple2 = data_structure
#
# print('list1 = ', list1)  # [1, 2, 3]
# print('dict1 = ', dict1)  # {'a': 4, 'b': 5}
# print('tuple1 = ', tuple1)  # (6, {'cube': 7, 'drum': 8})
# print('str1 = ', str1)  # "Hello"
# print('tuple2 = ', tuple2)  # ((), [{(2, 'Urban', ('Urban2', 35))}]


def calculate_structure_sum(*args):
    print(*args)

    for item in data_structure:

        print('item = ', item)

        if isinstance(item, list):
            print("List: ", item)
        elif isinstance(item, dict):
            print("Dictionary: ", item)
        elif isinstance(item, tuple):
            print("Tuple: ", item)
        else:
            print("String: ", item)




result = calculate_structure_sum(data_structure)
print(result)