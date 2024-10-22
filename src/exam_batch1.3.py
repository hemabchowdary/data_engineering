count = 0 
num = 18
if num <= 1:
    print(f"{num} is not a prime number")
if num == 2 or num == 3:
    print(f"{num} is a prime number")
for i in range(4, num+1,):
    if num % i == 0:
        count = count+1
    if count == 2:
        print("It is a Prime")
    else:
        print("It is not a prime")


20 - 2,3,5,7,11,13,17,19