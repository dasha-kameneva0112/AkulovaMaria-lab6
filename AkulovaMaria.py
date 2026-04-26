import math

def rectangle_area(a, b):
    if a <= 0 or b <= 0:
        return "Ошибка: стороны должны быть положительными"
    return a * b

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

def circle_perimeter():
    r = float(input("Введите радиус: "))
    if r <= 0:
        print("Ошибка: радиус должен быть положительным")
        return
    return 2 * math.pi * r

def circle_sector_area():
    r = float(input("Введите радиус: "))
    angle = float(input("Введите угол (градусы): "))
    if r <= 0 or angle <= 0:
        print("Ошибка: значения должны быть положительными")
        return
    return 0.5 * r**2 * math.radians(angle)

def triangle_area(base, height):
    if base <= 0 or height <= 0:
        print("Ошибка: основание и высота должны быть положительными")
        return
    return 0.5 * base * height

def triangle_area_heron(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print("Ошибка: стороны должны быть положительными")
        return
    if a + b <= c or a + c <= b or b + c <= a:
        print("Ошибка: такой треугольник не существует")
        return
    s = (a + b + c) / 2
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

TITLE = "=== КАЛЬКУЛЯТОР ПЛОЩАДЕЙ [круг] ==="

# КОНФЛИКТ 3: переменная EXIT_MSG
# Ветки: feature-rectangle vs feature-triangle
# ПРИОРИТЕТ: feature-triangle — взять эту версию
EXIT_MSG = "Спасибо за использование! До свидания! (tri)"

# КОНФЛИКТ 2: функция вывода результата
# Ветки: feature-circle vs feature-triangle
# СОХРАНИТЬ ОБА — объединить строки из обеих веток
def print_result(label, value):
    if value is not None:
        print(f">>> {label}: {value:.4f} <<<")

while True:
    print(f"\n{TITLE}")
    print("1. Площадь прямоугольника")
    print("2. Площадь круга")
    print("3. Площадь треугольника (осн. и высота)")
    print("4. Площадь треугольника (по трём сторонам)")
    print("0. Выход")
    choice = input("Выбери пункт: ")
    if choice == "0":
        print(EXIT_MSG)
        break
    elif choice == "1":
        a = float(input("Введите длину: "))
        b = float(input("Введите ширину: "))
        print(f"Площадь прямоугольника: S = {a} * {b} = {rectangle_area(a, b)}")
    elif choice == "2":
        print_result("Площадь круга", circle_area())
        print_result("Длина окружности", circle_perimeter())
    elif choice == "3":
        base = float(input("Введите основание: "))
        height = float(input("Введите высоту: "))
        print_result("Площадь треугольника", triangle_area(base, height))
    elif choice == "4":
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        c = float(input("Сторона c: "))
        print_result("Площадь треугольника (Герон)", triangle_area_heron(a, b, c))
    else:
        print("Неверный ввод!")