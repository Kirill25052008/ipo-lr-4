#Темник Кирилл
import math

number = int(input("Введите число "))
i = 0
j = 1

while i < number:
    print (i)
    i, j = j, i + j
