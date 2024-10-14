# Initial list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 1, 3, 2, 5]

# Append a new number to the list
new_number = 7  
numbers.append(new_number)
print("After appending:", numbers)

# Remove the newly appended number from the list
numbers.remove(new_number)
print("After removing the new number:", numbers)

# Sort the list in descending order
numbers.sort(reverse=True)
print("Sorted in descending order:", numbers)

# Insert a number between 1 and 4
insert_number = 8  
index = numbers.index(4)  
numbers.insert(index + 1, insert_number)
print("After inserting between 1 and 4:", numbers)
