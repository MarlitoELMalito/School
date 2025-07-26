# finance_calculators.py

import math

# Display menu
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.")
choice = input(
    "Enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()

# Investment calculator
if choice == "investment":
    deposit = float(input("Enter the amount you are depositing: "))
    interest_rate = float(
        input("Enter the interest rate (as a number, e.g., 8 for 8%): "))
    years = int(input("Enter the number of years you plan to invest: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    r = interest_rate / 100

    if interest_type == "simple":
        total = deposit * (1 + r * years)
    elif interest_type == "compound":
        total = deposit * math.pow((1 + r), years)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        exit()

    print(f"Your investment will be worth: ${total:.2f}")

# Bond calculator
elif choice == "bond":
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(
        input("Enter the annual interest rate (as a number, e.g., 7 for 7%): "))
    months = int(input("Enter the number of months to repay the bond: "))

    i = (interest_rate / 100) / 12
    repayment = (i * present_value) / (1 - (1 + i) ** (-months))

    print(f"Your monthly repayment will be: ${repayment:.2f}")

# Invalid input
else:
    print("Invalid selection. Please enter 'investment' or 'bond'.")
