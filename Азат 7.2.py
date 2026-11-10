import random
import math
import turtle as tr


def main():
    # 1. Настройка графического окна
    tr.setup(width=800, height=800)
    tr.title("Лабораторная №7. Задание 2: Мишень №3 (Метод Монте-Карло)")
    tr.bgcolor("white")

    # Задаем радиус мишени
    R = 10.0

    # Устанавливаем мировую систему координат (с небольшим отступом)
    margin = 2
    tr.setworldcoordinates(-R - margin, -R - margin, R + margin, R + margin)

    # Настройки "черепашки"
    tr.speed(0)  # Максимальная скорость
    tr.ht()  # Скрываем черепашку
    tr.shape("circle")
    tr.shapesize(0.2)  # Делаем точки маленькими
    tr.penup()

    # 2. Рисуем оси координат и контуры мишени
    tr.pencolor("black")
    tr.pensize(2)

    # Ось X
    tr.goto(-R - 1, 0)
    tr.pendown()
    tr.goto(R + 1, 0)
    tr.stamp()

    # Ось Y
    tr.goto(0, -R - 1)
    tr.pendown()
    tr.goto(0, R + 1)
    tr.stamp()

    tr.penup()
    tr.pencolor("gray")
    tr.pensize(1)

    # Рисуем контур круга
    tr.goto(0, -R)
    tr.pendown()
    tr.circle(R)
    tr.penup()

    # Заливка (штриховка) нужных четвертей для наглядности
    # Левая верхняя четверть
    tr.goto(0, 0)
    tr.pendown()
    tr.fillcolor("lightblue")
    tr.begin_fill()
    tr.setheading(90)
    tr.circle(R, 90)  # Дуга от (0,R) до (-R,0)
    tr.goto(0, 0)
    tr.end_fill()
    tr.penup()

    # Правая нижняя четверть
    tr.goto(0, 0)
    tr.pendown()
    tr.fillcolor("lightblue")
    tr.begin_fill()
    tr.setheading(270)
    tr.circle(R, 90)  # Дуга от (0,-R) до (R,0)
    tr.goto(0, 0)
    tr.end_fill()
    tr.penup()

    # 3. Метод Монте-Карло
    shots_count = 10000  # Количество испытаний
    hits = 0

    for i in range(shots_count):
        # Генерируем координаты от -R до R
        x = random.uniform(-R, R)
        y = random.uniform(-R, R)

        is_hit = False

        # Проверяем, что точка внутри круга
        inside_circle = (x ** 2 + y ** 2) <= R ** 2

        # 1. Левая верхняя четверть
        if x <= 0 and y >= 0 and inside_circle:
            is_hit = True
        # 2. Правая нижняя четверть
        elif x >= 0 and y <= 0 and inside_circle:
            is_hit = True

        # Отрисовка точки
        tr.goto(x, y)
        if is_hit:
            tr.dot(3, "green")  # Попадание
            hits += 1
        else:
            tr.dot(2, "lightgray")  # Промах

    # 4. Вывод результатов
    # Площадь квадрата, в который "стреляем"
    S_square = (2 * R) ** 2

    # Оценка площади Монте-Карло
    S_mc = S_square * (hits / shots_count)

    # Реальная площадь (две четверти круга = половина круга)
    S_real = (math.pi * R ** 2) / 2

    # Погрешность в процентах
    error_percent = abs(S_real - S_mc) / S_real * 100

    # Вывод на экран
    tr.goto(-R, R + 1.5)
    tr.pencolor("black")
    tr.write(f"Выстрелов: {shots_count}", font=("Arial", 12, "bold"))

    tr.goto(-R, R + 0.8)
    tr.write(f"Попаданий: {hits}", font=("Arial", 12, "bold"))

    tr.goto(-R, R + 0.1)
    tr.pencolor("darkgreen")
    tr.write(f"Площадь (Монте-Карло): {S_mc:.2f}", font=("Arial", 12, "bold"))

    tr.goto(-R, R - 0.6)
    tr.pencolor("blue")
    tr.write(f"Реальная площадь: {S_real:.2f}", font=("Arial", 12, "bold"))

    tr.goto(-R, R - 1.3)
    tr.pencolor("red")
    tr.write(f"Погрешность: {error_percent:.2f}%", font=("Arial", 12, "bold"))

    # Вывод в консоль
    print("--- Лабораторная работа №3. Задание 2 (Мишень №3) ---")
    print(f"Радиус мишени R = {R}")
    print(f"Количество испытаний: {shots_count}")
    print(f"Количество попаданий: {hits}")
    print(f"Площадь (Монте-Карло): {S_mc:.4f}")
    print(f"Реальная площадь: {S_real:.4f}")
    print(f"Погрешность: {error_percent:.2f}%")

    tr.done()


if __name__ == "__main__":
    main()