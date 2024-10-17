def factorial(n):
    result = 1
    for i in range(1, n + 1):  # Loop from 1 to n
        result *= i
    return result


num = int(input("Enter a number to calculate its factorial: "))
print(f"Factorial of {num} is {factorial(num)}")
