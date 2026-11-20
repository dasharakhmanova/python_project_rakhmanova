# Описать функцию RectPS(x1, y1, x2, y2, P, S), вычисляющую периметр P
# и площадь S прямоугольника со сторонами, параллельными осям координат,
# по координатам (x1, y1), (x2, y2) его противоположных вершин
# (x1, y1, x2, y2 — входные, P и S — выходные параметры вещественного
# типа). С помощью этой функции найти периметры и площади трех
# прямоугольников с данными противоположными вершинами.
def input_float(text):
    k = input(text)
    while type(k) != float:
        try:
            k = float(k)
        except ValueError:
            print("Неправильно ввели!")
            k = input(text)
    return k


def rect_ps(x1, y1, x2, y2):
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    p = 2 * (a + b)
    s = a * b
    return p, s


i = 1
while i <= 3:
    print("Прямоугольник", i)
    x1 = input_float("Введите x1: ")
    y1 = input_float("Введите y1: ")
    x2 = input_float("Введите x2: ")
    y2 = input_float("Введите y2: ")
    p, s = rect_ps(x1, y1, x2, y2)
    print("Периметр:", p)
    print("Площадь:", s)
    i += 1