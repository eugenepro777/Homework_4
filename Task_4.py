'''
Задана натуральная степень k. Сформировать случайным 
образом список коэффициентов (значения от 0 до 100) 
многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''

from random import randint
import itertools

k = int(input('Задайте натуральную степень k: '))


def get_ratios(k):
    ratios = [randint(0, 100) for i in range(k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 100)
    return ratios


def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynom = [[a, b, c] for a, b, c in itertools.zip_longest(
        ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynom:
        x.append(' + ')
    polynom = list(itertools.chain(*polynom))
    polynom[-1] = ' = 0'
    return "".join(map(str, polynom)).replace(' 1*x', ' x').replace('1*x', '*x')


ratios = get_ratios(k)
polynom_first = get_polynomial(k, ratios)

ratios = get_ratios(k)
polynom_second = get_polynomial(k, ratios)
print(f"{polynom_first}  или  {polynom_second}")
