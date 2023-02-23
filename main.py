#!/usr/bin/env python3

"""Assignment 6.1"""

from garage import Garage
from vehicle import Car, Truck

def get_int_input(prompt: str) -> int:
	"""Display a prompt and get an integer input.
	If the input is not an integer, an error message is displayed,
	then prompt is re-displayed, and the next input is used.
	"""
	while True:
		num = input(f"{prompt} ")
		try:
			return int(num)
		except ValueError:
			print("Please input a whole number.")

def get_float_input(prompt: str) -> float:
	"""Display a prompt and get a number input.
	If the input is not a number, an error message is displayed,
	then prompt is re-displayed, and the next input is used.
	"""
	while True:
		num = input(f"{prompt} ")
		try:
			return float(num)
		except ValueError:
			print("Please input a number.")

def get_string_input(prompt: str) -> str:
	"""Display a prompt and get a string input.
	If the string is empty the prompt is re-displayed and the next input is used.
	"""
	while True:
		in_str = input(f"{prompt} ")
		if in_str != "":
			return in_str

def main() -> None:
	"""Main"""
	garage = Garage()
	while True:
		car_or_truck = ""
		while car_or_truck not in ["car", "truck", "quit"]:
			car_or_truck = get_string_input("Would you like to create a car or a truck? [car|truck|quit]:").lower()

		if car_or_truck == "quit":
			break

		# Create object
		vehicle = Car() if car_or_truck == "car" else Truck()

		# Set make and model
		vehicle.SetVehicleMake(get_string_input(f"Enter the make of the {car_or_truck}:"))
		vehicle.SetVehicleModel(get_string_input(f"Enter the model of the {car_or_truck}:"))

		if isinstance(vehicle, Car):
			vehicle.SetCarDoor(get_int_input("Enter the number of doors:"))
		elif isinstance(vehicle, Truck):
			vehicle.SetBedLength(get_float_input("Enter the bed length in feet:"))

		garage.add_vehicle(vehicle)
		print(f"You have added a(n) {vehicle.describe()} to your garage.\n")

	print(f"\nYour garage contains {garage.get_car_count()} car(s) and {garage.get_truck_count()} truck(s):")
	for vehicle in garage:
		print(f"A(n) {vehicle.describe()}")

if __name__ == "__main__":
	main()
