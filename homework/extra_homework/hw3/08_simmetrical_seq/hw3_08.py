amount = int(input("Количество чисел: "))
numbers = [int(input("Число: ")) for x in range(amount)]

def is_palindrome(num):
    return num == num[::-1]

start = 0
while not is_palindrome(numbers[start:]):
    start += 1

final = numbers[:start][::-1]

print(f"Последовательность: {numbers}")
print(f"Нужно приписать чисел: {start}")
print(f"Сами числа: {final}")