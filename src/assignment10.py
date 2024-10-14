um = int(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Taking score input and checking its range
score = int(input("Enter your score: "))

if score > 90:
    print("The score is greater than 90.")
elif 80 <= score <= 89:
    print("The score is between 80 and 89.")
elif 70 <= score <= 79:
    print("The score is 70 or between 71 and 79.")
else:
    print("The score is less than 70.")
    