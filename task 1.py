print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, \n\ttwinkle, little star, \n\t\tHow I wonder what you are!")
import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)
import datetime
now = datetime.datetime.now()
print("date and time:")
print(now.strftime("%Y/%m/%d - %H.%M.%S"))
"Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are!"
# Import the 'pi' constant from the 'math' module to calculate the area of a circle
from math import pi

# Prompt the user to input the radius of the circle
r = float(input("Input the radius of the circle : "))

# Calculate the area of the circle using the formula: area = π * r^2
area = pi * r ** 2

# Display the result, including the radius and calculated area
print("The area of the circle with radius " + str(r) + " is: " + str(area))
ln = input("Write last name:")
fn = input("Write first name:")
print("Hello" + ln + "" + fn)