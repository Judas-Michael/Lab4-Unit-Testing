import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
      
        testPhone1 = Phone(1, 'Apple', 'iPhone 6') #testphone1 assigned values
        testPhone2 = Phone(1, 'Apple', 'iPhone 5') #testphone2 assigned values

        testAssignmentMgr = PhoneAssignments() #assigns new name 
        testAssignmentMgr.add_phone(testPhone1) #adds phone 1

        with self.assertRaises(PhoneError): #raises error when testphone2 is added
            testAssignmentMgr.add_phone(testPhone2)


    def test_create_and_add_new_employee(self):
		
		testEmployee1 = Employee(1, 'John', 'Jacobs') #assigns employee1 data
		testEmployee2 = Employee(2, 'Jenny', 'Jenson') #assigns employee2 data
		
		testAssignmentMgr = EmployeeAssignments() #assigns name
		testAssignmentMgr.add_employee(testEmployee1) #adds employee1
		testAssignmentMgr.add_employee(testEmployee2) #adds employee2
		
		self.assertIn(testEmployee1, EmployeeAssignments) #makes sure employee1 is in employee assignments	
		self.assertIn(testEmployee2, EmployeeAssignments) #makes sure employee 2 is in employee assignments


    def test_create_and_add_employee_with_duplicate_id(self):
  
        testEmployee1 = Employee(1, 'John', 'Jacobs') #assigns employee1 data
		testEmployee2 = Employee(1, 'Jenny', 'Jenson') #assigns employee2 data but same ID

        testAssignmentMgr = EmployeeAssignments() #assigns new name 
        testAssignmentMgr.add_employee(testEmployee1) #adds employee1

        with self.assertRaises(EmployeeError): #raises error when employee2 is added
            testAssignmentMgr.add_employee(employee2)


    def test_assign_phone_to_employee(self):
   
		testPhone1 = Phone(1, 'Apple', 'iPhone 6') #testphone1 assigned values
		testEmployee1 = Employee(1, 'John', 'Jacobs') #assigns employee1 data

		assign(self, testPhone1, testEmployee1) #sends data to assign method
		self.assertIn(testPhone1, EmployeeAssignments) #checks for phone in employee data

  


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
       
		testPhone1 = Phone(1, 'Apple', 'iPhone 6') #testphone1 assigned values
		testEmployee1 = Employee(1, 'John', 'Jacobs') #assigns employee1 data
		testEmployee2 = Employee(2, 'Jenny', 'Jenson') #assigns employee2 data but same ID

		assign(self, testPhone1, testEmployee1) # assigns phone to employee
		 with self.assertRaises(PhoneError): #raises error when phone is assigned to extra employee
            assign(self, testPhone1, testEmployee2)


		


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.
		
		testPhone1 = Phone(1, 'Apple', 'iPhone 6') #testphone1 assigned values
		testEmployee1 = Employee(1, 'John', 'Jacobs') #assigns employee1 data
		testPhone2 = Phone(2, 'Apple', 'iPhone 5')

		assign(self, testPhone1, testEmployee1) # assigns phone to employee
		 with self.assertRaises(PhoneError): #raises error when phone is assigned to employee with phone
            assign(self, testPhone2, testEmployee1)



    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
    
		testPhone1 = Phone(1, 'Apple', 'iPhone 6') #testphone1 assigned values
		testEmployee1 = Employee(1, 'John', 'Jacobs') #assigns employee1 data

		assign(self, testPhone1, testEmployee1) # assigns phone to employee
		 with self.assertRaises(PhoneError): #raises error when same phone is assigned to the same person
            assign(self, testPhone1, testEmployee1)


    def test_un_assign_phone(self):
       
		testPhone1 = Phone(1, 'Apple', 'iPhone 6') #testphone1 assigned values
		testEmployee1 = Employee(1, 'John', 'Jacobs') #assigns employee1 data

		assign(self, testPhone1, testEmployee1) #sends data to assign method
		unassign(self,testPhone1, testEmployee1) #unassigns phone
		
		assertIsNone(employee_id) #looks for none as employee_id

    def test_get_phone_info_for_employee(self):
      
        # TODO check that the method raises an PhoneError if the employee does not exist
		
		testEmployee1 = Employee(1, 'John', 'Jacobs') #assigns employee1 data
		testEmployee2 = Employee(2, 'Jenny', 'Jenson') #assigns employee2 data
		
        testPhone1 = Phone(1, 'Apple', 'iPhone 6') #testphone1 assigned values
        testPhone2 = Phone(2, 'Apple', 'iPhone 5') #testphone2 assigned values
		
		assign(self, testPhone1, testEmployee1) #assigns phone
		phoneResult = phone_info(testEmployee1) #calls phone info
		
		self.assertIs(phoneResult, testPhone1) #verifies testPhone1 was returned as answer
		self.assertIsNone(testEmployee2) #looks for none as employee_id because employee 2 doesn't have a phone
		
		with self.assertRaises(PhoneError): #raises error when employee does not have phone
            phone_info(testEmployee2)

       