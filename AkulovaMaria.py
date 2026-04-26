import math

def rectangle_area(a, b):
    if a <= 0 or b <= 0:
        return "Ошибка: стороны должны быть положительными"
    return a * b

def rectangle_perimeter(a, b):
    if a <= 0 or b <= 0:
        return "Ошибка: стороны должны быть положительными"
    return 2 * (a + b)

def rectangle_diagonal(a, b):
    return math.sqrt(a**2 + b**2)

def circle_area():
    print("1. Через радиус")
    print("2. Через диаметр")
    sub = input("Выбери: ")
    if sub == "1":
        r = float(input("Введите радиус: "))
        if r <= 0:
            print("Ошибка: радиус должен быть положительным")
            return
    if sub == "2":
        d = float(input("Введите диаметр: "))
        if d <= 0:
            print("Ошибка: диаметр должен быть положительным")
            return
        r = d / 2
    result = math.pi * r * r
    return result

def triangle_area(base, height):
    if base <= 0 or height <= 0:
        print("Ошибка: основание и высота должны быть положительными")
        return
    return 0.5 * base * height

TITLE = "=== КАЛЬКУЛЯТОР ПЛОЩАДЕЙ [прямоугольник] ==="
EXIT_MSG = "До свидания! (rect)"

while True:
    print(f"\n{TITLE}")
    print("1. Площадь прямоугольника")
    print("2. Площадь круга")
    print("3. Площадь треугольника")
    print("0. Выход")
    choice = input("Выбери пункт: ")
    if choice == "0":
        print(EXIT_MSG)
        break
    elif choice == "1":
        a = float(input("Введите длину: "))
        b = float(input("Введите ширину: "))
        print(f"Площадь прямоугольника: S = {a} * {b} = {rectangle_area(a, b)}")
        print(f"Периметр прямоугольника: P = {rectangle_perimeter(a, b)}")
        print(f"Диагональ прямоугольника: d = {rectangle_diagonal(a, b):.4f}")
    elif choice == "2":
        print(f"Площадь круга: {circle_area()}")
    elif choice == "3":
        base = float(input("Введите основание: "))
        height = float(input("Введите высоту: "))
        print(f"Площадь треугольника: {triangle_area(base, height)}")
    else:
        print("Неверный ввод!")