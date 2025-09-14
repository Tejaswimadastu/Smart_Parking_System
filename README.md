# Smart_Parking_System
🚗 Smart Parking System

A Python-based Smart Parking System demonstrating OOP concepts: Encapsulation, Inheritance, Polymorphism, and Abstraction.

📋 Features

Vehicle Hierarchy

Base class: Vehicle (encapsulated private attributes: license plate, owner name).

Derived classes:

Bike (helmet_required) – Fee: ₹20/hour

Car (seats) – Fee: ₹50/hour

SUV (four_wheel_drive) – Fee: ₹70/hour

Truck (max_load_capacity) – Fee: ₹100/hour

Overrides display() and calculate_parking_fee() → Demonstrates runtime polymorphism.

ParkingSpot

Spot sizes: S, M, L, XL.

Methods:

assign_vehicle(vehicle) – parks if size fits.

remove_vehicle() – unparks vehicle.

ParkingLot

Stores multiple spots.

Methods:

add_spot(size) – add new spot.

show_spots() – show all spots and statuses.

park_vehicle(vehicle) – find and assign a suitable spot.

unpark_vehicle(vehicle, hours) – free spot, calculate fee, process payment.

Payment (Abstraction)

Abstract class Payment (from abc).

Child classes: CashPayment, CardPayment, UPIPayment.

Each overrides process_payment(amount) to print payment method.

Main Program Demonstration

Create mixed parking spots and vehicles.

Park and unpark different vehicles.

Show direct access to private attributes fails, but getters/setters work.

Display spot statuses and process payments interactively.

🏗️ Concepts Demonstrated

Encapsulation: Private attributes (__license_plate, etc.) with getters/setters.

Inheritance: Bike, Car, SUV, and Truck inherit Vehicle.

Polymorphism: display() and calculate_parking_fee() behave differently for each subclass.

Abstraction: Payment as an abstract class with specific implementations.

▶️ Usage

Clone the repository or copy the code.

Run the program:

python smart_parking_system.py


Follow prompts to:

Add parking spots.

Create and park vehicles.

Unpark vehicles and choose a payment method.

📂 File Structure
SmartParkingSystem/
├── smart_parking_system.py   # Main implementation
└── README.md                 # Project documentation

🧠 Example Workflow

Create 2 small, 2 medium, 1 large, and 1 XL spot.

Add vehicles: 1 Bike, 1 Car, 1 SUV, 1 Truck.

Park vehicles → show dynamic allocation.

Unpark a vehicle after hours → fee is calculated → choose UPIPayment → prints Paid ₹X via UPI.

🏆 Learning Outcomes

Design reusable OOP-based systems.

Understand class hierarchies and method overriding.

Implement abstract classes and polymorphism in Python.

Manage parking allocation logic based on vehicle types.

🏷️ Tags

#Python #OOP #Encapsulation #Inheritance #Polymorphism #Abstraction #ParkingSystem #SmartParking