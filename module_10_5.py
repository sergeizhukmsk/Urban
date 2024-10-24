# Модуль №10 Домашняя работа 5

import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

    #return all_data


if __name__ == '__main__':

    filenames = [f'./FilesProz/file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f'Время выполнения линейного вызова: {linear_duration:.2f} секунд')
    # Время выполнения линейного вызова: 39.38 секунд
    # return all_data
    # Время выполнения многопроцессного вызова: 32.08 секунд

    # Многопроцессный вызов
    start_time = time.time()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    parallel_duration = time.time() - start_time
    print(f'Время выполнения многопроцессного вызова: {parallel_duration:.2f} секунд')
    # Время выполнения многопроцессного вызова: 57.33 секунд
    # return all_data
    # Время выполнения многопроцессного вызова: 29.68 секунд



