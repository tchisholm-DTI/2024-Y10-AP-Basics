# Ask the user for the width and height
# (assume they put in valid data)
width = float(input("Width: "))
height = float(input("Height: "))

# Calculate the area/perimeter
area = width * height
perimeter = 2 * (width + height)

# Output the area and perimeter
print()
print(f"Area is: {area} square units")
print(f"Perimeter: {perimeter} units")
