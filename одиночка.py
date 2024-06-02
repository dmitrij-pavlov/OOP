class GameSettings:
    _instance = None  # Приватный атрибут для хранения единственного экземпляра

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameSettings, cls).__new__(cls)
            cls._instance.volume = 50  # Настройки по умолчанию
            cls._instance.difficulty = "Medium"  # Настройки по умолчанию
        return cls._instance

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = GameSettings()
        return cls._instance
