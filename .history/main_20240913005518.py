from gas_scrap import * 
from carmaintenance import car_maintenance_cost
from calculator import Car

print("Welcome to the car loan calculator!")
print()
print("Please select cars from our database below:")
for key, value in car_maintenance_cost.items():
    print(key, end=', ')
print()
print()


print("Here are the gas prices in your state:")
gas_price = Car.get_gas_prices()

for key, value in gas_price.items():
    print(key.capitalize(), ': $', value)

miles_city_month = 0
miles_highway_month = 0
total_miles_month = Car.get_user_mileage(miles_city_month, miles_highway_month)

n = input("Enter the brand of your car you wish to compare: ")

total_cost = {}

for i in range(n):
    car_brand = input("Enter the car brand from our database: ").capitalize()
    
    
    