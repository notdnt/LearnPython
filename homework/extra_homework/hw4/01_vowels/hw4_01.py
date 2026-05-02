string = input("Введите текст: ")
vowels = ["у", "е", "а", "о", "э", "и", "ю", "ё", "ы", "я"]
list = []
for letter in string:
    if letter in vowels:
        list.append(letter)
print(f"Список гласных букв: {list}")
print(f"Длина списка: {len(list)}")
