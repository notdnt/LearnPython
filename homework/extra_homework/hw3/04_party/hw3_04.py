guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    check = input("Гость пришёл/ушёл? ")
    if check == "Пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
    name = input("Имя гостя: ")
    if check == "пришёл" and len(guests) < 6:
        guests.append(name)
        print(f"Привет, {name}!")
    elif check == "пришёл" and len(guests) >= 6:
        print(f"Прости, {name}, но мест нет.")
    elif check == "ушёл":
        guests.remove(name)
        print(f"Пока, {name}!")