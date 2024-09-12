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

n = int(input("Enter the brand of your car you wish to compare: "))

total_cost = {}

for i in range(n):
    car_brand = input("Enter the car brand from our database: ").capitalize()
    if car_brand not in car_maintenance_cost.keys():
        print("Sorry, we do not have this car in our database.")
    monthly_maintenance_cost = Car.get_monthly_maintenance_cost(car_brand)
    monthly_gas_cost = Car.get_car_mileage(miles_city_month, miles_highway_month, gas_price)
    monthly_interest_payment = Car.get_monthly_interest_rate()
    total_monthly_costs = monthly_maintenance_cost + monthly_gas_cost + monthly_interest_payment
    total_cost[car_brand] = total_monthly_costs
    print("Here is your summary:")
    print("Your preferred car: ", car_brand)
    print(f"Total monthly maintenance costs: $' {monthly_maintenance_cost:.2f}")
    print(f"Total monthly gas costs: $' {monthly_gas_cost:.2f}")
    print(f"Total monthly interest payment: $' {monthly_interest_payment:.2f}")
    print(f"Total monthly costs: $' {monthly_maintenance_cost:.2f}")
    print(f"Total monthly costs: $' {total_monthly_costs:.2f}")
    

    
    