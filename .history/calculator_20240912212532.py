
class Car:  
    def __init__(self, brand, price, down_payment, interest_rate, loan_term):  
        self.brand = brand  
        self.price = price  
        self.down_payment = down_payment  
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal  
        self.loan_term = loan_term  # In years  

    def calculate_loan_amount(self):  
        """Calculates the loan amount after down payment."""  
        return self.price - self.down_payment  

    def calculate_monthly_payment(self):  
        """Calculates the monthly payment using the formula M = P * (r * (1 + r)^n) / ((1 + r)^n - 1).
        Where:
        M = monthly loan payment
        P = principal amount of the loan (purchase price minus down payment)
        r = monthly interest rate (annual interest rate divided by 12)
        n = number of payments (number of months in the loan term)
        """  
        
        loan_amount = self.calculate_loan_amount()  
        monthly_interest_rate = self.interest_rate / 12  # Monthly interest rate  
        number_of_payments = self.loan_term * 12  # Total number of monthly payments  

        if self.interest_rate == 0:  
            return loan_amount / number_of_payments  

        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)  
        return monthly_payment  

    def display_loan_summary(self):  
        """Returns a summary of the loan details."""  
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


def compare_cars(car1, car2):  
    """Compares two car loans and prints their summaries."""  
    summary1 = car1.display_loan_summary()  
    summary2 = car2.display_loan_summary()  

    print(f"\nLoan Summary for {summary1['brand']}:")  
    print(f"Monthly Payment: ${summary1['monthly_payment']:.2f}")  
    print(f"Total Payments: ${summary1['total_payment']:.2f}")  
    print(f"Total Interest Paid: ${summary1['total_interest']:.2f}")  

    print(f"\nLoan Summary for {summary2['brand']}:")  
    print(f"Monthly Payment: ${summary2['monthly_payment']:.2f}")  
    print(f"Total Payments: ${summary2['total_payment']:.2f}")  
    print(f"Total Interest Paid: ${summary2['total_interest']:.2f}")  

    # Comparison  
    if summary1['monthly_payment'] < summary2['monthly_payment']:  
        print(f"\n{summary1['brand']} has a lower monthly payment than {summary2['brand']}.")  
    elif summary1['monthly_payment'] > summary2['monthly_payment']:  
        print(f"\n{summary2['brand']} has a lower monthly payment than {summary1['brand']}.")  
    else:  
        print(f"\nBoth cars have the same monthly payment.")  

    # Additional comparisons can be added here...  

# Example usage  
if __name__ == "__main__":  
    # Input values for the first car  
    print("Enter details for Car Brand 1:")  
    brand1 = input("Brand Name: ")  
    price1 = float(input("Car price: $"))  
    down_payment1 = float(input("Down payment: $"))  
    interest_rate1 = float(input("Interest rate (in %): "))  
    loan_term1 = int(input("Loan term (in years): "))  

    # Create the first Car object  
    car1 = Car(brand1, price1, down_payment1, interest_rate1, loan_term1)  

    # Input values for the second car  
    print("\nEnter details for Car Brand 2:")  
    brand2 = input("Brand Name: ")  
    price2 = float(input("Car price: $"))  
    down_payment2 = float(input("Down payment: $"))  
    interest_rate2 = float(input("Interest rate (in %): "))  
    loan_term2 = int(input("Loan term (in years): "))  

    # Create the second Car object  
    car2 = Car(brand2, price2, down_payment2, interest_rate2, loan_term2)  

    # Compare the two cars  
    compare_cars(car1, car2)