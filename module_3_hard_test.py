data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(structure, nums=0, strings=0):

    print(structure)

    for item in structure:

        print('item = ', item)

        if isinstance(item, list):
            print("List: ", item)
        elif isinstance(item, dict):
            print("Dictionary: ", item)
        elif isinstance(item, tuple):
            print("Tuple: ", item)
        else:
            print("String: ", item)


#result = calculate_structure_sum(data_structure)
result = len(data_structure)
print(result)