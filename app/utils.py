# app/utils.py
def to_upper(text):
    return text.upper()
  
from datetime import datetime

def now():
    return datetime.now().isoformat()
