from utils import generate_id, now_str
import database as db

class PatientService:
    def create(self, name, age, gender, phone, address=""):
        pid = generate_id("PAT")
        db.execute("INSERT INTO patients VALUES(?,?,?,?,?,?,?)",
            (pid, name, age, gender, phone, address, now_str()))
        return db.fetch("SELECT * FROM patients WHERE patient_id=?", (pid,))[0]

    def list(self):
        return db.fetch("SELECT * FROM patients")

    def get(self, pid):
        rows = db.fetch("SELECT * FROM patients WHERE patient_id=?", (pid,))
        return rows[0] if rows else None