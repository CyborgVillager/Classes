#making a class
#first_name = input('What is your first name?')
#last_name = input('What is your last name?')

class Patient():
    #first name is first attribute, last name second, age third
    def __init__(self,first_name, last_name, age,patient_info):

        self.first_name = first_name #this is an attribute
        self.last_name = last_name  #this is an attribute
        self.age = age  #this is an attribute
        self.patient_info = patient_info #this is an attribute


    #Aquire first and last name w/ age
    def getFirst_Name(self):
        return self.first_name

    def getLast_Name(self):
        return self.last_name

    def getAge(self):
        return self.age

    def getPatient_Info(self):
        # instances for the patients
        patient_id120 = {'first_name': 'John', 'last_name': 'Kenry', 'age': 55}
        patient_id121 = {'first_name': 'Kelly', 'last_name': 'Wilso', 'age': 43}
        patient_id122 = {'first_name': 'Susan', 'last_name': 'Marie', 'age': 67}
        patient_id123 = {'first_name': 'Duke', 'last_name': 'Kenniham', 'age': 48}

        # Aquring the data for patient 123 Age
        age_of_patient = patient_id123.age
        print(age_of_patient)


def main():
    pass
   # patient_info = Patient('JOhn','Kent','55')
    #patient_info1 = Patient(age_of_patient)
    #print('The patient name is', patient_info.getFirst_Name(),patient_info.getLast_Name(),patient_info.getAge())

main()

