import pytest
from RefactorCode import factorial, is_prime  # Замініть 'my_module' на назву вашого файлу

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (10, 3628800),
])
def test_factorial(n, expected):
    """Тести для factorial()"""
    assert factorial(n) == expected

def test_factorial_negative():
    """Перевірка, що факторіал від'ємного числа викликає ValueError"""
    with pytest.raises(ValueError):
        factorial(-1)

@pytest.mark.parametrize("n, expected", [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (9, False),
    (11, True),
    (25, False),
    (29, True),
])
def test_is_prime(n, expected):
    """Тести для is_prime()"""
    assert is_prime(n) == expected
