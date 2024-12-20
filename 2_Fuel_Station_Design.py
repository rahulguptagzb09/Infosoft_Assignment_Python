"""
Problem #2 - Fuel Station Design
Design a fuel station for 3 types of vehicles - Diesel, Petrol, and Electric. There are a fixed number of spots
for each type of vehicle at the fuel station.
Implement the FuelStation class:
• FuelStation(int diesel, int petrol, int electric) creates a FuelStation object. The number of spots for each type of fuel is defined by the values provided to the constructor.
• bool fuel_vehicle(str fuel_type)looks up whether there is an open slot that can provide fuel_type. A vehicle can only be fueled in a slot space of its fuel_type. If there is no slot free, return false, else put the vehicle in that fuel slot and return true.
• bool open_fuel_slot(str fuel_type)releases a fuel slot of fuel_type so that another vehicle can be fueled. If you try to open a fuel slot, when all slots of a fuel_type are empty, return false. Otherwise, return true.
Input & Output:
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
fuel_station.fuel_vehicle(“diesel”) -> true (1 slot now open)
fuel_station.fuel_vehicle(“petrol”) -> true (1 slot now open)
fuel_station.fuel_vehicle(“diesel”) -> true (0 slots now open)
fuel_station.fuel_vehicle(“electric”) -> true (0 slots now open)
fuel_station.fuel_vehicle(“diesel”) -> false (0 slots open)
fuel_station.open_fuel_slot(“diesel”) -> true (1 slot now open)
fuel_station.fuel_vehicle(“diesel”) -> true (0 slots now open)
fuel_station.open_fuel_slot(“electric”) -> true (1 slot now open)
fuel_station.open_fuel_slot(“electric”) -> false (only 1 slot available at fuel station)

Explanation of the Code:

1. Class Initialization (__init__ method):
   - The constructor takes three arguments (diesel, petrol, and electric), representing the number of fuel slots available for each type of vehicle.
   - The self.parking dictionary stores the current state of fuel slots. The key is the fuel type ("diesel", "petrol", "electric"), and the value is a list where the first element is the number of filled slots and the second element is the total available slots.

2. fuel_vehicle method:
   - This method is used to fuel a vehicle. It checks whether there is an available slot for the specified fuel type. If there is, it increments the count of filled slots for that fuel type and returns True. Otherwise, it returns False.

3. open_fuel_slot method:
   - This method is used when a vehicle leaves the station and frees up a fuel slot. It checks if there are any vehicles occupying slots of the specified fuel type. If there are, it decrements the filled slot count and returns True. If no vehicles are occupying slots for that fuel type, it returns False.

4. Test Cases:
   - Various test cases are used to simulate the fueling process, including attempts to fuel vehicles when no slots are available and releasing fuel slots when vehicles leave.

Time and Space Complexity:
- Time Complexity: Each method (fuel_vehicle and open_fuel_slot) performs constant time operations. Checking and updating the self.parking dictionary are O(1) operations, so the overall time complexity for each operation is O(1).
- Space Complexity: The space complexity is O(3) because the dictionary contains three keys for the three fuel types, and each key holds a list with two values. Since the dictionary size is constant, the space complexity is O(1).
"""

class FuelStation:
    """
    The FuelStation class simulates a fuel station with specific slots for each type of vehicle: Diesel, Petrol, and Electric.
    - It allows fueling vehicles and managing available slots.
    - The parking dictionary keeps track of how many vehicles are currently in the slots (the first number in each list) 
      and the total capacity of slots for each fuel type (the second number in each list).
    """

    def __init__(self, diesel: int, petrol: int, electric: int):
        """
        Initializes the FuelStation with a given number of slots for diesel, petrol, and electric vehicles.
        Arguments:
            diesel -- the number of diesel fuel slots available
            petrol -- the number of petrol fuel slots available
            electric -- the number of electric fuel slots available
        """
        self.parking = {
            "diesel": [0, diesel],   # [current filled slots, total available slots for diesel]
            "petrol": [0, petrol],   # [current filled slots, total available slots for petrol]
            "electric": [0, electric] # [current filled slots, total available slots for electric]
        }

    def fuel_vehicle(self, carType: str) -> bool:
        """
        Attempts to fuel a vehicle of a given type (diesel, petrol, or electric).
        Arguments:
            carType -- the type of fuel needed for the vehicle (either "diesel", "petrol", or "electric")
        Returns:
            bool -- True if the vehicle is successfully fueled (i.e., there was an available slot), False otherwise.
        """
        # The new total of vehicles in the specified slot is the current filled slots + 1
        new_total = self.parking[carType][0] + 1
        
        # Check if there is space available in the specified fuel type
        if new_total <= self.parking[carType][1]:
            # If there is space, increment the current filled slots
            self.parking[carType][0] += 1
            return True  # Vehicle is fueled successfully
        return False  # No available slots, cannot fuel the vehicle

    def open_fuel_slot(self, carType: str) -> bool:
        """
        Frees up a fuel slot of the given fuel type when a vehicle leaves the station.
        Arguments:
            carType -- the type of fuel for which the slot is being freed (either "diesel", "petrol", or "electric")
        Returns:
            bool -- True if the slot is successfully opened (i.e., a vehicle has left), False if no slots were filled initially.
        """
        # Check if there are any vehicles occupying the fuel type slot
        if self.parking[carType][0] <= 0:
            # If no vehicles are occupying, return False
            return False
        # If there are vehicles occupying, decrement the number of filled slots
        self.parking[carType][0] -= 1
        return True  # Fuel slot has been successfully opened

# Example of how to use the FuelStation class

# Initialize a fuel station with 2 diesel, 2 petrol, and 1 electric slot
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)

# Initial parking state (all slots are empty)
print(fuel_station.parking)

# Try fueling different types of vehicles and print the state after each operation

# Fuel a diesel vehicle (success)
print(fuel_station.fuel_vehicle("diesel"))  # Expected: True
print(fuel_station.parking)

# Fuel a petrol vehicle (success)
print(fuel_station.fuel_vehicle("petrol"))  # Expected: True
print(fuel_station.parking)

# Fuel another diesel vehicle (success)
print(fuel_station.fuel_vehicle("diesel"))  # Expected: True
print(fuel_station.parking)

# Fuel an electric vehicle (success)
print(fuel_station.fuel_vehicle("electric"))  # Expected: True
print(fuel_station.parking)

# Try to fuel another diesel vehicle (fails, no more slots)
print(fuel_station.fuel_vehicle("diesel"))  # Expected: False
print(fuel_station.parking)

# Open a diesel fuel slot (success)
print(fuel_station.open_fuel_slot("diesel"))  # Expected: True
print(fuel_station.parking)

# Fuel a diesel vehicle after opening a slot (success)
print(fuel_station.fuel_vehicle("diesel"))  # Expected: True
print(fuel_station.parking)

# Open an electric fuel slot (success)
print(fuel_station.open_fuel_slot("electric"))  # Expected: True
print(fuel_station.parking)

# Try to open another electric fuel slot (fails, only 1 slot available)
print(fuel_station.open_fuel_slot("electric"))  # Expected: False
print(fuel_station.parking)
