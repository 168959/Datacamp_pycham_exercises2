"""For a fancy clustering algorithm, you want to find the circumference,C, and area,A, of a circle."""

"When the radius of the circle is r, you can calculate C and A  as:"
"C=2*pi*r"
"A=pi*r2"

"# Definition of radius"
r = 0.43

"# Import the math package"
import math

"# Calculate C"
C = 2 * r * math.pi

"# Calculate A"
A = math.pi * r ** 2

"# Build printout"
print("Circumference: " + str(C))
print("Area: " + str(A))

"Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist."
"You can calculate this as r * phi, where r is the radius and phi is the angle in radians."
"To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported."

"# Definition of radius"
r = 192500

"# Import radians function of math package"
from math import radians

"# Travel distance of Moon over 12 degrees. Store in dist."
dist = r * radians(12)

# Print out dist
print(dist)

"# Create list baseball"
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

"# Import the numpy package as np"
import numpy as np

"# Create a Numpy array from baseball: np_baseball"
np_baseball = np.array(baseball)

"# Print out type of np_baseball"
print(type(np_baseball))

"# height is available as a regular list"

"# Import numpy"
import numpy as np

"# Create a numpy array from height_in: np_height_in"
np_height_in = np.array(height_in)

"# Print out np_height_in"
print(np_height_in)

"# Convert np_height_in to m: np_height_m"
np_height_m = np_height_in * 0.0254

"# Print np_height_m"
print(np_height_m)

"# height and weight are available as regular lists"

"# Import numpy"
import numpy as np

"# Create array from height_in with metric units: np_height_m"
np_height_m = np.array(height_in) * 0.0254

"# Create array from weight_lb with metric units: np_weight_kg"
np_weight_kg = np.array(weight_lb) * 0.453592

"# Calculate the BMI: bmi"
bmi = np_weight_kg / np_height_m ** 2

"# Print out bmi"
print(bmi)

"# height and weight are available as a regular lists"

"# Import numpy"
import numpy as np

"# Calculate the BMI: bmi"
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

"# Create the light array"
light = bmi < 21

"# Print out light"
print(light)

"# Print out BMIs of all baseball players whose BMI is below 21"
print(bmi[light])

# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])