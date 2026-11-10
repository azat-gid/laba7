import math
import turtle as tr


def taylor_exp(x, eps):
    """
    Вычисляет e^x с помощью ряда Тейлора.
    Возвращает сумму ряда и количество итераций n.
    """
    n = 0
    current_term = 1.0  # Первый член ряда (n=0)
    sum_y = 0.0

    while abs(current_term) > eps:
        sum_y += current_term
        n += 1
        current_term *= x / n  # Рекуррентная формула для e^x

    return sum_y, n


def draw_axes(x_min, x_max, y_min, y_max):
    """Рисует оси координат, деления и подписи"""
    tr.pencolor("black")
    tr.pensize(2)

    # Ось X
    tr.penup()
    tr.goto(x_min, 0)
    tr.pendown()
    tr.goto(x_max, 0)
    tr.stamp()

    # Ось Y
    tr.penup()
    tr.goto(0, y_min)
    tr.pendown()
    tr.goto(0, y_max)
    tr.stamp()

    # Деления по оси X
    tr.pensize(1)
    tr.penup()
    for i in range(int(x_min), int(x_max) + 1):
        if i == 0: continue
        tr.goto(i, 0)
        tr.pendown()
        tr.goto(i, y_max * 0.02)
        tr.penup()
        tr.goto(i, y_max * 0.04)
        tr.write(str(i), align="center", font=("Arial", 9, "normal"))

    # Деления по оси Y
    for i in range(int(y_min), int(y_max) + 1):
        if i == 0 or i % 2 != 0: continue  # Деления через 2 для красоты
        tr.goto(0, i)
        tr.pendown()
        tr.goto(x_max * 0.02, i)
        tr.penup()
        tr.goto(x_max * 0.03, i - 0.2)
        tr.write(str(i), align="left", font=("Arial", 9, "normal"))


def main():
    # --- Параметры расчета (вместо input) ---
    x_start = -2.0
    x_end = 2.0
    dx = 0.5
    eps = 0.0001

    # 1. Настройка графического окна
    tr.setup(width=900, height=700)
    tr.title("Лабораторная №7. Задание 3: Ряд Тейлора для e^x")
    tr.bgcolor("white")

    # Определяем границы для графика
    # По Y берем от минимума e^(-2) до e^2 + запас
    y_min = math.exp(x_start) - 1
    y_max = math.exp(x_end) + 2

    # Устанавливаем мировую систему координат
    tr.setworldcoordinates(x_start - 1, y_min, x_end + 1, y_max)

    # Настройки черепашки
    tr.speed(0)
    tr.ht()
    tr.shape("arrow")
    tr.shapesize(0.5)
    tr.penup()

    # 2. Рисуем оси координат
    draw_axes(x_start - 1, x_end + 1, y_min, y_max)

    # 3. Рисуем ТОЧНУЮ функцию e^x (гладкая синяя линия)
    tr.pencolor("blue")
    tr.pensize(2)
    tr.penup()

    x_plot = x_start - 0.5
    tr.goto(x_plot, math.exp(x_plot))
    tr.pendown()

    while x_plot <= x_end + 0.5:
        tr.goto(x_plot, math.exp(x_plot))
        x_plot += 0.05  # Мелкий шаг для плавности

    # 4. Рисуем точки, вычисленные Рядом Тейлора
    tr.penup()
    tr.shape("circle")
    tr.shapesize(0.6)

    x = x_start
    while x <= x_end + 0.0001:
        # Считаем ряд
        sum_y, n = taylor_exp(x, eps)

        # Ставим красную точку
        tr.goto(x, sum_y)
        tr.pencolor("red")
        tr.stamp()

        # Подписываем количество итераций (N) под точкой
        tr.goto(x, sum_y - (y_max - y_min) * 0.07)
        tr.pencolor("darkred")
        tr.write(f"N={n}", align="center", font=("Arial", 9, "bold"))

        # Подписываем X на оси
        tr.goto(x, -0.5)
        tr.pencolor("black")
        tr.write(f"{x:.1f}", align="center", font=("Arial", 9, "normal"))

        x += dx

    # 5. Легенда и заголовок
    tr.penup()
    tr.goto(x_start - 0.5, y_max - 0.5)
    tr.pencolor("black")
    tr.write("Ряд Тейлора для e^x", font=("Arial", 14, "bold"))

    tr.goto(x_start - 0.5, y_max - 1.5)
    tr.pencolor("blue")
    tr.write("Точная функция y = e^x", font=("Arial", 12, "normal"))

    tr.goto(x_start - 0.5, y_max - 2.5)
    tr.pencolor("red")
    tr.write("Точки: сумма ряда Тейлора", font=("Arial", 12, "normal"))

    tr.goto(x_start - 0.5, y_max - 3.5)
    tr.pencolor("black")
    tr.write(f"Параметры: x ∈ [{x_start}, {x_end}], dx = {dx}, ε = {eps}", font=("Arial", 11, "normal"))

    # Дублируем результаты в консоль
    print("=" * 60)
    print("Лабораторная №7. Задание 3: Визуализация ряда Тейлора")
    print("=" * 60)
    print(f"| {'X':^7} | {'Ряд Тейлора':^16} | {'Точное':^16} | {'N':^4} |")
    print("-" * 60)
    x = x_start
    while x <= x_end + 0.0001:
        sum_y, n = taylor_exp(x, eps)
        true_y = math.exp(x)
        print(f"| {x:7.2f} | {sum_y:16.6f} | {true_y:16.6f} | {n:4d} |")
        x += dx

    tr.done()


if __name__ == "__main__":
    main()