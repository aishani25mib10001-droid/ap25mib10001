from utils import generate_id, now_str
import database as db

class RecordService:
    def add(self, pid, did, diagnosis, notes=""):
        rid = generate_id("REC")
        db.execute("INSERT INTO records VALUES(?,?,?,?,?,?)",
           (rid, pid, did, diagnosis, notes, now_str()))
        return db.fetch("SELECT * FROM records WHERE record_id=?", (rid,))[0]

    def list_for_patient(self, pid):
        return db.fetch("SELECT * FROM records WHERE patient_id=?", (pid,))