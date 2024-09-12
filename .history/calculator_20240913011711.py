from gas_scrap import * 
from carmaintenance import car_maintenance_cost


class Car:  
    def __init__(self, brand, price, down_payment, interest_rate, loan_term):  
        self.brand = brand  
        self.price = price  
        self.down_payment = down_payment  
        self.interest_rate = interest_rate    
        self.loan_term = loan_term  # In years  

    
    def get_gas_prices():
        '''Retrieves the current gas price for a given state'''
        url = 'https://gasprices.aaa.com/state-gas-price-averages/'
        gas_price = scrap_gas(url)
        user_state = input("Enter your state: ").capitalize()
        if user_state in gas_price:
            state_prices = gas_price[user_state]
            return state_prices
    
    
    def get_user_mileage(miles_city_month, miles_highway_month): 
        '''Calculates the miles driven in a month'''
        miles_city_weekdays = float(input("Enter miles driven in the city on weekdays: "))
        miles_city_weekends = float(input("Enter miles driven in the city on weekends: "))
        miles_highway_weekdays = float(input("Enter miles driven on highway on weekdays: "))
        miles_highway_weekends = float(input("Enter miles driven on highway on weekends: "))
        miles_city_month = (miles_city_weekdays*5) + (miles_city_weekends*2)*52/12
        miles_highway_month = (miles_highway_weekdays*5) + (miles_highway_weekends*2)*52/12
        total_miles_month = miles_city_month + miles_highway_month
        print(f"Your total mileage per month is {total_miles_month}")
       
       
    def get_car_mileage(miles_city_month, miles_highway_month, state_prices):
        city_mileage = float(input("Enter car miles driven in the city: "))
        highway_mileage = float(input("Enter car miles driven on the highway: "))
        fuel_type = input("Enter fuel type: ").capitalize()
        if fuel_type in state_prices:
            cost_per_gallon = float(state_prices[fuel_type])
        total_gas_cost = (miles_city_month/city_mileage)*cost_per_gallon + (miles_highway_month/highway_mileage)*cost_per_gallon   
        return total_gas_cost
    
    
    def get_monthly_maintenance_cost(brand):
        '''Calculates monthly maintenance cost'''
        return car_maintenance_cost[brand]  
    
    
    def get_monthly_interest_rate():
        '''Calculates monthly interest rate'''
        principal = float(input("Enter loan amount: "))
        interest_rate = float(input("Enter interest rate per year: "))
        loan_term = float(input("Enter loan term in years: "))
        down_payment = float(input("Enter down payment: "))
        sales_tax_rate = float(input("Enter sales tax rate: "))
        amount_owed = principal + ((principal * sales_tax_rate)/100)
        amount_owed = amount_owed - down_payment
        monthly_interest_rate = interest_rate/ 12/100
        
        
        if monthly_interest_rate == 0:
            monthly_payment = amount_owed / loan_term * 12
        else:
            monthly_payment = (amount_owed * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -loan_term)
        return monthly_payment
            
    
    def calculate_loan_amount(self):  
        '''Calculates the loan amount after down payment.'''  
        return self.price - self.down_payment  

    def calculate_monthly_payment(self):  
        '''Calculates the monthly payment using the formula M = P * (r * (1 + r)^n) / ((1 + r)^n - 1).
        Where:
        M = monthly loan payment
        P = principal amount of the loan (purchase price minus down payment)
        r = monthly interest rate (annual interest rate divided by 12)
        n = number of payments (number of months in the loan term)
        '''  
        
        loan_amount = self.calculate_loan_amount()  
        monthly_interest_rate = self.interest_rate / 12  # Monthly interest rate  
        number_of_payments = self.loan_term * 12  # Total number of monthly payments  

        if self.interest_rate == 0:  
            return loan_amount / number_of_payments  

        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)  
        return monthly_payment  

    def display_loan_summary(self):  
        '''Returns a summary of the loan details.'''
        monthly_payment = self.calculate_monthly_payment()  
        total_payment = monthly_payment * self.loan_term * 12  
        total_interest = total_payment - self.calculate_loan_amount()  
        
        summary = {  
            'brand': self.brand,  
            'monthly_payment': monthly_payment,  
            'total_payment': total_payment,  
            'total_interest': total_interest  
        }  
        return summary  


# car = Car()
# gas_price = car.get_gas_prices()


#     def compare_cars(car1, car2):  
#         '''Compares two car loans and prints their summaries.'''  
#         summary1 = car1.display_loan_summary()  
#         summary2 = car2.display_loan_summary()  

#         print(f"\nLoan Summary for {summary1['brand']}:")  
#         print(f"Monthly Payment: ${summary1['monthly_payment']:.2f}")  
#         print(f"Total Payments: ${summary1['total_payment']:.2f}")  
#         print(f"Total Interest Paid: ${summary1['total_interest']:.2f}")  

#         print(f"\nLoan Summary for {summary2['brand']}:")  
#         print(f"Monthly Payment: ${summary2['monthly_payment']:.2f}")  
#         print(f"Total Payments: ${summary2['total_payment']:.2f}")  
#         print(f"Total Interest Paid: ${summary2['total_interest']:.2f}")  

#         # Comparison  
#         if summary1['monthly_payment'] < summary2['monthly_payment']:  
#             print(f"\n{summary1['brand']} has a lower monthly payment than {summary2['brand']}.")  
#         elif summary1['monthly_payment'] > summary2['monthly_payment']:  
#             print(f"\n{summary2['brand']} has a lower monthly payment than {summary1['brand']}.")  
#         else:  
#             print(f"\nBoth cars have the same monthly payment.")  


# if __name__ == "__main__":  
#     # Input values for the first car  
#     print("Enter details for Car Brand 1:")  
#     brand1 = input("Brand Name: ")  
#     price1 = float(input("Car price: $"))  
#     down_payment1 = float(input("Down payment: $"))  
#     interest_rate1 = float(input("Interest rate (in %): "))  
#     loan_term1 = int(input("Loan term (in years): "))  

#     # Create the first Car object  
#     car1 = Car(brand1, price1, down_payment1, interest_rate1, loan_term1)  

#     # Input values for the second car  
#     print("\nEnter details for Car Brand 2:")  
#     brand2 = input("Brand Name: ")  
#     price2 = float(input("Car price: $"))  
#     down_payment2 = float(input("Down payment: $"))  
#     interest_rate2 = float(input("Interest rate (in %): "))  
#     loan_term2 = int(input("Loan term (in years): "))  

#     # Create the second Car object  
#     car2 = Car(brand2, price2, down_payment2, interest_rate2, loan_term2)  

#     # Compare the two cars  
#     compare_cars(car1, car2)