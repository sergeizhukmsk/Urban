class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)  # Хэш пароля
        self.age = age

    def __repr__(self):
        return f"User({self.nickname}, {self.password}, {self.age})"

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video({self.title}, {self.duration}, {self.adult_mode})"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                break
        else:
            print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(other_video.title.lower() == video.title.lower() for other_video in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        matching_titles = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return matching_titles

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")

        elif any(video.title == title for video in self.videos):
            found_video = next((video for video in self.videos if video.title == title), None)

            if found_video.adult_mode and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
            else:
                import time
                for i in range(found_video.duration):
                    #print(i + 1)
                    print(f"Время просмотра: {i + 1} в секундах.")
                    time.sleep(1)
                print("Конец видео")

        else:
            print("Видео не найдено")


# Пример использования
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

