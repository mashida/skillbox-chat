

class Human:
	first_name: str
	last_name: str


	def __init__(self, name, lastname="NoLastName"):
		self.first_name = name
		self.last_name = lastname
	

	def __str__(self):
		return f"Human: {self.first_name} {self.last_name}"


class User(Human):
	passport: str = "1234 123123"
	

	def hello(self):
		print(f"Hello, {self.first_name} {self.last_name}!")



john = User(lastname="Serditov", name="Nikita")
john.hello()
print(john.passport)

kate = User("Kate")
kate.hello()

