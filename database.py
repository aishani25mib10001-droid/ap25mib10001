import sqlite3
from pathlib import Path

DB_PATH = Path("data/hospital.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS patients(
        patient_id TEXT PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        phone TEXT,
        address TEXT,
        created_at TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS doctors(
        doctor_id TEXT PRIMARY KEY,
        name TEXT,
        specialization TEXT,
        phone TEXT,
        created_at TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS appointments(
        appointment_id TEXT PRIMARY KEY,
        patient_id TEXT,
        doctor_id TEXT,
        appointment_datetime TEXT,
        reason TEXT,
        status TEXT,
        created_at TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
        FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id)
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS bills(
        bill_id TEXT PRIMARY KEY,
        patient_id TEXT,
        items TEXT,
        total_amount REAL,
        paid REAL,
        created_at TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS records(
        record_id TEXT PRIMARY KEY,
        patient_id TEXT,
        doctor_id TEXT,
        diagnosis TEXT,
        notes TEXT,
        created_at TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
        FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id)
    )""")

    conn.commit()
    conn.close()

def fetch(query, params=()):
    conn = get_conn()
    c = conn.cursor()
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def execute(query, params=()):
    conn = get_conn()
    c = conn.cursor()
    c.execute(query, params)
    conn.commit()
    conn.close()