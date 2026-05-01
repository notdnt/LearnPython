films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
def func(films):
    amount = int(input("Сколько фильмов хотите добавить? "))
    fav = []
    for i in range(amount):
        film = input("Введите название фильма:")
        if film in films:
            fav.append(film)
        else:
            print(f"Ошибка: фильма {film} у нас нет :(")
    return fav
print("Ваш список любимых фильмов:", ", ".join(func(films)))