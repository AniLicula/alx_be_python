# finance_calculator.py

# Prompt the user for their monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Annual interest rate
interest_rate = 0.05

# Project annual savings with interest
annual_savings = monthly_savings * 12 * (1 + interest_rate)

# Display the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings:.2f}.")
