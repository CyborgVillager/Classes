class Employee():
    #include fist,last,pay onto _init_(self) for it to work properly
    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@email.com'


    def fullname(self):
        return '{} {}' .format(self.first_name, self.last_name)

  #EMPLOYEE INFORMATION
#emp_1 = {'first_name':'John', 'last_name':'Henry', 'pay':'60000'}
emp_1 = Employee('John', 'Henry', 60000)
emp_2 = Employee('Mario', 'Lugio', 50000)
print(emp_2.fullname())

