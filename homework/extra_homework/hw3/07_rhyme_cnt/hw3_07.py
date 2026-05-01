list = []
for i in range(1, int(input("Кол-во человек: ")) + 1):
    list.append(i)
number = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {number}-й человек")
start = 0
while len(list) > 1:
   print(f"Текущий круг людей: {list}")
   print(f"Начало счёта с номера {list[start]}")
   new_start = (start + number - 1) % len(list)

   print(f"Выбывает человек под номером {list[new_start]}")
   list.pop(new_start)
   start = new_start % len(list)

print(f"Остался человек под номером {list[0]}")



