# Создаем класс Selector
class Selector:
    # Инициализация класса, принимает список чисел
    def __init__(self, values):
        self.values = values

    # Метод для получения нечетных чисел
    def get_odds(self):
        return [num for num in self.values if num % 2 != 0]

    # Метод для получения четных чисел
    def get_evens(self):
        return [num for num in self.values if num % 2 == 0]

# Пример использования
values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))