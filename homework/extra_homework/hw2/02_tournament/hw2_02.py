list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
def func(list):
    new_list = []
    for i in range(len(list)):
        if i % 2 == 0:
            new_list.append(list[i])
    return new_list
print(func(list))