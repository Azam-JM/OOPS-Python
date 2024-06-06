class Doctor:
    def __init__(self, name) -> None:
        self.name = name
    
class Patient:
    def __init__(self, name) -> None:
        self.name = name
        self.doctor = None
    
    def assign_doctor(self, doctor) -> None:
        self.doctor = doctor

doctor = Doctor("Mr")
patient = Patient("X")
patient.assign_doctor(doctor)
print(f"The doctor for patient: {patient.name} is {patient.doctor.name}")
