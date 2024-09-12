from gas_scrap import * 
from carmaintenance import car_maintenance_cost


def get_gas_prices():
        '''
        Retrieves the current gas price for a given state
        '''
        url = 'https://gasprices.aaa.com/state-gas-price-averages/'
        gas_price = scrap_gas(url)
        user_state = input("Enter your state: ").capitalize()
        if user_state in gas_price:
            state_prices = gas_price[user_state]
            return state_prices
        
def get_user_mileage(miles_city_month, miles_highway_month): 
    '''
    Calculates the miles driven in a month 
    '''
    miles_city_weekdays = float(input("Enter miles driven in the city on weekdays: "))
    miles_city_weekends = float(input("Enter miles driven in the city on weekends: "))
    miles_highway_weekdays = float(input("Enter miles driven on highway on weekdays: "))
    miles_highway_weekends = float(input("Enter miles driven on highway on weekends: "))
    miles_city_month = (miles_city_weekdays*5) + (miles_city_weekends*2)*52/12
    miles_highway_month = (miles_highway_weekdays*5) + (miles_highway_weekends*2)*52/12
    total_miles_month = miles_city_month + miles_highway_month
    return total_miles_month
           

def get_monthly_maintenance_cost(brand):
    '''
    Calculates monthly maintenance cost
    '''
    return car_maintenance_cost[brand]

    
def get_car_mileage(miles_city_month, miles_highway_month, state_prices):
    city_mileage = float(input("Enter car miles driven in the city: "))
    highway_mileage = float(input("Enter car miles driven on the highway: "))
    fuel_type = input("Enter fuel type: ").capitalize()
    if fuel_type in state_prices:
        cost_per_gallon = float(state_prices[fuel_type])
    total_gas_cost = (miles_city_month/city_mileage)*cost_per_gallon + (miles_highway_month/highway_mileage)*cost_per_gallon   
    return total_gas_cost

