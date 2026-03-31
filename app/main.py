# app/main.py
print("App started")
from app.tasks import add_task, list_tasks

add_task("Learn Python")
print(list_tasks())
