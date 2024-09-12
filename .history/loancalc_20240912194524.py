

class Car:  
    def __init__(self, model, price):  
        self.model = model  
        self.price = price  

    def calculate_loan_payment(self, down_payment, annual_interest_rate, loan_term_years):  
        """  
        Calculates the monthly payment for the car loan.  

        :param down_payment: The down payment made for the car  
        :param annual_interest_rate: The annual interest rate (as a percentage)  
        :param loan_term_years: The term of the loan in years  
        :return: Monthly payment amount  
        """  
        loan_amount = self.price - down_payment  
        monthly_interest_rate = (annual_interest_rate / 100) / 12  
        total_payments = loan_term_years * 12  

        if monthly_interest_rate == 0:  # If the interest rate is 0%  
            monthly_payment = loan_amount / total_payments  
        else:  
            monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)  

        return monthly_payment  


# Example usage  
if __name__ == "__main__":  
    # Create a car object  
    my_car = Car("Toyota Camry", 30000)  

    # Input loan parameters  
    down_payment = 5000  # The down payment  
    annual_interest_rate = 5  # Annual interest rate in percent  
    loan_term_years = 5  # Loan term in years  

    # Calculate monthly payment  
    monthly_payment = my_car.calculate_loan_payment(down_payment, annual_interest_rate, loan_term_years)  

    # Output the result  
    print(f"Monthly payment for {my_car.model}: ${monthly_payment:.2f}")