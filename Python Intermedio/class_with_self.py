class Car:
	wheel_number = 4
	
	def my_first_method(self):
		print("Hello OOP World!")

	def show_history(self, miles, crashes):
		print(f"This car has {miles} miles, {crashes} crashes and {self.wheel_number} wheels")
		
		
my_car = Car()

my_truck = Car()
my_truck.wheel_number = 6

my_bigger_truck = Car()
my_bigger_truck.wheel_number = 8


my_car.show_history(45000, 2)
my_truck.show_history(45000, 2)
my_bigger_truck.show_history(45000, 2)