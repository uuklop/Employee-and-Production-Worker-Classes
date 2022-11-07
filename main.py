import employee

def main():
    
    # opening a connection with a file
    in_file = open('Employee_Data','w')

    # Opening a connection with a file for the production worker class
    in_file2 = open('Production_Worker', 'w')

    # Getting the user input
    print('\nEmployee Data')
    emp_name = input("Employee name: ")
    emp_number  = input("Employee number: ")

    # Creating the object for employee class
    employee_one = employee.Employee(emp_name, emp_number)

    # Getting the user input for productionWorker class
    print('\nProduction worker details')
    emp_name = input("Employee name: ")
    emp_number  = input("Employee number: ")
    shift_number = int(input('Shif Number: '))
    hourly_rate = float(input('Hourly Rate: '))
     
    #  Creating the object for production worker class
    productionWorkerOne = employee.ProductionWorker(emp_name, emp_number, shift_number, hourly_rate)

    # Saving the inputs into the respective text files

    # writing the file to the text file
    in_file.write(f'Employee Name: {employee_one.return_emp_name()} \n')
    in_file.write(f'Empolyee Number: {employee_one.return_emp_number()}\n')

    # writing the file to the text file
    in_file2.write(f'Employee Name: {productionWorkerOne.return_emp_name()} \n')
    in_file2.write(f'Empolyee Number: {productionWorkerOne.return_emp_number()}\n')
    in_file2.write(f'Shift: {productionWorkerOne.shift_method()} \n')
    in_file2.write(f'Hourly Rate: {str(hourly_rate)}\n')

    print(f'\nEmployee Data')
    print(f'---------------')
    print(f'Employee Name: {employee_one.return_emp_name()}')
    print(f'Employee Number: {employee_one.return_emp_number()}') 


    print('\nProduction Worker Details')
    print('--------------------------')
    print(f'Employee Name: {productionWorkerOne.return_emp_name()}')
    print(f'Employee Number: {productionWorkerOne.return_emp_number()}') 
    print(f'Shift Number: {productionWorkerOne.shift_method()}')
    print(f'Hourly Rate: {productionWorkerOne.return_hourly_rate()}')



    
# Calling the Main Function
if __name__ == '__main__':
    main()