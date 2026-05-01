dim1  = int(input("Введите размер первого списка:"))
dim2  = int(input("Введите размер второго списка:"))
list1 = []
list2 = []
for i in range(dim1):
    list1.append(int(input("Введите число для 1 списка:")))
for i in range(dim2):
    list2.append(int(input("Введите число для 2 списка:")))
#list1 = [1, 3, 5, 7, 9]
#list2 = [2, 4, 5, 6, 8, 10]
def merge_sorted_lists(list1, list2):
    combined = list1 + list2
    result = sorted(list(set(combined)))
    return result

merged = merge_sorted_lists(list1, list2)
print(merged)