class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        pass

    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.emp_id}"


class Manager(Employee):
    def __init__(self, name, emp_id, department, *args):
        super().__init__(name, emp_id, *args)
        self.department = department

    def manage_project(self, project_name):
        return f"Менеджер {self.name} управляет проектом: {project_name}"


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Техник {self.name} выполняет техническое обслуживание в области {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department=None, specialization=None, *args):
        super().__init__(name, emp_id, department, specialization)
        
    def get_tech_manager_info(self):
        return f"{self.get_info()}, Отдел: {self.department}, Специализация: {self.specialization}"


# Пример использования:
tech_manager = TechManager("Алексей", 101, "ИТ", "Сеть")
print(tech_manager.get_tech_manager_info())
print(tech_manager.manage_project("Проект X"))
print(tech_manager.perform_maintenance())
