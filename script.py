# Базовый класс
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издает звук."

    def info(self):
        return f"Это животное: {self.name}"

# Производный класс
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Вызов конструктора базового класса
        self.breed = breed

    # Переопределяем метод speak
    def speak(self):
        return f"{self.name} лает."

    # Добавляем новый метод
    def info(self):
        return f"Это собака породы {self.breed}, её зовут {self.name}."

# Тестовая программа
def test_classes():
    # Создание экземпляра базового класса
    animal = Animal("Животное")
    print(animal.speak())  # Используем метод базового класса
    print(animal.info())   # Используем метод базового класса

    print()

    # Создание экземпляра производного класса
    dog = Dog("Бобик", "Овчарка")
    print(dog.speak())  # Используем переопределенный метод производного класса
    print(dog.info())   # Используем новый метод производного класса

# Запуск тестовой программы
test_classes()
