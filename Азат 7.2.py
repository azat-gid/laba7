import random
import math
import turtle as tr


def draw_dashed_circle(cx, cy, r, dashes=60):
    """Рисует пунктирную окружность с центром (cx, cy) и радиусом r."""
    tr.penup()
    for i in range(dashes):
        angle1 = 2 * math.pi * i / dashes
        angle2 = 2 * math.pi * (i + 0.5) / dashes
        tr.goto(cx + r * math.cos(angle1), cy + r * math.sin(angle1))
        tr.pendown()
        tr.goto(cx + r * math.cos(angle2), cy + r * math.sin(angle2))
        tr.penup()


def main():
    # 1. Настройка графического окна
    tr.setup(width=800, height=800)
    tr.title("Метод Монте-Карло: Заштрихованная фигура (вариант 34)")
    tr.bgcolor("white")

    # Отключаем автообновление экрана для максимальной скорости
    tr.tracer(0)

    # Задаем радиус R
    R = 15.0

    # Масштаб окна, чтобы поместились обе полные окружности [-2R, 2R]
    limit = 2 * R + 4
    tr.setworldcoordinates(-limit, -limit, limit, limit)

    tr.ht()
    tr.penup()

    # 2. Рисуем оси координат
    tr.pencolor("black")
    tr.pensize(2)

    # Ось X
    tr.goto(-2 * R - 1, 0)
    tr.pendown()
    tr.goto(2 * R + 1, 0)
    tr.penup()
    tr.goto(2 * R + 1.5, -1)
    tr.write("X", font=("Arial", 12, "bold"))

    # Ось Y
    tr.goto(0, -2 * R - 1)
    tr.pendown()
    tr.goto(0, 2 * R + 1)
    tr.penup()
    tr.goto(0.8, 2 * R + 1)
    tr.write("Y", font=("Arial", 12, "bold"))

    # 3. Метод Монте-Карло (рисуем точки до контуров, чтобы контуры были поверх)
    shots_count = 20000
    hits = 0

    for i in range(1, shots_count + 1):
        x = random.uniform(-R, R)
        y = random.uniform(-R, R)

        # Левая верхняя окружность с центром (-R, R)
        in_circle1 = (x + R) ** 2 + (y - R) ** 2 <= R ** 2

        # Правая нижняя окружность с центром (R, -R)
        in_circle2 = (x - R) ** 2 + (y + R) ** 2 <= R ** 2

        # Попадание: внутри квадрата, но ВНЕ обеих окружностей
        is_hit = not in_circle1 and not in_circle2

        tr.goto(x, y)
        if is_hit:
            tr.dot(3, "dimgray")
            hits += 1
        else:
            tr.dot(3, "lightgray")

        # Обновляем кадр каждые 1000 точек (создает плавный и быстрый эффект)
        if i % 1000 == 0:
            tr.update()

    # 4. Рисуем контуры фигуры поверх точек
    tr.pencolor("black")
    tr.pensize(2)

    # Контур квадрата [-R, R]
    tr.goto(-R, -R)
    tr.pendown()
    tr.goto(R, -R)
    tr.goto(R, R)
    tr.goto(-R, R)
    tr.goto(-R, -R)
    tr.penup()

    # Пунктирные окружности с центрами (-R, R) и (R, -R)
    tr.pencolor("gray")
    tr.pensize(1)
    draw_dashed_circle(-R, R, R)
    draw_dashed_circle(R, -R, R)

    # 5. Расчет и вывод результатов
    S_square = (2 * R) ** 2
    S_mc = S_square * (hits / shots_count)

    # Точная площадь: площадь квадрата минус две четверти круга (полукруг)
    S_real = S_square - (math.pi * R ** 2) / 2
    error_percent = abs(S_real - S_mc) / S_real * 100

    # Вывод текста в свободном правом верхнем углу
    text_x = 3
    tr.goto(text_x, 2 * R)
    tr.pencolor("black")
    tr.write(f"Выстрелов: {shots_count}", font=("Arial", 10, "bold"))

    tr.goto(text_x, 2 * R - 2)
    tr.write(f"Попаданий: {hits}", font=("Arial", 10, "bold"))

    tr.goto(text_x, 2 * R - 4)
    tr.pencolor("darkgreen")
    tr.write(f"S (MC): {S_mc:.2f}", font=("Arial", 10, "bold"))

    tr.goto(text_x, 2 * R - 6)
    tr.pencolor("blue")
    tr.write(f"S (Точная): {S_real:.2f}", font=("Arial", 10, "bold"))

    tr.goto(text_x, 2 * R - 8)
    tr.pencolor("red")
    tr.write(f"Погрешность: {error_percent:.2f}%", font=("Arial", 10, "bold"))

    # Финальное обновление экрана
    tr.update()

    print("--- Метод Монте-Карло для заштрихованной фигуры ---")
    print(f"Радиус R = {R}")
    print(f"Всего точек: {shots_count}")
    print(f"Попаданий: {hits}")
    print(f"Площадь (Монте-Карло): {S_mc:.4f}")
    print(f"Точная площадь: {S_real:.4f}")
    print(f"Погрешность: {error_percent:.2f}%")

    tr.done()


if __name__ == "__main__":
    main()
