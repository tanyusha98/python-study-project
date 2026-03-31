# app/main.py
print("App started")
from app.tasks import add_task, list_tasks

add_task("Learn Python")
print(list_tasks())
from app.weather import get_weather

print(get_weather("Berlin"))
def run():
    print("Application running")

if __name__ == "__main__":
    run()
