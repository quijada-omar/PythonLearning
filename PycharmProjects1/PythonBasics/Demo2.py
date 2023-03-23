
# First list created
values = [1, 2, "Rahul", 3, 4]
print(values[0]) # 1
print(values[3]) # 3
print(values[-1]) # 4
print(values[1:3]) # 1-3 no countable
print(values[::-1]) # Reversed list
values.insert(3, "Shetty")  # 1,2,'Rahul', 'Shetty', 3, 4
print(values)
values.append("End") # 1, 2, "Rahul", "Shetty", 3, 4, "End"
print(values)
values[2] = "RAUL"   # 1, 2, "RAUL", "Shetty", 3, 4, "End"
print(values)

del values[0]   # 2, "RAUL", "Shetty", 3, 4, "End"
print(values)