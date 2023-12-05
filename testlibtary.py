
import numpy as np


class LibraryFunction:

    # Фибоначчи
    def fibonacci(self, n):
        # Проверка на длину последовательности
        if n <= 0:
            raise Exception("Длина последовательности должна быть больше 0")
        if isinstance(n, str):
            raise TypeError("Тип данных должен быть числовой")

        fib_sequence = np.array([])
        for x in range(1, n + 1):
            fib_sequence = np.append(fib_sequence, self.fib(x))

        return fib_sequence

    # Рекуррентная функция Фибоначчи
    def fib(self, x):
        if x < 2:
            return 1
        return self.fib(x - 2) + self.fib(x - 1)

    # Сортировка пузырьком
    def bubble(self, numbers):
        # Проверка на тип данных в массиве
        for i in numbers:
            if isinstance(i, str):
                raise TypeError("Тип данных в массиве должен быть числовой")

        # Сортировка пузырьком
        for i in range(len(numbers) - 1):
            for j in range(len(numbers) - 1 - i):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        return numbers

    # Калькулятор
    def calculator(self, first_number, second_number, operation):
        # Проверка на тип данных
        if isinstance(first_number, str) or isinstance(second_number, str) == str:
            raise TypeError("Тип данных должен быть числовой")
        # Проверка на тип операции
        approve_operation = ['+', '-', '*', '/']
        count = 0
        for i in approve_operation:
            if operation.__eq__(i):
                count += 1
        if count == 0:
            raise TypeError("Разрешены только операции '+', '-', '*', '/'")

        if operation == '+':
            return first_number + second_number
        if operation == '-':
            return first_number - second_number
        if operation == '*':
            return first_number * second_number
        if operation == '/':
            return first_number / second_number