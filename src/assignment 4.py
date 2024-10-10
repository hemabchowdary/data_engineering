# Given tuple
t = (25, 45, 85, 7.5, 3.67, True, "greetings", False, "from", "Python4")
x = t[1]  # Access the 2nd element (index 1)
print(x)

# Slice the tuple to retrieve the last 4 elements
y = t[-4:]
print(y)

# Finding the index of a particular element
index_value = t.index(3.67)
print(index_value)

# Count how many times an element is repeated
count_value = t.count(85)
print(count_value)

# Add two elements to the existing tuple
a = t + (500, 600)
print(a)

# Convert tuple to list, add multiple elements, and convert back to tuple
x = list(t)
x.extend([400, 700])  # Add two elements
y = tuple(x)
print(y)

# Remove an element from a tuple by converting it to a list
x = list(t)
x.remove(85)  # Remove the element with value 85 directly
y = tuple(x)
print(y)

# Pack a tuple
countries = ("Japan", "Brazil", "Canada")

# Unpack the tuple
(Japanese, Portuguese, English) = countries
print(Japanese)
print(Portuguese)
print(English)

# Using set operations
k = {10, 20, 30, 40, 50}
j = {40, 50, 60, 70, 80}
print(k.union(j))  # Union
print(k.intersection(j))  # Intersection
print(k.difference(j))  # Difference
print(k.symmetric_difference(j))  

# Create a list, remove duplicates, and perform add/remove operations
l = [15, 12, 10, 12, 8, 15, 7, 10, 6, 5, 4, 7, 3, 2, 1]
m = list(set(l))  # Remove duplicates
print(m)

# Remove an element and add another
l.remove(12)  # Removes the first occurrence of 12
l.append(18)  # Adds 18 to the list
print(l)
