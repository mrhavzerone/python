def average():
    # Ввод чисел от пользователя
    numbers = input("Введите числа через пробел: ")

    # Разбиваем строку на список чисел
    numbers_list = numbers.split()

    # Преобразуем каждый элемент списка в число типа float
    numbers_list = [float(num) for num in numbers_list]

    # Считаем среднее арифметическое
    if len(numbers_list) > 0:
        avg = sum(numbers_list) / len(numbers_list)
        return avg
    else:
        return 0  # Если список пустой, возвращаем 0


# Пример использования функции
result = average()
print(f"Среднее арифметическое: {result}")
