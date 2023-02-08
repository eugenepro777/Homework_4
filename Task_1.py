'''
Вычислить число pi c заданной точностью d
Пример:
- при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}
'''
from decimal import * 
Decimal, ROUND_FLOOR
getcontext().prec = 100


d = input('Задайте точность от 0.1 до 0.0000000001: ')
place = d.split('.')
accurate = len(place[1])
digit = "0"*len(place[1])
digit_plus = "1" + "." + digit

if accurate <= 3:
    n = 10000
else:
    n = 1000000

# ряд Нилаканта
s = Decimal(1)
pi = Decimal(3)

for i in range(2, n * 2, 2):
    pi = pi + s * (Decimal(4) / (Decimal(i) * (Decimal(i) +
                   Decimal(1)) * (Decimal(i) + Decimal(2))))
    s = -1 * s

print(f"ряд Нилаканта π = {pi.quantize(Decimal(digit_plus), ROUND_FLOOR)}\n")

# Формула Виете
var = Decimal(2).sqrt()
pi = var / Decimal(2)

for i in range(1, n):
    var = Decimal(var + 2).sqrt()
    pi *= var / Decimal(2)

pi = Decimal(2) / pi

print(f"формула Виете π = {pi.quantize(Decimal(digit_plus), ROUND_FLOOR)}\n")

# ряд Лейбница
# rang = int(1/float(d))
# denominator = 1
# total = 0
# digit = "0"*len(place[1])
# digit_plus = "1" + "." + digit

# for i in range(n):
#     if i % 2 == 0:
#         total += 4/denominator
#     else:
#         total -= 4/denominator
#     denominator += 2

# print(f"ряд Лейбница π = {round(pi, accurate)}")
