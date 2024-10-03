import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha1(password.encode ()).hexdigest()
        # self.password = hash(password)  # Хэш пароля
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
            if user.nickname == nickname and user.password == hashlib.sha1(password.encode()).hexdigest():
                self.current_user = user
                return
        print("Неверное имя пользователя или пароль")


    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user


    def log_out(self):
        self.current_user = None


    def add(self, *videos):
        for video in videos:
            if not any(v.title.lower() == video.title.lower() for v in self.videos):
                self.videos.append(video)


    def get_videos(self, search_word):
        result = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return result


    def watch_video(self, video_title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        found_video = None

        for video in self.videos:
            if video.title.lower() == video_title.lower():
                found_video = video

        if not found_video:
            print( "Видео не найдено")
            return

        if found_video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Просмотр видео: {found_video.title}")

        while found_video.time_now < found_video.duration:
            time.sleep(1)
            found_video.time_now += 1
            print(f"Время просмотра: {found_video.time_now} в секундах.")

        found_video.time_now = 0
        print("Конец видео")


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

