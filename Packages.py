"""For a fancy clustering algorithm, you want to find the circumference,C, and area,A, of a circle."""
from typing import List

"from numpy.core._multiarray_umath import ndarray"

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
baseball: List[int] = [180, 215, 210, 210, 188, 176, 209, 200]

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
height_in = ([1.73, 1.68, 1.71, 1.89, 1.79])

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
weight_lb = ([65.4, 59.2, 63.6, 88.4, 68.7])

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

"# height and weight are available as a regular lists"

"# Import numpy"
import numpy as np

"# Store weight and height lists as numpy arrays"
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

"# Print out the weight at index 50"
print(np_weight_lb[50])

"# Print out sub-array of np_height_in: index 100 up to and including index 110"
print(np_height_in[100:111])


"# Create baseball, a list of lists"
baseball = [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]

"# Import numpy"
import numpy as np

'# Create a 2D numpy array from baseball: np_baseball'
np_baseball = np.array(baseball)

"# Print out the type of np_baseball"
print(type(np_baseball))

"# Print out the shape of np_baseball"
print(np_baseball.shape)

"# baseball is available as a regular list of lists"

"# Import numpy package"
import numpy as np

"# Create a 2D numpy array from baseball: np_baseball"
np_baseball = np.array(baseball)

"# Print out the shape of np_baseball"
print(np_baseball.shape)

"# baseball is available as a regular list of lists"

"# Import numpy package"
import numpy as np

"# Create np_baseball (2 cols)"
np_baseball = np.array(baseball)

"# Print out the 50th row of np_baseball"
print(np_baseball[49, :])

"# Select the entire second column of np_baseball: np_weight_lb"
np_weight_lb = np_baseball[:, 1]

"# Print out height of 124th player"
print(np_baseball[123, 0])

"# baseball is available as a regular list of lists"
# updated is available as 2D numpy array

"# Import numpy package"
import numpy as np

"# Create np_baseball (3 cols)"
np_baseball = np.array(baseball)

"# Print out addition of np_baseball and updated"


def updated(args):
    pass


print(np_baseball + updated)

"# Create numpy array: conversion"
conversion = np.array([0.0254, 0.453592, 1])

"# Print out product of np_baseball and conversion"
print(np_baseball * conversion)

"# np_baseball is available"

"# Import numpy"
import numpy as np

"# Create np_height_in from np_baseball"
np_height_in = np_baseball[:,0]

"# Print out the mean of np_height_in"
print(np.mean(np_height_in))

"# Print out the median of np_height_in"
print(np.median(np_height_in))

# np_baseball is available

# Import numpy
import numpy as np

"# Print mean height (first column)"
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

"# Print median height. Replace 'None'"
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

"# Print out the standard deviation on height. Replace 'None'"
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

"# Print out correlation between first and second column. Replace 'None'"
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))

"# heights and positions are available as lists"

"# Import numpy"
import numpy as np

"# Convert positions and heights to numpy arrays: np_positions, np_heights"
np_positions = np.array(positions)
np_heights = np.array(heights)

"# Heights of the goalkeepers: gk_heights"
gk_heights = np_heights[np_positions == 'GK']

"# Heights of the other players: other_heights"
other_heights = np_heights[np_positions != 'GK']

"# Print out the median height of goalkeepers. Replace 'None'"
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

"# Print out the median height of other players. Replace 'None'"
print("Median height of other players: " + str(np.median(other_heights)))