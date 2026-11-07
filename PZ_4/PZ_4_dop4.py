# Найти и вывести на экран S = 1! + 2! + 3! + 4! + ... + n! (n > 1).
n = int(input("Введите n: "))
fact = 1
s = 0
for i in range(1, n + 1):
    fact *= i
    s += fact
print("S =", s)