from utils import generate_id, now_str
import database as db

class DoctorService:
    def add(self, name, specialization, phone):
        did = generate_id("DOC")
        db.execute("INSERT INTO doctors VALUES(?,?,?,?,?)",
            (did, name, specialization, phone, now_str()))
        return db.fetch("SELECT * FROM doctors WHERE doctor_id=?", (did,))[0]

    def list(self):
        return db.fetch("SELECT * FROM doctors")