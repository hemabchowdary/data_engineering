num = int(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Taking score input and checking if it's greater than 90
score = int(input("Enter your score: "))

if score > 90:
    print("The score is greater than 90.")
else:
    print("The score is 90 or less.")