# Creating the employee class

class Employee:

    # setting up the empoyee constructor
    def __init__(self, emp_name, emp_number):
        self.__emp_name = emp_name
        self.__emp_number = emp_number

    # defining the accessors and mutators for the attributes
    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name
    
    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number

    def return_emp_name(self):
        return self.__emp_name
    
    def return_emp_number(self, ):
        return self.__emp_number 


# Creating the employee class
class ProductionWorker(Employee):
    
    # setting up the empoyee constructor
    def __init__(self, emp_name, emp_number, shift_number, hourly_rate):
        Employee.__init__(self, emp_name, emp_number)
        self.__shift_number = shift_number
        self.__hourly_rate = hourly_rate

 # defining the accessors and mutators for the attributes

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def return_shift_number(self):
        return self.__shift_number

    def return_hourly_rate(self):
        return self.__hourly_rate

# Defining the shift method
    def shift_method(self):
        shift_detail = ''
        if self.__shift_number == 1:
            shift_detail = 'Day'
        elif shift_detail == '2':
            shift_detail = 'Night'
        else:
            shift_detail = 'Wrong Input'
        
        return shift_detail 
        



