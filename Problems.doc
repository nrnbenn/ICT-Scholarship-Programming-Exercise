#8. Carpet Calculation
length = float(input("What is the length of the room: "))
width = float(input("What is the width of the room: "))
costRate = 20 #per unit of measurment squared

area = length*width
cost = area*costRate

print(f"Area: {area}")
print(f"Cost: £{cost}")


#9. Paint Calculation
def roundup(n):
    return(n + (1 - (n % 1)))

length = float(input("What is the length of the room: "))
width = float(input("What is the width of the room: "))
height = float(input("What is the height of the room: "))

#find the area of the walls
totalArea = 0
totalArea += 2*(length*height)
totalArea += 2*(width*height)

pots = roundup(totalArea/10)

print(f"Area to be painted: {totalArea}")
print(f"Pots required: {pots}")
