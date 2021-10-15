 def sum(x, y):...
    s = float(x) + float(y)
    return s
x = input("Введите число 1: ")
y = input("Введите число 2: ")
print("сумма равна:", sum(x, y))
print("global premennaya")
def sub(x, y):
    global result
    result = float(x) - float(y)
result = 0
sub(x, y)
print("разность равна:", result)
print("-----MODULI")
import math as m
print(m.sin(1))
import m.ce...

