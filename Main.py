class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False


class TaskManager:
    def __init__(self):
        self.tasks = []


    def add_task(self, task):
        self.tasks.append(task)
        print("Завдання додано!")


    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print("Завдання видалено!")
                return
        print("Завдання не знайдено!")


    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                print("Завдання виконано!")
                return
        print("Завдання не знайдено!")


    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній!")
            return

        for task in self.tasks:
            status = "Виконано" if task.completed else "Не виконано"
            print(f"""
Назва: {task.title}
Опис: {task.description}
Дедлайн: {task.deadline}
Стан: {status}
-------------------------
""")


manager = TaskManager()

task1 = Task("Навчання", "Вивчити Python", "25.11.2026")
task2 = Task("Домашнє завдання", "Виконати вправи", "26.11.2026")

manager.add_task(task1)
manager.add_task(task2)

manager.complete_task("Навчання")

manager.show_tasks()

manager.delete_task("Домашнє завдання")