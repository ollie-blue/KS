from gas_scrap import * 
from carmaintenance import car_maintenance_cost
from calculator import *

print("Welcome to the car loan calculator!")
print()
print("Please select cars from our database below:")
for key, value in car_maintenance_cost.items():
    print(key, end=', ')
print()
print()
# brand = input("Enter your car brand: ").capitalize()
# price = float(input("Enter your car price: "))

print("Here are the gas prices in your state:")

