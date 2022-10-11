# Calculate the total to charge for an order from an online store in canada
# ask user what country they are from and their total
# if the user is from canada ask which province
# if the order is from outside canada do not charge any taxes
# if the order was placed in canada calculate tax based on the province

# Alberta - 0.05% general sales tax [GST]
# Ontario, New Brunswick, Nova Scotia - 0.13% Harmonized Sales Tax [HST]
# All other provinces charge 0.06% PST + 0.05 GST tax

# Declare & initilize the variables

from ctypes.wintypes import HSTR
from itertools import count


country = ""
province = ""
orderTotal = 0
totalWithTax = 0

# I am declaring variables to hold the tax values used in the calculations
# This way if a tax rate was to ever fluctuate or change I only have to change it in one place
# Instead of searching through the whole code to update in every part of the code.

GST = .05
HST = .13
PST = .06

# Ask the user what country they are from
country = input("What country are you from? " )

# if canada proceed to province
if country.lower() == "canada" :
    province = input("Which Province do you reside? ")

# Ask for the order total
orderTotal = float(input("What is your order total? "))

# Add taxes
# Check if they are from Canada
if country.lower() == 'canada' :
    # If they are from canada, we must change the calculation based on the province they specified
    if province.lower() == "alberta" :
        orderTotal = orderTotal + orderTotal * GST
    elif province.lower() == "ontario" or \
        province.lower == "new brunswick" or \
            province.lower() == "nova scotia" :
        orderTotal = orderTotal + orderTotal * HST
    
    else :
        orderTotal = orderTotal + orderTotal * PST + orderTotal * GST

# if they are not from canada there is no tax, so the amount the entered is the total with tax

# display the total with taxes to the user, dont forget to format the number
print("Your total including taxes comes to £%.2f " % orderTotal)

