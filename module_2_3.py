my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

num = 0
while num <= len(my_list):

    if my_list[num] == 0:
        num = num + 1
        continue

    if my_list[num] < 0:
        break

    print('Значение my_list = ' + str(my_list[num]))

    num = num + 1

    if num == len(my_list):
        break
