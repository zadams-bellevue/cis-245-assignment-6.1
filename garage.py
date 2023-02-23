"""A Garage class to store vehicles"""

from typing import Iterator
from vehicle import Car, Truck, Vehicle

class Garage:
	"""A Garage class to store vehicles"""
	vehicles: list[Vehicle] = []
	car_count: int = 0
	truck_count: int = 0

	def __iter__(self) -> Iterator[Vehicle]:
		return iter(self.vehicles)

	def add_vehicle(self, vehicle: Vehicle) -> None:
		"""Add a vehicle to the garage"""
		if isinstance(vehicle, Car):
			self.car_count += 1
		elif isinstance(vehicle, Truck):
			self.truck_count += 1

		self.vehicles.append(vehicle)

	def get_car_count(self) -> int:
		"""Get the number of cars in the garage"""
		return self.car_count

	def get_truck_count(self) -> int:
		"""Get the number of trucks in the garage"""
		return self.truck_count
