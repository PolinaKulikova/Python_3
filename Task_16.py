import random
number = int(input("Введите длину массива: "))
N = int(input("Введите натуральное число: "))
index = 0
list = []
for i in range(1, number+1):
    i = random.randint(1, number)
    list.append(i)
print(list)
for j in range(len(list)):
    if N == list[j]:
        index += 1
print(f"Количество числа {N} в массиве - {index}")