from auth import login
from database import init_db
from patient import PatientService
from doctor import DoctorService
from appointment import AppointmentService
from billing import BillingService
from medical_records import RecordService

def menu():
    print("""
=== HOSPITAL MANAGEMENT SYSTEM ===
1. Register patient
2. Add doctor
3. Book appointment
4. Cancel appointment
5. Create bill
6. Pay bill
7. Add medical record
8. List patients
9. List doctors
10. List appointments
11. List bills
12. List records of patient
0. Exit
""")

def main():
    init_db()
    user = login()
    if not user:
        return

    patient = PatientService()
    doctor = DoctorService()
    appt = AppointmentService()
    bill = BillingService()
    rec = RecordService()

    while True:
        menu()
        ch = input("Select option: ")

        if ch == "0":
            break

        elif ch == "1":
            p = patient.create(
                input("Name: "),
                input("Age: "),
                input("Gender: "),
                input("Phone: "),
                input("Address: "),
            )
            print("Patient Registered:", p)

        elif ch == "2":
            d = doctor.add(
                input("Doctor name: "),
                input("Specialization: "),
                input("Phone: "),
            )
            print("Doctor Added:", d)

        elif ch == "3":
            a = appt.book(
                input("Patient ID: "),
                input("Doctor ID: "),
                input("Datetime (YYYY-MM-DD HH:MM): "),
                input("Reason: "),
            )
            print("Appointment booked:", a)

        elif ch == "4":
            appt.cancel(input("Appointment ID: "))
            print("Appointment cancelled.")

        elif ch == "5":
            pid = input("Patient ID: ")
            items = []
            print("Enter items (blank description to stop)")
            while True:
                desc = input("Description: ")
                if desc == "":
                    break
                amt = float(input("Amount: "))
                items.append({"description": desc, "amount": amt})
            b = bill.create_bill(pid, items)
            print("Bill Created:", b)

        elif ch == "6":
            res = bill.pay(input("Bill ID: "), float(input("Pay amount: ")))
            print("Updated bill:", res)

        elif ch == "7":
            r = rec.add(
                input("Patient ID: "),
                input("Doctor ID: "),
                input("Diagnosis: "),
                input("Notes: "),
            )
            print("Record Added:", r)

        elif ch == "8":
            print(patient.list())

        elif ch == "9":
            print(doctor.list())

        elif ch == "10":
            print(appt.list())

        elif ch == "11":
            print(bill.list())

        elif ch == "12":
            print(rec.list_for_patient(input("Patient ID: ")))

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()