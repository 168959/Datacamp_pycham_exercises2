# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

"# Print out second element from areas"
print(areas[1])

"# Print out last element from areas"
print(areas[9])

"# Print out the area of the living room"
print(areas[5])

"# Create the areas list"
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

"# Sum of kitchen and bedroom area: eat_sleep_area"
eat_sleep_area = areas[3] + areas[-3]

"# Print the variable eat_sleep_area"
print(eat_sleep_area)

"#Subset and calculate"
"# Create the areas list"
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

"# Sum of kitchen and bedroom area: eat_sleep_area"
eat_sleep_area = areas[3] + areas[-3]

"# Print the variable eat_sleep_area"
print(eat_sleep_area)

"#Slicing and dicing"

"# Create the areas list"
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

"# Use slicing to create downstairs"
downstairs = areas[0:6]

"# Use slicing to create upstairs"
upstairs = areas[6:10]

"# Print out downstairs and upstairs"
print(downstairs)
print(upstairs)

"# Alternative slicing to create downstairs"
downstairs = areas[:6]

"# Alternative slicing to create upstairs"
upstairs = areas[-4:]

"#Replace list elements"
"# Create the areas list"
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

"# Correct the bathroom area"
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

"#Extend a list"
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

"# Add poolhouse data to areas, new list is areas_1"
areas_1 = areas + ["poolhouse", 24.5]
"# Add garage data to areas_1, new list is areas_2"
areas_2 = areas_1 + ["garage", 15.45]

"#Inner workings of lists"

"# Create list areas"
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

"# Create areas_copy"
areas_copy = list(areas)

"# Change areas_copy"
areas_copy[0] = 5.0

"# Print areas"
print(areas)
