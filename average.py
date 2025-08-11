# ask user to input the lenght of a three sides of a triangle

side1 = float(input("Enter the length of side 1: \n"))
side2 = float(input("Enter the length of side 2: \n"))
side3 = float(input("Enter the length of side 3: \n"))

# if all sides are equal, print equilateral
# if two sides are equal, print isosceles
# if no sides are equal, print scalene
if side1 == side2 and side2 == side3:
    print ("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print ("The triangle is isosceles.")
else:
    print ("The triangle is scalene.")