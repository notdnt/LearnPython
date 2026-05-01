word = input("Введите слово:" )
centre = len(word) // 2
print(len(word))
print(centre)
flag = True
for i in range(centre):
    j = len(word) - i - 1
    if word[i] != word[j]:
        flag = False
        break
if flag:
    print(f"{word} является палиндромом")
else:
    print(f"{word} не является палиндромом")