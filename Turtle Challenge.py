import turtle


numberOfSides = int(input("How many sides would you like your polygon to have? " ))
secondPolygonRun = input("Would you like a similar scaled polygon inside the original? ").lower()

# This portion creates the 'outer shell' or the larger polygon
for steps in range(numberOfSides):
    turtle.forward(100)
    turtle.right(360/numberOfSides)

# Use pen up and pen down function to indicate to the turtle not to mark this portion of code

turtle.penup()
turtle.right(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(30)
turtle.pendown()

# use same number of sides so a 'scaled' replica polygon of previous polygon is produced within larger shape
if secondPolygonRun == ('yes') :
    for steps in range(numberOfSides):
        turtle.forward(50)
        turtle.right(360/numberOfSides)
    turtle.done()
