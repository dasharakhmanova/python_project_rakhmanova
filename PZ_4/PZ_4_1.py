# Даны целые числа A и B (A < B). Вывести все целые числа от A до B
# включительно; при этом число A должно выводиться 1 раз, число A + 1
# должно выводиться 2 раза и т. д.
a = input("Введите число A: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите число A: ")

b = input("Введите число B: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите число B: ")
    else:
        if b <= a:
            print("B должно быть больше A!")
            b = input("Введите число B: ")

print("A =", a, "B =", b)
n = a
while n <= b:
    k = 0
    while k < n - a + 1:
        print(n, end=" ")
        k += 1
    n += 1
print()