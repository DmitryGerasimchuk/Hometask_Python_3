# Задача № 23 (была не решена на семинаре):
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива, больших предыдущего
# (элемента с предыдущим номером)
#
# Проверка:
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
#
# Примечание:
# Пользователь может вводить значения списка или список задан изначально.
# Для моего решения принимаем, что список задан изначально

# Решение:
list_1 = [0, -1, 5, 2, 3]
print(list_1)
count = 0
for i in range(len(list_1)):
    if list_1[i] > list_1[i-1]:
        count = count + 1
print("Количество элементов массива, больших предыдущего, для заданного массива равно", count)