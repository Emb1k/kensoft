import math

try:
    a = float(input("Введите A="))
    b = float(input("Введите B="))
    x = float(input("Введите X="))
    try:
        if x >= 4:
            y = (a * a) + (5 * x) + (b * b) / (a * b)
        else:
            y = x * (a - b)
        print("y = %.1f" % y)
    except:
        print("Нет решения!")
except:
    print("Неверные входные данные!")
input("Нажмите Enter для выхода")
