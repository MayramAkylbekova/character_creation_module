from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')


def calculate_square_root(Number1: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(Number1)


def Calcul(your_number: float) -> float:
    """Вывод сообщения."""
    root: float = 0.0
    if your_number <= root:
        return
    else:
        result: float = calculate_square_root(your_number)
        return print('Мы вычислили квадратный корень из введённого '
                     f'вами числа. Это будет: {result}')


print(message)
Calcul(25.5)