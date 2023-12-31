import pytest
from contextlib import nullcontext as does_not_raise

from testlibtary import LibraryFunction


class TestLibraryFunction:

    # Функция, тестирующая метод fibonacci
    @pytest.mark.parametrize(
        "n, array_fib, expectation",
        [
            (10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55], does_not_raise()),
            (0, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55], pytest.raises(Exception)),
            (-5, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55], pytest.raises(Exception)),
            ("ad", [1, 1, 2, 3, 5, 8, 13, 21, 34, 55], pytest.raises(TypeError))
        ]
    )
    def test_fibonacci(self, n, array_fib, expectation):
        with expectation:
            assert (LibraryFunction().method_fibonacci(n), array_fib)

    # Функция, тестирующая метод bubble
    @pytest.mark.parametrize(
        "array, sorted_array, expectation",
        [
            ([1, 0, 6, 12, 9, 14, 93, 54, 21, 8], [0, 1, 6, 8, 9, 12, 14, 21, 54, 93], does_not_raise()),
            (["z", "gg", "tt", "bb", "gh", "agg"], [1, 2, 3, 4, 5], pytest.raises(TypeError))
        ]
    )
    def test_bubble(self, array, sorted_array, expectation):
        with expectation:
            assert LibraryFunction().bubble(array) == sorted_array

    # Функция, тестирующая метод calculator
    @pytest.mark.parametrize(
        "first_number, second_number, operation, result, expectation",
        [
            (100, 10, '+', 110, does_not_raise()),
            (100, 50, '-', 50, does_not_raise()),
            (50, 6, '*', 300, does_not_raise()),
            (10, 2, '/', 5, does_not_raise()),
            ("z", 2, '/', 5, pytest.raises(TypeError)),
            (1, "g", '+', 100, pytest.raises(TypeError)),
            (10, 5, 'o', 5, pytest.raises(ValueError))
        ]
    )
    def test_calculator(self, first_number, second_number, operation, result, expectation):
        with expectation:
            assert LibraryFunction().calculator(first_number, second_number, operation) == result