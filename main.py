# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print(areas[-3])

print(areas[0:-1])

#Subset and calculate
x = ["a", "b", "c", "d"]
print(x[1] + x[3])

#Slicing and dicing

x = ["a", "b", "c", "d"]
var = x[:2]
x[2:]
x[:]

#Subsetting lists of lists

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]

# Replace list elements
x = ["a", "b", "c", "d"]
x[1]= "r"
x[2:] ["s","t"]

#Extend a list
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]

#Delete list elements
x = ["a", "b", "c", "d"]
del(x[1])

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
del(areas[-4:-2])



