# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
  pass

# Parent: Vehicle
class FlightVehicle(Vehicle):
  pass

# Parent: Vehicle
class GroundVehicle(Vehicle):
  pass

# Parent: FlightVehicle
class Airplane(FlightVehicle):
  pass

# Parent: FlightVehicle
class Starship(FlightVehicle):
  pass

# Parent: GroundVehicle
class Car(GroundVehicle):
  pass

# Parent: GroundVehicle
class Motorcycle(GroundVehicle):
  pass