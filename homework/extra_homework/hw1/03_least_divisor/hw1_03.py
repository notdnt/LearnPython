num = int(input("Введите число:"))
def least_divider(num):
    for i in range(2, num+1):
        if num % i == 0:
            return i
print(least_divider(num))