length = int(input("Введите длину списка:"))
numbers = []
for i in range(length):
    numbers.append(int(input("Введите число:")))
#[2 111 1 2 8 0 9]
for i in range(length - 1):
    if numbers[i] %  2 == 0:
        continue
    for j in range(i + 1, length):
        if numbers[j] % 2 == 0:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            break
print(numbers)

index = length
for n in range(length):
  if numbers[n] % 2 != 0:
      index = n
      break

for i in range(index - 1, -1, -1):
    print(numbers[i])


