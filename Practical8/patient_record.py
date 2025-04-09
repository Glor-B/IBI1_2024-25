class patient_record:
    def __init__(self, name, age, latest_submission, medical_history):
        self.name = name
        self.age = age
        self.latest_submission = latest_submission
        self.medical_history = medical_history
    def record(self):
        return 'Patient name:'+ self.name + '\t' + "Patient age:" + self.age + '\t' + "Update date:" + self.latest_submission + '\t' + "Medical history:" + self.medical_history

name, age, latest_submission, medical_history = input('Enter patient name:'), input('Enter patient age:'), input('Enter last usbmission data:'), input('Enter patient medical history:')

data = patient_record(name, age, latest_submission, medical_history).record()
print(data)