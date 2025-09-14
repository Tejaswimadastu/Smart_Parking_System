from abc import ABC, abstractmethod
import random
class Vehicle:
    def __init__(self, license_plate, owner_name, parking_lot):
        self.__license_plate = license_plate
        self.__owner_name = owner_name
        self.__parking_lot = parking_lot
    @property
    def license_plate(self):
        return self.__license_plate
    @license_plate.setter
    def license_plate(self, value):
        self.__license_plate = value
    @property
    def owner_name(self):
        return self.__owner_name
    @owner_name.setter
    def owner_name(self, value):
        self.__owner_name = value

    def display(self):
        print(f"License number is {self.license_plate}\nOwner name is {self.owner_name}")

    def calculate_parking_fee(self, hours):
        return 0
class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, parking_lot, helmet):
        super().__init__(license_plate, owner_name, parking_lot)
        self.helmet = helmet

    def display(self):
        print(f"License plate: {self.license_plate}\nOwner name: {self.owner_name}\nParking Lot: {self._Vehicle__parking_lot}\nHelmet Required: {self.helmet}")

    def calculate_parking_fee(self, hours):
        return 20 * hours
class Car(Vehicle):
    def __init__(self, license_plate, owner_name, parking_lot, seat):
        super().__init__(license_plate, owner_name, parking_lot)
        self.seat = seat
    def display(self):
        print(f"License plate: {self.license_plate}\nOwner name: {self.owner_name}\nParking Lot: {self._Vehicle__parking_lot}\nSeat Count: {self.seat}")
    def calculate_parking_fee(self, hours):
        return 50 * hours
class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, parking_lot, four_wheel_drive):
        super().__init__(license_plate, owner_name, parking_lot)
        self.four_wheel_drive = four_wheel_drive
    def display(self):
        print(f"License plate: {self.license_plate}\nOwner name: {self.owner_name}\nParking Lot: {self._Vehicle__parking_lot}\n4-Wheel Drive: {self.four_wheel_drive}")
    def calculate_parking_fee(self, hours):
        return 70 * hours
class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, parking_lot, max_load_capacity):
        super().__init__(license_plate, owner_name, parking_lot)
        self.max_load_capacity = max_load_capacity
    def display(self):
        print(f"License plate: {self.license_plate}\nOwner name: {self.owner_name}\nParking Lot: {self._Vehicle__parking_lot}\nMax Load Capacity: {self.max_load_capacity} tons")
    def calculate_parking_fee(self, hours):
        return 100 * hours
# Parking Spot Class
class parking_spot:
    size_map = {"Bike": "S", "Car": "M", "SUV": "L", "Truck": "XL"}
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.__size = size
        self.__vehicle = None
    @property
    def size(self):
        return self.__size
    @property
    def vehicle(self):
        return self.__vehicle
    def assign_vehicle(self, vehicle):
        vehicle_type = type(vehicle).__name__
        required_size = parking_spot.size_map[vehicle_type]
        size_order = ["S", "M", "L", "XL"]
        if size_order.index(self.__size) >= size_order.index(required_size):
            if self.__vehicle is None:
                self.__vehicle = vehicle
                print(f"{vehicle_type} parked in spot {self.spot_id}")
                return True
            else:
                print(f"Spot {self.spot_id} is already occupied")
                return False
        else:
            print(f"{vehicle_type} cannot fit in spot {self.spot_id} (Size: {self.__size})")
            return False
    def remove_vehicle(self):
        if self.__vehicle:
            vehicle = self.__vehicle
            self.__vehicle = None
            print(f"{type(vehicle).__name__} removed from spot {self.spot_id}")
            return vehicle
        else:
            print(f"Spot {self.spot_id} is empty")
            return None
    def status(self):
        if self.__vehicle:
            return f"Occupied by {type(self.__vehicle).__name__}"
        else:
            return "Empty"
# Parking Lot Class
class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []
    def add_spots(self, spot):
        self.spots.append(spot)
    def show_spots(self):
        print(f"\nParking Lot: {self.name}")
        for spot in self.spots:
            print(f"Spot {spot.spot_id} (Size: {spot.size}) - {spot.status()}")
    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.assign_vehicle(vehicle):
                return spot
        print("No suitable spot available")
        return None
    def unpark_vehicle(self, vehicle, hours):
        for spot in self.spots:
            if spot.vehicle == vehicle:
                spot.remove_vehicle()
                fee = vehicle.calculate_parking_fee(hours)
                print(f"Parking Fee for {type(vehicle).__name__}: ₹{fee}")
                return fee
        print("Vehicle not found")
        return 0
# Payment Abstraction
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Cash.")
class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Card.")
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI.")
# Main Interactive Program
if __name__ == "__main__":
    parking_lot = ParkingLot("Main Lot")
    parking_lot.add_spots(parking_spot(1, 'S'))
    parking_lot.add_spots(parking_spot(2, 'M'))
    parking_lot.add_spots(parking_spot(3, 'L'))
    parking_lot.add_spots(parking_spot(4, 'XL'))
    vehicles = []
    print("\n--- Smart Parking System ---")
    n = int(input("Enter number of vehicles to register: "))
    for _ in range(n):
        print("\nSelect Vehicle Type:\n1. Bike\n2. Car\n3. SUV\n4. Truck")
        choice = input("Enter choice (1-4): ")
        license_plate = input("Enter License Plate: ")
        owner_name = input("Enter Owner Name: ")
        parking_lot_name = "Main Lot"  # fixed for simplicity
        if choice == '1':
            helmet = input("Helmet required (yes/no): ").lower() == 'yes'
            vehicle = Bike(license_plate, owner_name, parking_lot_name, helmet)
        elif choice == '2':
            seat = int(input("Number of Seats: "))
            vehicle = Car(license_plate, owner_name, parking_lot_name, seat)
        elif choice == '3':
            four_wheel_drive = input("Four wheel drive (yes/no): ").lower() == 'yes'
            vehicle = SUV(license_plate, owner_name, parking_lot_name, four_wheel_drive)
        elif choice == '4':
            max_load_capacity = float(input("Max Load Capacity (tons): "))
            vehicle = Truck(license_plate, owner_name, parking_lot_name, max_load_capacity)
        else:
            print("Invalid choice. Skipping.")
            continue
        vehicles.append(vehicle)
    print("\n--- Parking Vehicles ---")
    for vehicle in vehicles:
        vehicle.display()
        parking_lot.park_vehicle(vehicle)
    parking_lot.show_spots()
    print("\n--- Unparking Vehicles and Processing Payment ---")
    for vehicle in vehicles:
        hours = int(input(f"\nEnter parking duration in hours for {vehicle.license_plate}: "))
        fee = parking_lot.unpark_vehicle(vehicle, hours)
        if fee:
            print("\nChoose payment method:\n1. Cash\n2. Card\n3. UPI")
            method_choice = input("Enter choice (1-3): ")
            if method_choice == '1':
                payment_method = CashPayment()
            
            elif method_choice == '2':
                payment_method = CardPayment()
            else:
                payment_method = UPIPayment()
            payment_method.process_payment(fee)
    parking_lot.show_spots()
