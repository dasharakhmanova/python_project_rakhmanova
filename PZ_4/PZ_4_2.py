# Даны целые положительные числа N и K. Используя только операции
# сложения и вычитания, найти частное от деления нацело N на K,
# а также остаток от этого деления.
n = input("Введите число N: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число N: ")
    else:
        if n <= 0:
            print("N должно быть положительным!")
            n = input("Введите число N: ")

k = input("Введите число K: ")
while type(k) != int:
    try:
        k = int(k)
    except ValueError:
        print("Неправильно ввели!")
        k = input("Введите число K: ")
    else:
        if k <= 0:
            print("K должно быть положительным!")
            k = input("Введите число K: ")

print("N =", n, "K =", k)
quotient = 0
rest = n
while rest >= k:
    rest -= k
    quotient += 1
print("Частное:", quotient)
print("Остаток:", rest)