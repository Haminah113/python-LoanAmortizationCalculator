# This program will help you calculate the monthly payments on a loan
# and show you how much of each payment goes towards the principal and interest.

# First, we need to ask the user for some information about the loan.
# We'll ask for the loan amount, the interest rate, and the number of years for the loan.

loan_amount = float(input("How much is the loan amount? "))
interest_rate = float(input("What is the annual interest rate (as a decimal)? "))
loan_length = int(input("How many years is the loan for? "))

# Next, we'll calculate some values that we'll need for the calculations.
# We'll calculate the number of months for the loan and the monthly interest rate.

num_months = loan_length * 12
monthly_interest_rate = interest_rate / 12

# Now, we'll use a formula to calculate the monthly payment amount.
# The formula is: P = (PV * r) / (1 - (1 + r)^-n)
# Where P is the monthly payment, PV is the loan amount, r is the monthly interest rate,
# and n is the number of months for the loan.

payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-num_months))

# Finally, we'll loop through each month of the loan and calculate how much of each payment
# goes towards the principal and how much goes towards the interest.

remaining_balance = loan_amount

for i in range(num_months):
    interest = remaining_balance * monthly_interest_rate
    principal = payment - interest
    remaining_balance -= principal
    
    # Print out the details for each month's payment
    print("Month {}: payment = {:.2f}, interest = {:.2f}, principal = {:.2f}, remaining balance = {:.2f}"
          .format(i+1, payment, interest, principal, remaining_balance))
