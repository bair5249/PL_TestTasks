"""

0 - точка лежит на окружности

1 - точка внутри

2 - точка снаружи.
"""


from math import sqrt


with open("circle.txt", "r") as f:
    strings_circle = f.readlines()

    for i, iword in enumerate(strings_circle):
        if iword[-1] == "\n":
            strings_circle[i] = iword[:-1]

with open("dot.txt", "r") as f:
    strings_dots = f.readlines()

    for i, iword in enumerate(strings_dots):
        if iword[-1] == "\n":
            strings_dots[i] = iword[:-1]


"""
Задачу буду решать построив прямоугольные труегольники и теорему Пифагора c^2 = a^2 + b^2
"""


"Координаты центра окружности, а также точка нашего треугольника: "
x_and_y = strings_circle[0].split()
x_circle = float(x_and_y[0])
y_circle = float(x_and_y[1])

"Радиус окружности: "
radius = float(strings_circle[1])


for i in strings_dots:
    a = 0  # Длина 1 стороны треугольника
    b = 0  # Длина 2 стороны треугольника
    line = i.split()
    x_dot = float(line[0])
    y_dot = float(line[1])

    a = x_dot - x_circle
    b = y_dot - y_circle

    c = sqrt(a*a + b*b)

    if c > radius:
        print(2)
    elif c == radius:
        print(0)
    else:
        print(1)
