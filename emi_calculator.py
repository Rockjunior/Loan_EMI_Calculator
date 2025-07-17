import math

def calculate_emi(principal, annual_rate, tenure_months):
    # Convert annual interest rate to monthly and percentage to decimal
    monthly_rate = (annual_rate / 12) / 100
    if monthly_rate == 0:
        return principal / tenure_months
    emi = (principal * monthly_rate * math.pow(1 + monthly_rate, tenure_months)) / (math.pow(1 + monthly_rate, tenure_months) - 1)
    return emi

def main():
    print("\n--- Loan EMI Calculator ---\n")
    try:
        principal = float(input("Enter the principal amount (P): "))
        annual_rate = float(input("Enter the annual interest rate (in %): "))
        tenure_months = int(input("Enter the loan tenure (in months): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    emi = calculate_emi(principal, annual_rate, tenure_months)
    print(f"\nFor a loan of {principal:.2f} at {annual_rate:.2f}% annual interest for {tenure_months} months:")
    print(f"Your monthly EMI is: {emi:.2f}\n")

if __name__ == "__main__":
    main() 