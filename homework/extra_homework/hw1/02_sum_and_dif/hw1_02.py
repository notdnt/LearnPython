num = int(input("Введите число: "))
def sumi(num):
    result = 0
    while num > 0:
        digit = num % 10
        result += digit
        num //= 10
    return result
print("Сумма чисел:", sumi(num))

def count_digits(num):
    result = 0
    while num > 0:
        digit = num % 10
        result += 1
        num //= 10
    return result
print("Количество цифр в числе:",count_digits(num))

print("Разность:", sumi(num)-count_digits(num))