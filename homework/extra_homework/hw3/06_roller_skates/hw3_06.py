amount = int(input("Кол-во коньков: "))
list1 = [int(input(f"Размер {x}-й пары: ")) for x in range(1, amount + 1)]
amount2 = int(input("Кол-во людей: "))
list2 = [int(input(f"Размер ноги {x}-го человека: ")) for x in range(1, amount2 + 1)]
k = 0
list1.sort()
list2.sort()
for item in list2:
    if item in list1:
        k += 1
        list1.remove(item)
print(f"Наибольшее кол-во людей, которые могут взять ролики: {k}")
