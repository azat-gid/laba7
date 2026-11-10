import math
import turtle as tr


def calculate_function(x):
    """
    Вычисляет значение y для графика №3.
    (Логика полностью взята из файла import.txt)
    """
    if x < -9 or x > 5:
        return None

    # Участок 1: Дуга окружности (спуск и подъем)
    # Центр: (-7, 2), Радиус R = 2. Уравнение: y = 2 - sqrt(4 - (x+7)^2)
    elif -9 <= x <= -5:
        y = 2 - math.sqrt(4 - (x + 7) ** 2)

    # Участок 2: Горизонтальная прямая
    elif -5 < x <= -4:
        y = 2.0

    # Участок 3: Наклонная прямая (от (-4, 2) до (0, 0))
    elif -4 < x <= 0:
        y = -0.5 * x

    # Участок 4: Синусоида (от 0 до pi)
    elif 0 < x <= math.pi:
        y = math.sin(x)

    # Участок 5: Прямая под 45 градусов (от pi до 5)
    elif math.pi < x <= 5:
        y = x - math.pi

    return y


def draw_axes(x_min, x_max, y_min, y_max):
    """Рисует оси координат, деления и подписи"""
    tr.pencolor("black")
    tr.pensize(2)

    # Ось X
    tr.penup()
    tr.goto(x_min, 0)
    tr.pendown()
    tr.goto(x_max, 0)
    tr.stamp()  # Стрелка на конце оси

    # Ось Y
    tr.penup()
    tr.goto(0, y_min)
    tr.pendown()
    tr.goto(0, y_max)
    tr.stamp()

    # Деления и подписи по оси X
    tr.pensize(1)
    tr.penup()
    for i in range(int(x_min), int(x_max) + 1):
        if i == 0: continue
        tr.goto(i, 0)
        tr.pendown()
        tr.goto(i, y_max * 0.03)  # Длина деления
        tr.penup()
        tr.goto(i, y_max * 0.05)
        tr.write(str(i), align="center", font=("Arial", 10, "normal"))

    # Деления и подписи по оси Y
    for i in range(int(y_min), int(y_max) + 1):
        if i == 0: continue
        tr.goto(0, i)
        tr.pendown()
        tr.goto(x_max * 0.02, i)
        tr.penup()
        tr.goto(x_max * 0.03, i - 0.2)
        tr.write(str(i), align="left", font=("Arial", 10, "normal"))


def main():
    # 1. Настройка экрана
    tr.setup(width=900, height=600)
    tr.title("Лабораторная №7. Задание 1: График №3 (сложная функция)")
    tr.bgcolor("white")

    # Задаем границы видимой области (немного больше самих границ функции)
    x_min, x_max = -11, 7
    y_min, y_max = -3, 6

    # Устанавливаем мировую систему координат (чтобы избежать искажений)
    tr.setworldcoordinates(x_min, y_min, x_max, y_max)

    # Настройки "черепашки"
    tr.speed(0)  # Максимальная скорость
    tr.shape("arrow")
    tr.shapesize(0.7)
    tr.ht()  # Скрываем саму черепашку (нам нужен только след)

    # 2. Рисуем оси координат
    draw_axes(x_min, x_max, y_min, y_max)

    # 3. Рисуем график функции
    tr.penup()
    tr.pencolor("blue")
    tr.pensize(3)

    # Начинаем с левой границы функции
    x = -9.0
    step = 0.05  # Мелкий шаг для плавной кривой (вместо dx=0.5 из таблицы)

    # Опускаем перо в первой точке
    y = calculate_function(x)
    tr.goto(x, y)
    tr.pendown()

    # Проходим по всему диапазону
    while x <= 5.0:
        y = calculate_function(x)

        # Если функция не определена (None) - поднимаем перо
        if y is None:
            tr.penup()
        else:
            tr.goto(x, y)
            # Если перо было поднято (после разрыва), опускаем его
            if not tr.isdown():
                tr.pendown()

        x += step

    # 4. Добавляем заголовок на холст
    tr.penup()
    tr.goto(-10, 5)
    tr.pencolor("black")
    tr.write("График №3: Дуга, прямая, синусоида", font=("Arial", 14, "bold"))

    # Оставляем окно открытым до клика
    tr.done()


if __name__ == "__main__":
    main()