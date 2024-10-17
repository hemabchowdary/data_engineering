# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage
num = int(input("Enter a number to calculate its factorial: "))
print(f"Factorial of {num} is {factorial(num)}")
