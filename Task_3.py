'''
Задайте последовательность чисел. Напишите программу, которая выведет
 список неповторяющихся элементов исходной последовательности.
'''

nums = int(input('Задайте количество элементов:\t'))

list_input = []
for i in range(nums):
    elem = int(input("Задайте значение:  "))
    list_input.append(elem)

list_output = list(set(list_input))
list_output.sort()
print(f"{list_input} => {list_output}")