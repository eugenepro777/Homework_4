'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''
number = int(input('Введите натуральное число: ' + " "*3))
number_original = number

simple_minimum = 2
list_out = []
while number > 1:
    if number % simple_minimum == 0:        
        list_out.append(simple_minimum)
        number = number / simple_minimum
    else:
        simple_minimum += 1

print(f"Разложение на простые множители числа {number_original} => {list_out}")
list_simple = list(set(list_out))
list_simple.sort()
print(f"Простые множители числа {number_original} => {list_simple}")