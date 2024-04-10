class Button:
    def __init__(self):
        self.clicks = 0

    def click(self):
        self.clicks += 1

    def click_count(self):
        return self.clicks

    def reset(self):
        self.clicks = 0

# Пример использования
btn = Button()
btn.click()  # Увеличиваем количество нажатий на 1
btn.click()  # Увеличиваем количество нажатий на 1
print(btn.click_count())  # Выведет 2
btn.reset()  # Обнуляем количество нажатий
print(btn.click_count())  # Выведет 0
