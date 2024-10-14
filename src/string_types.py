x = [29, 38, 49, 56, 61]
big_number = max(x)
small_number = min(x)
print(big_number)
print(small_number)

x.sort(reverse=True)
print(x)

y = sum(x)
print(y)

strings = ["welcome", "to",  "programming", "language", "in", "data", "engineering" , " in", "databricks"]
a = [s.upper() for s in strings]
print(a)

longest_string = max(strings, key=len)
shortest_string = min(strings, key=len)
print(longest_string)
print(shortest_string)

c = '-'.join(strings)
print(c)

student_list = {'hema': 91, 'bhargav': 98 , 'veda': 56, 'maitri': 69, 'siva': 55}
highest = max(student_list, key=student_list.get)
highest_score = student_list[highest]
lowest = min(student_list, key=student_list.get)
lowest_score =student_list[lowest]
print(f"{highest} :{highest_score}")
print(f"{lowest} :{lowest_score}")

student_list = {'hema': 91, 'bhargav': 98 , 'veda': 56, 'maitri': 69, 'siva': 55}
student_list['jai'] = 49
print(student_list)

if 'siva' in student_list:
    del student_list['bhargav']
print(student_list)
