len = int(input("Введите длину списка: "))
result = []
for i in range(len):
    if i % 2 == 0:
        result.append(1)
    else:
        result.append(i%5)
print(f"Результат: {result}")