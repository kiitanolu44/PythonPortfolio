#  calculate shipping charges for a shopper
# ask the user to enter the amount for their total purchase
# if their total is under $ 50 add $ 10, otherwise shipping is free
# tell the user their final total including shipping costs and format the number so it looks like a monetary value
# dont forget to test your solution with; 
#     - a value > 50
#     - a value < 50
#     - a value of exactly 50

# Declare the variables
totalOrderPrice = 0
shippingCost = 0
valueIncludingShipping = 0

# Ask the user for the order total and convert the answer to a number
totalOrderPrice = float(input("What was the total order for your order? " ))

# Calculate the shipping cost based on the order total
if totalOrderPrice >=50:
    shippingCost = 0
else :
    shippingCost = 10

# Calculate the total order including shipping
valueIncludingShipping = totalOrderPrice + shippingCost

# Print total for user
print("Your final total, including shipping, will be £%.2f " % valueIncludingShipping)