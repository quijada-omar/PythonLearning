
# List

# Different types of data, ordered sequence
values = [1, 2, "Rahul", 4, 5]

print(values[0]) # Prints 1
print(values[3]) # Prints 4
print(values[-1]) # Prints the last index of the list
print(values[1:3]) # Prints 2 and Rahul
values.insert(3, "Shetty") # [0] = 1, [1] = 2, [2] = "Rahul", [3] = "Shetty"
print(values) #
values.append("End")
print(values)

values[2] = "RAHUL"
print(values) # Rahul --> RAHUL
del values[2]  # deletes RAHUL
print(values)

