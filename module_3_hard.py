
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(structure, nums=0, strings=0):

    print('structure = ', structure)

    for item in structure:

        print('item0 = ', item, 'type_item0 = ', type(item))

        if isinstance(item, str):
            nums += len(item)
            print('item_str nums', nums, 'strings = ', strings)

        elif isinstance(item, int):
            #print('isinstance_item_int', item)
            nums += item
            print('item_int nums = ', nums, 'strings = ', strings)

        elif isinstance(item, list):
            #print('Рекурсивно вызываем функцию для списка')
            #print('isinstance_item_list')
            new_nums = 0
            new_strings = 0
            nums, strings = calculate_structure_sum(item, new_nums, new_strings)
            #nums += new_nums
            #strings += new_strings
            print('item_list nums = ', nums, 'strings = ', strings)
            #continue

        elif isinstance(item, dict):
            print('item_dict_0 nums = ', nums, 'strings = ', strings)

            for key in item:
                value = item[key]
                #print('key = ', key, 'value = ', value)

                if isinstance(key, str):
                    nums += len(key)
                if isinstance(value, int):
                    nums += value
                elif isinstance(value, str):
                    nums += len(value)

                print('item_dict_1 nums = ', nums, 'strings = ', strings)

        elif isinstance(item, set):
            print('item_0 = ', item, 'item_set_0 nums = ', nums, 'strings = ', strings)

            for st in item:
                print('Обходим все элементы множества - st_for = ', st, 'type_st = ', type(st))
                #print('Обходим все элементы множества - st_for = ', st, 'st_item nums = ', nums, 'strings = ', strings)

                if isinstance(st, int):
                    nums += st
                elif isinstance(st, str):
                    nums += len(st)
                else:
                    print('Рекурсивно обрабатываем вложенные структуры множества')
                    new_nums = 0
                    new_strings = 0
                    nums, strings = calculate_structure_sum([st], new_nums, new_strings)
                    #print('item_set_1 new_nums = ', new_nums, 'new_strings = ', new_strings)
                    #nums += new_nums
                    #strings += new_strings
                    print('item_set_2 nums = ', nums, 'strings = ', strings)

            print('item_set_end nums = ', nums, 'strings = ', strings)

        elif isinstance(item, tuple):
            print('item_0 = ', item, 'item_tuple_0 nums = ', nums, 'strings = ', strings)

            for tup in item:
                print('Обходим все элементы кортежа - tup_for = ', tup, 'type_tup = ', type(tup))
                #print('Обходим все элементы кортежа - tup_for = ', tup, 'tup_item nums = ', nums, 'strings = ', strings)

                if isinstance(tup, int):
                    nums += tup
                elif isinstance(tup, str):
                    nums += len(tup)
                else:
                    print('Рекурсивно обрабатываем вложенные структуры кортежа')
                    new_nums = 0
                    new_strings = 0
                    print('tup = ', tup)
                    nums, strings = calculate_structure_sum([tup], new_nums, new_strings)
                    print('item_tup_1 new_nums = ', new_nums, 'new_strings = ', new_strings)
                    #nums += new_nums
                    #strings += new_strings
                    print('item_tup_2 nums = ', nums, 'strings = ', strings)

            print('item_tuple_end nums = ', nums, 'strings = ', strings)

        else:
            continue

    return nums, strings


data_structure_0 = [
    [1, 2, 3],
    {'a': 4, 'b': 5}
]

data_structure_1 = [
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5}
# ]

nums, strings = calculate_structure_sum(data_structure)
print(nums, strings)

# result_0 = (1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 +
#          len('drum') + 8 + len("Hello") + len(()) + 2 + len('Urban') + len('Urban2') + 35)
# print('result_0 = ', result_0)

