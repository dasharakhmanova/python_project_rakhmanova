#Даны целые числа A и B (A<B). Вывести все целые числа от A до B включительно; при этом число A должно выводиться 1 раз, число A+1 должно выводиться 2 раза и т.д.
try:
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
except ValueError:
    print("Неправильно ввели! Нужны целые числа.")
else:
    if a < b:
        for i in range(a, b + 1):
            for _ in range(i - a + 1):
                print(i)
    else:
        print("Должно быть A < B!")