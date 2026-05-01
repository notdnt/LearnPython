num = int(input("Введите количество видеокарт:"))
list = []
for i in range(num):
    list.append(int(input("Введите модель:")))
def func(list):
    for i in list:
        if i == max(list):
            list.remove(i)
    return list
print(func(list))


