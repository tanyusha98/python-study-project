# app/notes.py
notes = []

def add_note(text):
    notes.append(text)
def list_notes():
    return notes
from app.notes import add_note, list_notes

add_note("My first note")
print(list_notes())
