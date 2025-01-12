class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

# Пример использования класса Book
book1 = Book("1984", "Джордж Оруэлл", 1949)
print(book1.get_info())

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius

# Пример использования класса Circle
circle = Circle(5)  # Создаем круг с радиусом 5
print("Начальный радиус круга:", circle.get_radius())

circle.set_radius(10)  # Изменяем радиус на 10
print("Новый радиус круга:", circle.get_radius())