import random
number = int(input("Введите длину массива: "))
X = int(input("Введите число: "))
index = 0
list = []
for i in range(1, number + 1):
    i = random.randint(1, number)
    list.append(i)
print(list)
min = abs(X - list[0])
for j in range(1, number):
    count = abs( - list[j])
    if count < min:
        min = count
        index = j
print(f"Число {list[index]} - самое близкое по величине к числу {X}")