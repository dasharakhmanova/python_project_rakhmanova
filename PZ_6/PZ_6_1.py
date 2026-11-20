# Дан список ненулевых целых чисел размера N. Проверить, образуют ли его
# элементы геометрическую прогрессию. Если образуют, то вывести
# знаменатель прогрессии, если нет — вывести 0.
n = input("Введите размер списка N: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите размер списка N: ")
    else:
        if n < 2:
            print("N должно быть не меньше 2!")
            n = input("Введите размер списка N: ")

a = []
i = 1
while i <= n:
    x = input("Введите элемент " + str(i) + ": ")
    while type(x) != int:
        try:
            x = int(x)
        except ValueError:
            print("Неправильно ввели!")
            x = input("Введите элемент " + str(i) + ": ")
        else:
            if x == 0:
                print("Элемент не должен быть нулевым!")
                x = input("Введите элемент " + str(i) + ": ")
    a.append(x)
    i += 1

print("Исходный список:", a)

q = a[1] / a[0]
ok = True
i = 1
while i < n:
    if a[i] / a[i - 1] != q:
        ok = False
    i += 1

if ok:
    if q == int(q):
        q = int(q)
    print("Знаменатель прогрессии:", q)
else:
    print(0)