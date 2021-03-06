"# Definition of countries and capital"
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

"# Get index of "
germany': ind_ger"
ind_ger = countries.index('germany')

"# Use ind_ger to print out capital of Germany"
print(capitals[ind_ger])

"# Definition of countries and capital"
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

"# From string in countries and capitals, create dictionary europe"
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

"# Print europe"
print(europe)

"# Definition of dictionary"
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

"# Print out the keys in europe"
print(europe.keys())

"# Print out value that belongs to key 'norway'"
print(europe['norway'])

'# Definition of dictionary'
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

'# Update capital of germany'
europe['germany'] = 'berlin'

'# Remove australia'
del(europe['australia'])

'# Print europe'
print(europe)

'# Dictionary of dictionaries'
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


'# Print out the capital of France'
print(europe['france']['capital'])

'# Create sub-dictionary data'
data = { 'capital':'rome', 'population':59.83 }

"# Add data to europe under key 'italy'"
europe['italy'] = data

"# Print europe"
print(europe)
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

"# Import pandas as pd"
import pandas as pd

"# Create dictionary my_dict with three key:value pairs: my_dict"
my_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }

"# Build a DataFrame cars from my_dict: cars"
cars = pd.DataFrame(my_dict)

"# Print cars"
print(cars)

"# Pre-defined lists"
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

"# Import pandas as pd"
import pandas as pd

"# Create dictionary my_dict with three key:value pairs: my_dict"
my_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }

"# Build a DataFrame cars from my_dict: cars"
cars = pd.DataFrame(my_dict)

"# Print cars"
print(cars)
import pandas as pd

"# Build cars DataFrame"
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

"# Definition of row_labels"
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

"# Specify row labels of cars"
cars.index = row_labels

"# Print cars again"
print(cars)

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)
  Unnamed: 0  cars_per_cap        country  drives_right
0         US           809  United States          True
1        AUS           731      Australia         False
2        JPN           588          Japan         False
3         IN            18          India         False
4         RU           200         Russia          True
5        MOR            70        Morocco          True
6         EG            45          Egypt          True

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)
