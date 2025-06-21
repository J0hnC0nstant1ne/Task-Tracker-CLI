import json
from task_tracker.task import Task


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, description, priority=1):
        task = Task(description, priority)
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self, show_all=False):
        for i, task in enumerate(self.tasks, 1):
            if show_all or not task.done:
                status = "✅" if task.done else "❌"
                print(f"{i}. {status} {task.description} (Priority: {task.priority})")

    def mark_done(self, index):
        try:
            self.tasks[index - 1].mark_done()
            self.save_tasks()
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, index):
        try:
            self.tasks.pop(index - 1)
            self.save_tasks()
        except IndexError:
            print("Invalid task number.")

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            self.tasks = []
