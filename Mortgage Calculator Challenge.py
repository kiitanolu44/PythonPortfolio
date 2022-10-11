# Formula for mortgage calculator
# M = L(I(1 + I)*N) / ((1 + I)*N - 1)
# M = Monthly Payment, L = Loan, I = Interest, N = Number of payments, ** = exponent

# Declares and asks for user to input loan amount. 
# Then converts to float
loanAmount = input('Enter loan amount \n')
loanAmount = float(loanAmount)

# Declares and asks user to input number of payments in years. 
# Then converts to float.
#  Years * 12 to get total number of months
years = input('How many years will you have the loan? \n')
years = float(years) * 12

# Declares and asks user to input interest rate. 
# Then converts to float 
# and input interest rate is /100/12
interestRate = input('Enter Interest Rate \n')
interestRate = float(interestRate) / 100 / 12

# Formula to calculate monthly payments
mortgagePayment = loanAmount * (interestRate * (1 + interestRate)
                                ** years) / ((1 + interestRate) ** years - 1)

# Prints monthly payment on next line and reformat the string to a float using 2 decimal places
print("The monthly mortgage payment is\n (%.2f) " % mortgagePayment)