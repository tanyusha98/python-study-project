# app/utils.py
def to_upper(text):
    return text.upper()
  
from datetime import datetime

def now():
    return datetime.now().isoformat()
from app.utils import to_upper

def test_upper():
    assert to_upper("hi") == "HI"
