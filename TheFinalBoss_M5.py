import time


class UrTube:
    users = []  # Список объектов User (пользователей)
    videos = []  # Список объектов Video
    current_user = None  # Текущий пользователь *User

    def log_in(self, nickname, password):  # условно авторизация
        for user in self.users:  # Для user в списке пользователей
            if nickname == user.nickname and password == user.password:  # Если аргумент совпадает с именем и паролем пользователи
                self.current_user = user  # становится текущим пользователем

    def register(self, nickname, password, age):  # Регистрация
        for user in self.users:  # Для user в списке пользователей
            if nickname in user.nickname:  # Если имя уже занято
                print(f'Пользователь {nickname} уже существует')
                break
        else:  # если такого имени еще нетЖ
            user = User(nickname, password, age)  # создание пользователя
            self.users.append(user)  # добавление в список пользователей
            self.log_in(user.nickname, user.password)  # авторизация, выполнение входа

    def log_out(self):  # сброс
        self.current_user = None  # Сброс текущего пользователя

    def add(self, *args):  # Метод добавляет элементы в множество(если элемент уже есть, он не дублируется)
        for i in args:  # Для i в *args(неограниченное количество объектов класса Video
            self.videos.append(i)  # добавление в список объектов

    def get_videos(self, text):  # Принимает поисковое слово
        list = []  # Список всех названий video
        for video in self.videos:  # Для video в списке объектов video
            if text.upper() in video.title.upper():  # Если поисковое слова(ниж.рег) в списке заголовков(ниж.рег)
                list.append(video.title)  # добавить в список list
        return list  # Вернуть список всех названий

    def watch_video(self, movie):
        if self.current_user and self.current_user.age < 18:  # Проверка на возраст 18+
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:  # Если текущий пользователь
            for video in self.videos:  # Для видео в списке videos
                if movie in video.title:  # Если название фильма есть в заголовках
                    for j in range(1, 11):  # отчет просмотра с 1вой по 10ю секунды
                        print(j, end=' ')
                        time.sleep(1)  # для паузы между выводами секунд воспроизведения
                    print('Конец видео.')
        else:  # Если пользователь авторизован
            print('Для просмотра, выполните Вход.')

    def __repr__(self):  # отображение информации об объекте класса в режиме отладки
        return f'{self.videos}'


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title  # Заголовок
        self.duration = duration  # Продолжительность
        self.time_now = time_now  # Секунда остановки *изначально = 0
        self.adult_mode = adult_mode  # Ограничение по возрасту *по умолчанию = False

    def __str__(self):  # отображение информации об объекте класса для пользователей
        return f'{self.title}'  # Возврат заголовка


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname  # Имя пользователя
        self.password = password  # Пароль
        self.age = age  # Возраст

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return f'{self.nickname}'  # Возврат имени авторизованного пользователя

    def __eq__(self, other):
        return self.nickname == other.nickname


# Проверка
if __name__ == '__main__':
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
ur.register('vasya_pypkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4lJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pypkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
