# app/tasks.py
tasks = []
def add_task(task):
    tasks.append({"task": task, "done": False})
def list_tasks():
    return tasks
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
