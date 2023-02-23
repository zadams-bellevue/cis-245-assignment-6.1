# Ignore intentional violations of snake case naming convention since we're following a class diagram that uses a weird convention.
# pylint: disable=invalid-name

"""Vehicle classes"""

class Vehicle:
	"""Vehicle superclass containing make and model"""
	# Note that this class doesn't use a good case convention, but it's followed because the class diagram for the assignment requires it.
	# These property names are also horribly redundant, simply "make" and "model" would suffice.
	# This would also be better off as Optional[string], but the assignment says it should be string, so we use a default of "unknown".
	VehicleMake: str = "unknown"
	VehicleModel: str = "unknown"

	def GetVehicleMake(self) -> str:
		"""Get the vehicle's make"""
		return self.VehicleMake

	def SetVehicleMake(self, make: str) -> None:
		"""Set the vehicle's make"""
		self.VehicleMake = make

	def GetVehicleModel(self) -> str:
		"""Get the vehicle's model"""
		return self.VehicleModel

	def SetVehicleModel(self, model: str) -> None:
		"""Set the vehicle's model"""
		self.VehicleModel = model

	def describe(self) -> str:
		"""Get a string describing the vehicle"""
		return f"{self.GetVehicleMake()} {self.GetVehicleModel()}"

class Car(Vehicle):
	"""Car Vehicle type that has a car door count."""
	# Technically the class diagram says this should be a string, but storing
	# the number of doors as a string is so asinine that it must be a mistake.
	# This is also horribly named, and should be called something like "number_of_doors".
	# Since it's not allowed to be Optional[int] we default it to 0.
	CarDoor: int = 0

	def GetCarDoor(self) -> int:
		"""Get the number of doors"""
		return self.CarDoor

	def SetCarDoor(self, door_count: int) -> None:
		"""Set the number of doors"""
		self.CarDoor = door_count

	def describe(self) -> str:
		"""Get a string describing the car"""
		return f"{super().describe()} with {self.GetCarDoor()} doors"

class Truck(Vehicle):
	"""Truck Vehicle type that has a bed length."""
	# This is stored as a float instead of as a string as indicated by the class diagram.
	# Finally a property that's rationally named, even if it uses a weird capitalization convention.
	# Since it's not allowed to be Optional[float] we default it to 0.0.
	# Since it's not specified, we'll assume it's length in feet.
	BedLength: float = 0.0

	def GetBedLength(self) -> float:
		"""Get the length of the truck bed in feet"""
		return self.BedLength

	def SetBedLength(self, bed_length: float) -> None:
		"""Set the length of the truck bed in feet"""
		self.BedLength = bed_length

	def describe(self) -> str:
		"""Get a string describing the truck"""
		return f"{super().describe()} with a {self.GetBedLength()}' bed"
