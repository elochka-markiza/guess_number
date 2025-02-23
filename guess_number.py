def find_max_odd_number(iterable_numbers):
    """
    Ищет максимальное чётное значение в списке положительных целых значений.
    Переданном в параметр функции.
    """
    current_max = 0
    for iterable_number in iterable_numbers:
        if iterable_number % 2 == 0:
            current_max = max(iterable_number, current_max)
    return current_max


max_odd = find_max_odd_number([1, 2, 3, 4, 5])
# Попробуйте передать в find_max_odd_number() другие списки:
"""[10, 8, 6, 4, 2]"""
"""[2, 12, 85, 0, 6]"""
print(f'Максимальное чётное число: {max_odd}')
