class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies


class Hospital(Patient):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.beds = capacity
        self.patientBed = 0
        self.patients = []
        
        self.patientBeds = []
        while self.capacity > 0:
            self.patientBeds.append(self.capacity)
            self.capacity -= 1

    
    def admit(self, id, name, allergies):
        if self.patientBeds:
            self.patientBed = self.patientBeds[0]
            patientNew = {
                'admitList': Patient(id, name, allergies),
                'bed_num': self.patientBed
            }
            self.patients.append(patientNew)
            self.beds -= 1
            self.patientBeds.pop(0)
            print 'You have successfully been admitted.'
        else:
            print 'We cannot admit you, hospital is full.' 
        return self
    
    def discharge(self, name):
        for patient in self.patients:
            if patient['admitList'].name == name:
                dischargeID = self.patients.index(patient)
                self.patientBeds.append(patient['bed_num'])
        self.patients.pop(dischargeID)
        self.beds += 1
        return self
    
    def display(self):
        print 'Hospital:', self.name
        print 'The number of available beds is:', self.beds
        print 'Admitted Patients:'
        for patient in self.patients:
            print "Patient Info:" 
            print "*Name:", patient['admitList'].name
            print "*Allergies:", patient['admitList'].allergies
            print "*Bed #:", patient['bed_num']



x = Hospital('St Lukes', 300)
x.admit(2,'Holly','c-chlor').display()
x.admit(6,'Michael','morphine').admit(12,'George','peanuts').display()
x.discharge('Michael').display()