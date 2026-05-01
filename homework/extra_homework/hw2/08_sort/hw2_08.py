length = int(input("Введите длину списка:"))
numbers = []
for i in range(length):
    numbers.append(int(input("Введите число:")))
for i in range(length - 1):
    for j in range(i + 1, length):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)