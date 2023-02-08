'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
Пример
n = 11 m = 6 =>
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12

'''
sizes = input('Задайте через запятую размеры наборов n,m:' + " "*2)
resize = sizes.split(',')
n = int(resize[0])
m = int(resize[1])

first_list = []
second_list = []
for i in range(n):
    elem = input(f"введите {i + 1} элемент первого набора:\t")
    first_list.append(int(elem))
print()
for j in range(m):
    elem = input(f" введите {j + 1} элемент второго множества:\t")
    second_list.append(int(elem))
print()
print(f"Первый набор {first_list}")
print(f"Второй набор {second_list}")

first_set = set(first_list)
second_set= set(second_list)
output_set = first_set.intersection(second_set)
list_out = list(output_set)

print(sorted(list_out))
