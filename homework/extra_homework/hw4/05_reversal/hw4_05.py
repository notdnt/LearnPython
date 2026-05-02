str = input("Введите строку: ")
first_h = str.find("h")
last_h = str.rfind("h")
result = str[first_h+1:last_h]
if result == "":
    result += "h"
print(f"Развёрнутая последовательность между первым и последним h: {result[::-1]}")