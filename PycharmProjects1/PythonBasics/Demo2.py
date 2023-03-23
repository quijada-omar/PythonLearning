values = [1, 2, "Rahul", 3, 4]
print(values[0])
print(values[3])
print(values[-1])
print(values[1:3])
print(values[::-1])
values.insert(3, "Shetty")
print(values)
values.append("End")
print(values)
values[2] = "RAUL"
print(values)

del values[0]
print(values)