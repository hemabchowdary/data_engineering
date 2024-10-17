def is_palindrome(s):
    
    s = str(s)
    return s == s[::-1]

# Example usage
value = input("Enter a string or number to check for palindrome: ")
if is_palindrome(value):
    print(f"'{value}' is a palindrome!")
else:
    print(f"'{value}' is not a palindrome.")
