

class Car:  
    def __init__(self, brand, price):  
        self.brand = brand  
        self.price = price  

    def calculate_principal(self, down_payment):  
        """  
        Calculate the principal amount of the loan.  
        """  
        return self.price - down_payment  

    def calculate_monthly_payment(self, down_payment, annual_interest_rate, loan_term_years):  
        """  
        Calculate the monthly payment for the car loan.  
        """  
        principal = self.calculate_principal(down_payment)  
        monthly_interest_rate = (annual_interest_rate / 100) / 12  
        total_payments = loan_term_years * 12  

        if monthly_interest_rate == 0:  # If the interest rate is 0%  
            monthly_payment = principal / total_payments  
        else:  
            monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)  

        return monthly_payment  


# Example usage  
if __name__ == "__main__":  
    # Create a car object  
    my_car = Car("Toyota Camry", 30000)  

    # Input loan parameters  
    down_payment = 5000  # The down payment  
    annual_interest_rate = 5  # Annual interest rate in percent  
    loan_term_years = 5  # Loan term in years  

    # Calculate principal  
    principal = my_car.calculate_principal(down_payment)  
    print(f"Principal amount for loan: ${principal:.2f}")  

    # Calculate monthly payment  
    monthly_payment = my_car.calculate_monthly_payment(down_payment, annual_interest_rate, loan_term_years)  

    # Output the results  
    print(f"Monthly payment for {my_car.brand}: ${monthly_payment:.2f}")