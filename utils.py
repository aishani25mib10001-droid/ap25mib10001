import uuid
from datetime import datetime

def generate_id(prefix="ID"):
    return f"{prefix}-{uuid.uuid4().hex[:8]}"

def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")