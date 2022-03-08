# test inheritence and polymorphism
# create the parent class
class SoftwareEngineer:

	#class attributes
	alias1 = "Keyboard Guru"
	alias2 = "Coding Ninja"

	def __init__(self, name, age, level, salary, language):
		# instance attributes
		self.name = name
		self.age = age
		self.level = level
		self.salary = salary
		self.language = language
		

	# instance method
	def work(self):
		return f"{self.name} is writing code..."

	# overwriting default langauage set for instances
	# note the language parameter does not include self
	def code_more(self, language):
		return f"{self.name} is now writing code in {language}"

	# special dunder method
	# this method will show a string version of an object
	def __str__(self):
		return f"""
		name = {self.name}, 
		age = {self.age}, 
		level = {self.level}, 
		salary = {self.salary}, 
		expertise = {self.language}\n"""

		
# create the child class to inherit from parent
# inherit, extend, overwrite the parent class
class Designer(SoftwareEngineer):
	# inheriting from the parent class
	def __init__(self, name, age, level, salary, language, group):
		# super refers to the parent class
		# dunder init refers to all instance variables inherited
		super().__init__(name, age, level, salary, language)
		# extend instance variables
		self.group = group

	# extend the child class with own methods
	def meeting(self):
		return f"{self.name} is in a meeting with database designers"
	
	# override the child methods
	def work(self):
		return f"{self.name} is working on a data model..."

	# override the parent method
	def __str__(self):
		return f"""
		name = {self.name}, 
		age = {self.age}, 
		level = {self.level}, 
		salary = {self.salary}, 
		expertise = {self.language}, 			
		group = {self.group}\n"""


se3 = SoftwareEngineer("Mia", 27, "senior developer", 7100, "python")
#print(se3)

d1 = Designer("Lara", 26, "consultant", 6400, "postgresql", "database desinger")
#print(d1)
print(se3.work())
print(se3.code_more("javascript"))
print(d1.work())
print(f"{d1.name} is a {d1.alias1}")
print(f"{se3.name} is a {se3.alias2}")

# polymorphism
# list of people from various roles
employees = [SoftwareEngineer("Sam", 27, "senior developer", 7100, "python"),
			SoftwareEngineer("Jenny", 25, "lead developer", 8500, "python"),
			Designer("Paul", 26, "consultant", 6400, "postgresql", "database desinger"),
			Designer("Mark",30, "senior designer", 7600, "mongodb", "database desinger")]

# it doesn't matter which person is to which role
# polymorphism ensures the correct __str__() is called for the type of employee
for employee in employees:
	print(employee)
	print(employee.work())
	#print(employee.meeting())

# note: polymorphism doesn't work  
# if calling functions specific to a class (parent or child) 
print(employees[2].meeting()) 
# calling a method specific to a class object 
