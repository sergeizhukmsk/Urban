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

        print('item0 = ', item, 'type_item0 = ', type(item), 'item0 nums = ', nums, 'strings = ', strings)

        if isinstance(item, str):
            nums += len(item)
            print('item_str_end nums', nums, 'strings = ', strings)

        elif isinstance(item, int):
            nums += item
            print('item_int_end nums = ', nums, 'strings = ', strings)

        elif isinstance(item, list):

            for lst in item:
                print('Обходим все элементы списка list - lst_for = ', lst, 'type_lst = ', type(lst), 'lst_item nums = ', nums, 'strings = ', strings)

                if isinstance(lst, int):
                    nums += lst
                elif isinstance(lst, str):
                    nums += len(lst)
                else:
                    print('Рекурсивно обрабатываем список list')
                    nums, strings = calculate_structure_sum([lst], nums, strings)
                    print('item_list_recur nums = ', nums, 'strings = ', strings)

            print('item_list_end nums = ', nums, 'strings = ', strings)

        elif isinstance(item, dict):
            print('item_dict = ', item, 'item_dict_0 nums = ', nums, 'strings = ', strings)

            for key in item:
                value = item[key]
                print('key = ', key, 'value = ', value)

                if isinstance(key, str):
                    nums += len(key)
                if isinstance(value, int):
                    nums += value
                elif isinstance(value, str):
                    nums += len(value)

                print('item_dict_end nums = ', nums, 'strings = ', strings)

        elif isinstance(item, set):
            print('item_set = ', item, 'item_set_0 nums = ', nums, 'strings = ', strings)

            for st in item:
                print('Обходим все элементы множества - st_for = ', st, 'type_st = ', type(st), 'st_item nums = ', nums, 'strings = ', strings)

                if isinstance(st, int):
                    nums += st
                elif isinstance(st, str):
                    nums += len(st)
                else:
                    print('Рекурсивно обрабатываем множество')
                    nums, strings = calculate_structure_sum([st], nums, strings)
                    print('item_set_recur nums = ', nums, 'strings = ', strings)

            print('item_set_end nums = ', nums, 'strings = ', strings)

        elif isinstance(item, tuple):
            #print('item_0 = ', item, 'item_tuple_0 nums = ', nums, 'strings = ', strings)

            for tup in item:
                print('Обходим кортеж - tup_for = ', tup, 'type_tup = ', type(tup), 'tup_item nums = ', nums, 'strings = ', strings)

                if isinstance(tup, int):
                    nums += tup
                    print('item_tup_int nums = ', nums, 'strings = ', strings)
                elif isinstance(tup, str):
                    nums += len(tup)
                else:
                    print('Рекурсивно обрабатываем вложенный кортеж')
                    print('tup = ', tup)
                    nums, strings = calculate_structure_sum([tup], nums, strings)
                    print('item_tup_recur nums = ', nums, 'strings = ', strings)

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

