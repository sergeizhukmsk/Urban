# number = 25
# if number % 6 == 0 and number % 5 == 0:
#     print('БухБах')
# elif number % 6 == 0:
#     print('Бух')
# elif number % 5 == 0:
#     print('Бах')
# else:
#     print('Не Бух и не Бах')

# age = input('Enter your age')
# name = input('Enter your name')
# age = int(age)
# print(name, age)

# for i in range(len('sum')):
#     if i != 2:
#         print('sum'[i], end='-')
#     else:
#         print("sum"[1])

def calculate_age(birth_year, now_year=2024):
    user_age = now_year - birth_year
    return user_age

my_year = 2000

result = calculate_age(my_year)
print(result)
