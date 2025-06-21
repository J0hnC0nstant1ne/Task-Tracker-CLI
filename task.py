class Task:
    def __init__(self, description, priority=1):
        self.description = description
        self.priority = int(priority)
        self.done = False

    def mark_done(self):
        self.done = True

    def to_dict(self):
        return {
            "description": self.description,
            "priority": self.priority,
            "done": self.done
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["description"], data["priority"])
        task.done = data["done"]
        return task
