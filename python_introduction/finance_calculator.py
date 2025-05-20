#Personal Finance Calculator
# This program calculates the future value of an investment

#enter monthly income
monthly_income = float(input("Enter your monthly income: "))
#enter monthly expenses
monthly_expenses = float(input("Enter your monthly expenses: "))

#calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

#project annual savings for 1 year
interest_rate = 0.05
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (monthly_savings*12 *0.05)

#print the results
print ("your monthly income is: ", monthly_income)
print ("your monthly expenses are: ", monthly_expenses)
print ("your monthly savings are: ", monthly_savings)
print ("Projected savings after one year , with interest is", projected_savings)

