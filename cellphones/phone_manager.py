# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
		
		 try: #tries to add employee 
			self.employees.append(employee)
		except ValueError as multipleEmployee: #raises exception if 2 employees with the same ID are added.
			print('You can not assign the same employee twice')

    def add_phone(self, phone):
        try: #tries to add phone 
			self.phones.append(phone)
		except ValueError as multiplePhones: #raises exception if 2 phones with the same ID are added.
			print('You can not assign the same phone twice')


    def assign(self, phone_id, employee):
 
		
        for phone in self.phones: #searches through each phone
            if phone.id == phone_id: #finds matching ID
                phone.assign(employee.id) #adds employee
			else :
                raise Exception(PhoneError) #raises an exception if not found


    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):

        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone
			else: 
				raise Exception(PhoneError) #raises an exception if employee doesn't exist
				return None #returns none
				


class PhoneError(Exception):
    pass
