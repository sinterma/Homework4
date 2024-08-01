import math
import random


def test_greeting():
    # Вывести приветствие на экран
    # Дано:
    name = "Анна"
    age = 25

    # Код
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    # Высчитываем периметр и площадь прямоугольника
    # Дано:
    a = 10
    b = 20

    # Код
    perimeter = a * 2 + b * 2

    # Проверяем результат
    assert perimeter == 60

    # Код
    area = a * b

    # Проверяем результат
    assert area == 200


def test_circle():
    # Высчитываем длину и площадь круга
    # Дано:
    r = 23

    # Код
    area = math.pi * r ** 2

    # Проверяем результат
    assert area == 1661.9025137490005

    # Код
    length = 2 * math.pi * r

    # Проверяем результат
    assert length == 144.51326206513048


def test_random_list():
    # Создаем список из 10 случайных чисел от 1 до 100, и сортируем в порядке возрастания
    # Код:
    l = []

    # Выполняем цикл 10 раз
    for _ in range(10):
        # Добавляем случайное число от 1 до 100 в список
        l.append(random.randint(1, 100))

    # Сортируем
    l.sort()

    # Проверяем результат
    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements():
    # Удаляем из писка повторяющиеся элементы
    # Дано:
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    # Код
    l = list(set(l))

    # Проверяем результат
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    # Создаем словарь из двух списков
    # Дано:
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    # Создаем словарь при помощи zip
    d = dict(zip(first, second))

    # Проверяем результат
    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second
