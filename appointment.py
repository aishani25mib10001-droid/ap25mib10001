from utils import generate_id, now_str
import database as db

class AppointmentService:
    def book(self, pid, did, datetime, reason=""):
        aid = generate_id("APP")
        db.execute("INSERT INTO appointments VALUES(?,?,?,?,?,?,?)",
            (aid, pid, did, datetime, reason, "scheduled", now_str()))
        return db.fetch("SELECT * FROM appointments WHERE appointment_id=?", (aid,))[0]

    def cancel(self, aid):
        db.execute("UPDATE appointments SET status='cancelled' WHERE appointment_id=?", (aid,))

    def list(self):
        return db.fetch("SELECT * FROM appointments")