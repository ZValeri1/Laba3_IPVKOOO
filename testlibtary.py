
import numpy as np


class LibraryFunction:

    # Фибоначчи
    def method_fibonacci(self, n):
        # Проверка на длину последовательности
        if n <= 0:
            raise Exception("Длина последовательности не может быть меньше или равно 0")
        if isinstance(n, str):
            raise TypeError("Тип данных должен быть числовой")

        fib_sequence = np.array([])
        for x in range(1, n + 1):
            fib_sequence = np.append(fib_sequence, self.fib(x))

        return fib_sequence


    def fib(self, x):
        if x < 2:
            return 1
        return self.fib(x - 2) + self.fib(x - 1)

    # Сортировка пузырьком
    def bubble(self, numbers):
        # Проверка на тип данных в массиве
        for i in numbers:
            if isinstance(i, str):
                raise TypeError("Тип данных в массиве не может быть строкой")

        # Сортировка пузырьком
        for i in range(len(numbers) - 1):
            for j in range(len(numbers) - 1 - i):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        return numbers

    # Калькулятор
    def calculator(self, first_number, second_number, operation):
        # Проверка на тип данных
        if not (isinstance(first_number, (int, float)) and isinstance(second_number, (int, float))):
            raise TypeError("Тип данных должен быть числом")

        # Проверка на тип операции
        approve_operation = ['+', '-', '*', '/']
        if operation not in approve_operation:
            raise ValueError("Разрешены только операции '+', '-', '*', '/'")

        # Выполнение математической операции
        if operation == '+':
            return first_number + second_number
        if operation == '-':
            return first_number - second_number
        if operation == '*':
            return first_number * second_number
        if operation == '/':
            if second_number == 0:
                raise ValueError("Деление на ноль недопустимо")
            return first_number / second_number