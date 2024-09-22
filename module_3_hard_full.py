def calculate_structure_sum_1(*args):
    total_numbers = 0
    total_strings = 0

    #print('total_numbers_0 = ', total_numbers)
    #print('total_strings_0 = ', total_strings)

    for arg in args:
        print('arg = ', arg, print('args = ', args))
        if isinstance(arg, int) or isinstance(arg, float):
            total_numbers += arg
            print('total_numbers_1 = ', total_numbers)
            #print('total_strings_1 = ', total_strings)

        elif isinstance(arg, str):
            total_numbers += arg
            total_strings += 1
            print('total_numbers_2 = ', total_numbers)
            #print('total_strings_2 = ', total_strings)

        elif isinstance(arg, dict):
            sub_total_numbers, sub_total_strings = calculate_structure_sum_1(*arg.values())
            total_numbers += sub_total_numbers
            total_strings += sub_total_strings
            print('total_numbers_3 = ', total_numbers)
            #print('total_strings_3 = ', total_strings)

        elif isinstance(arg, tuple) or isinstance(arg, list):
            sub_total_numbers, sub_total_strings = calculate_structure_sum_1(*arg)
            total_numbers += sub_total_numbers
            total_strings += sub_total_strings
            print('total_numbers_4 = ', total_numbers)
            #print('total_strings_4 = ', total_strings)

    return total_numbers, total_strings


def calculate_structure_sum(structures, nums = 0, strings = 0):
    for s in structures:
        if isinstance(s, dict):
            print('Обходим все ключи и значения в словаре')
            print('s = ', s)
            for key in s:
                value = s[key]
                print('key = ', key, 'value = ', value)
                if isinstance(key, str):
                    nums += len(key)
                    #nums += value
                    strings += 1
                if isinstance(value, int):
                    nums += value
                if isinstance(value, str):
                    nums += len(value)
                    strings += 1
                else:
                    print('Рекурсивно обрабатываем вложенные структуры в словаре')
                    calculate_structure_sum([value], nums, strings)

        elif isinstance(s, list):
            print('Рекурсивно вызываем функцию для списка')
            return calculate_structure_sum(s, nums, strings)

        elif isinstance(s, tuple):
            print('Обходим все элементы кортежа')
            for item in s:
                if isinstance(item, int):
                    nums += item
                elif isinstance(item, str):
                    strings += 1
                else:
                    print('Рекурсивно обрабатываем вложенные структуры кортежа')
                    calculate_structure_sum([item], nums, strings)

        elif isinstance(s, str):
            strings += 1
        elif isinstance(s, int):
            nums += s
        else:
            continue

    return nums, strings


data_structure_0 = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5}
# ]

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}]
#data_structure = [{'a': 4, 'b': 5}]

#result_0 = (1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 +
#          len('drum') + 8 + len("Hello") + len(()) + 2 + len('Urban') + len('Urban2') + 35)
#print(result_0)

#result_0 = (1 + 2 + 3 + len('a') + 4 + len('b') + 5)
#print(result_0)


nums, strings = calculate_structure_sum(data_structure)
print(nums, strings)

#total_numbers, total_strings = calculate_structure_sum_1(data_structure)
#print(total_numbers, total_strings)
