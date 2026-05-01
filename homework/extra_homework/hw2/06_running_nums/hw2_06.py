k = int(input("Сдвиг:"))
num = int(input("Введите количество чисел:"))
list = []
for i in range(num):
    list.append(int(input("Введите число:")))
print(list)
k = k % num
if k == 0:
    result = list
else:
    result = list[-k:] + list[:-k]

print(result)