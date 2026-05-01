
num = int(input("Количество контейнеров: "))
list = []

for i in range(num):
    while True:
        try:
            weight = int(input("Введите вес контейнера: "))
            if weight >= 200:
                print("Ошибка! Вес должен быть меньше 200")
                continue
            list.append(weight)
            break
        except ValueError:
            print("Введите число!")

new_container = int(input("Введите вес нового контейнера: "))

position = len(list) + 1
for i in range(len(list)):
    if new_container > list[i]:
        position = i + 1
        break
print(f"Номер, который получит новый контейнер: {position}")
