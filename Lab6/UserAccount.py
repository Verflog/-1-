class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password #создаем приватный атрибут

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password

user = UserAccount("Petrov Petr", "PetrovPetr@gmail.com", "12345")
user.set_password("54321")
is_correct = user.check_password("12345")
print(is_correct)
is_correct = user.check_password("12345")
print(is_correct)