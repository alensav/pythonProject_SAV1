'''from random import random

myset = set("Python")
print(myset)

list = [int(random()* 10) for i in range(0, 10)]
print(list)
myset = set(list)
print(myset)

#СТРОКИ
mystr1 = "abc"
mystr2 = 'xyz'
print("Сложение строк", mystr1 + mystr2 )
number1 = input("Введите первое число = ",)
print("Вы ввели первое число - ", int(number1))
number2 = input("Введите второе ервое число = ",)
print("Вы ввели второе число - ", int(number2))
print("Сумма чисел = ", int(number1) + int(number2))
#Оператор IF
print("Введите 0,1 или 2 - ")
a = input()
if a == "0":
    print("Вы ввели - 0")
else:
	print("Вы ввели болше чем ноль")
i = 0
while i < 10:
     i = i + 1
     print("Helo Word")
list = []
list = ['h','e','i','l','o']
print(list)
print(list[4])
print(list[-1])
print(list[len(list) - 2 ])
print ('==================================')
i = 0
while i < len(list) :
    print(list[i])
    i += 1
myset = set("Python")
print(myset)
myset2 = {'1','2','3','1','1'}
print(myset2)
import random
list = [int(random.random() * 10)  for  i in range(0, 10)]
print(list)
myset3 = set(list)
print(myset3)'''
mydict = dict()
mydict = {'Name':'John', 'Age': 35}
print(mydict)
print(mydict["Age"])
mytuple = ('Name', 'Age', 'isMale')
print(mytuple)
for key in mytuple:
    print(key, '*', mydict[key])
