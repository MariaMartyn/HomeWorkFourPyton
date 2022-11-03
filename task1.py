# Задача 1. Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.

def simpleArray():
    number = int(input('Введите число N: '))
    i = 2
    list = []
    while number > 1:
        if number % i == 0:
            list.append(i)
            number = number/i
        else:
            i = i+1
    print(list)
    return list

simpleArray()