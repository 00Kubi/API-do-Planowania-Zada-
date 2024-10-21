from datetime import datetime, timedelta

class Task:
    def __init__(self, task_id, title, description, dependencies=None, interval=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.dependencies = dependencies if dependencies else []
        self.interval = interval  # Czas powtarzania (np. 'daily', 'weekly')
        self.created_at = datetime.now()
    
    def is_due(self):
        if self.interval == 'daily':
            return self.created_at + timedelta(days=1) <= datetime.now()
        elif self.interval == 'weekly':
            return self.created_at + timedelta(weeks=1) <= datetime.now()
        return False
