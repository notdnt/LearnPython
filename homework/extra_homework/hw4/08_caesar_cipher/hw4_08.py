alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
message = input("Введите сообщение: ")
k = int(input("Введите сдвиг: "))
final = ""
for i in message:
    if i not in alphabet:
        final += i
        continue
    s = alphabet.find(i)
    final += alphabet[(s + k) % 33]
print(f"Зашифрованное сообщение: {final}")