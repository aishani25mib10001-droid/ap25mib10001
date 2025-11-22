import json
from utils import generate_id, now_str
import database as db

class BillingService:
    def create_bill(self, pid, items):
        bid = generate_id("BIL")
        total = sum(float(i["amount"]) for i in items)
        db.execute("INSERT INTO bills VALUES(?,?,?,?,?,?)",
            (bid, pid, json.dumps(items), total, 0.0, now_str()))
        return db.fetch("SELECT * FROM bills WHERE bill_id=?", (bid,))[0]

    def pay(self, bid, amount):
        bill = db.fetch("SELECT * FROM bills WHERE bill_id=?", (bid,))
        if not bill:
            return None
        paid = bill[0]["paid"] + amount
        db.execute("UPDATE bills SET paid=? WHERE bill_id=?", (paid, bid))
        return db.fetch("SELECT * FROM bills WHERE bill_id=?", (bid,))[0]

    def list(self):
        bills = db.fetch("SELECT * FROM bills")
        for b in bills:
            b["items"] = json.loads(b["items"])
        return bills