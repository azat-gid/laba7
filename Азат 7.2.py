import random
import math
import turtle as tr


def main():
    # 1. Настройка графического окна
    tr.setup(width=800, height=800)
    tr.title("Метод Монте-Карло: Заштрихованная фигура")
    tr.bgcolor("white")

    # Задаем радиус R
    R = 15.0

    # Устанавливаем мировую систему координат
    # Оставляем место для осей и подписей
    margin = 5
    tr.setworldcoordinates(-R - margin, -R - margin, R + margin, R + margin)

    # Настройки "черепашки"
    tr.speed(0)  # Максимальная скорость
    tr.ht()  # Скрываем черепашку
    tr.penup()

    # 2. Рисуем оси координат
    tr.pencolor("black")
    tr.pensize(2)

    # Ось X
    tr.goto(-R - 2, 0)
    tr.pendown()
    tr.goto(R + 2, 0)
    tr.penup()
    tr.goto(R + 2.5, 0)
    tr.write("X", font=("Arial", 12, "bold"))

    # Ось Y
    tr.goto(0, -R - 2)
    tr.pendown()
    tr.goto(0, R + 2)
    tr.penup()
    tr.goto(0, R + 2.5)
    tr.write("Y", font=("Arial", 12, "bold"))

    # 3. Рисуем контуры фигуры (для наглядности)
    tr.pencolor("black")
    tr.pensize(2)

    # Контур квадрата
    tr.goto(-R, -R)
    tr.pendown()
    tr.goto(R, -R)
    tr.goto(R, R)
    tr.goto(-R, R)
    tr.goto(-R, -R)
    tr.penup()

    # Контур левой верхней окружности (пунктиром)
    tr.pencolor("gray")
    tr.pensize(1)
    tr.goto(-R, R - R)  # Начало в точке касания (центр окружности (-R, R), нижняя точка (-R, 0))
    tr.setheading(270)  # Смотрим вниз
    tr.pendown()
    tr.circle(R)  # Рисуем полную окружность
    tr.penup()

    # Контур правой нижней окружности (пунктиром)
    tr.goto(R, -R + R)  # Начало в точке касания (центр окружности (R, -R), верхняя точка (R, 0))
    tr.setheading(90)  # Смотрим вверх
    tr.pendown()
    tr.circle(R)  # Рисуем полную окружность
    tr.penup()

    # 4. Метод Монте-Карло
    shots_count = 20000  # Количество испытаний (чем больше, тем четче картинка)
    hits = 0

    # Настройка точек
    tr.shape("circle")
    tr.shapesize(0.15)  # Маленькие точки

    for i in range(shots_count):
        # Генерируем случайные координаты в квадрате [-R, R]
        x = random.uniform(-R, R)
        y = random.uniform(-R, R)

        # Проверка условий:
        # 1. Точка внутри левой верхней окружности с центром (-R, R)
        in_circle1 = (x + R) ** 2 + (y - R) ** 2 <= R ** 2

        # 2. Точка внутри правой нижней окружности с центром (R, -R)
        in_circle2 = (x - R) ** 2 + (y + R) ** 2 <= R ** 2

        # Точка попадает в заштрихованную область, если она в любой из этих окружностей
        # (Внутри квадрата они не пересекаются, поэтому условие ИЛИ работает корректно)
        is_hit = in_circle1 or in_circle2

        tr.goto(x, y)
        if is_hit:
            # Заштрихованная область - темно-серый
            tr.color("dimgray")
            tr.stamp()
            hits += 1
        else:
            # Фон - светло-серый
            tr.color("lightgray")
            tr.stamp()

    # 5. Вывод результатов
    # Площадь квадрата (выборочного пространства)
    S_square = (2 * R) ** 2

    # Оценка площади Монте-Карло
    S_mc = S_square * (hits / shots_count)

    # Реальная площадь (две четверти круга, так как они не пересекаются внутри квадрата)
    S_real = (math.pi * R ** 2) / 2

    # Погрешность
    error_percent = abs(S_real - S_mc) / S_real * 100

    # Вывод текста на экран (сверху)
    tr.goto(-R - 2, R + 4)
    tr.pencolor("black")
    tr.write(f"Выстрелов: {shots_count}", font=("Arial", 10, "bold"))

    tr.goto(-R - 2, R + 2.5)
    tr.write(f"Попаданий: {hits}", font=("Arial", 10, "bold"))

    tr.goto(-R - 2, R + 1)
    tr.pencolor("darkgreen")
    tr.write(f"S (MC): {S_mc:.2f}", font=("Arial", 10, "bold"))

    tr.goto(-R - 2, R - 0.5)
    tr.pencolor("blue")
    tr.write(f"S (Точная): {S_real:.2f}", font=("Arial", 10, "bold"))

    tr.goto(-R - 2, R - 2)
    tr.pencolor("red")
    tr.write(f"Погрешность: {error_percent:.2f}%", font=("Arial", 10, "bold"))

    # Вывод в консоль
    print("--- Метод Монте-Карло для заштрихованной фигуры ---")
    print(f"Радиус R = {R}")
    print(f"Всего точек: {shots_count}")
    print(f"Попаданий: {hits}")
    print(f"Площадь (Монте-Карло): {S_mc:.4f}")
    print(f"Точная площадь (полукруг): {S_real:.4f}")
    print(f"Погрешность: {error_percent:.2f}%")

    tr.done()


if __name__ == "__main__":
    main()
