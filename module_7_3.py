# Модуль № 7 Домашнее задание № 3

class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read().lower().replace(',', '').replace('.', '').replace('=', '').replace('!',
                                                                                                       '').replace('?', '').replace(':', '').replace(';', '').replace(' - ', '')
                words = content.split()
                all_words[filename] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        results = {}
        for filename, words in all_words.items():
            if word in words:
                try:
                    index = words.index(word) + 1
                except ValueError:
                    index = None
                results[filename] = index
        return results

    def count(self, word):
        all_words = self.get_all_words()
        results = {}
        for filename, words in all_words.items():
            cnt = words.count(word)
            results[filename] = cnt
        return results

# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('text'))  # Найти первое вхождение слова 'text'
print(finder2.count('text'))  # Количество вхождений слова 'text'

