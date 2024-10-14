def sum_using_for_loop(n):
    return sum(range(1, n+1))


def sum_using_list_comprehension(n):
    return sum(i for i in range(1, n+1))


def sum_using_formula(n):
    return (n * (n + 1)) // 2


def main():
    n = int(input("Enter the value of n: "))

  
    print(f"Sum using for loop for first {n} numbers: {sum_using_for_loop(n)}")
    
   
    print(f"Sum using list comprehension for first {n} numbers: {sum_using_list_comprehension(n)}")
    
   
    print(f"Sum using formula for first {n} numbers: {sum_using_formula(n)}")

# Run the main function
main()