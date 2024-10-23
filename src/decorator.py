import functools

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
     
        result = func(*args, **kwargs)
       
        print(f"Return value: {result}")
        
        return result
    return wrapper

@log_function_call
def factorial(n):
    """Returns the factorial of the given number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)
