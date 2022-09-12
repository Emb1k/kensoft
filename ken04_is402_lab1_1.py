def main():
    a = int(input('Введите A: '))
    b = int(input('Введите B: '))
    x = int(input('Введите X: '))
    if x >= 4:
        y = (a * a) + (5 * x) + (b * b) / (a * b)
    else:
        y = x * (a - b)
    print("y = %.1f" % y)
    input("Нажмите Enter для выхода")

if __name__ == '__main__':
    main()
