num = int(input("Введите число:"))
def counter(num):
    list = []
    for i in range(1,num+1):
        if i % 2 != 0:
            list.append(i)
    return list
print(counter(num))