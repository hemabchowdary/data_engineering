def separate_and_sums(lista):
    even_list = [num for num in lista if num % 2 == 0]
    odd_list = [num for num in lista if num % 2 != 0]

    even_sum = sum(even_list)
    odd_sum = sum(odd_list)

    if even_sum >= odd_sum:
        return even_list, even_sum
    else:
        return odd_list, odd_sum      

lista = [1,2,3,4,5,6,7,8]
print(f"The Result of the Separate and Sums for a given list is {separate_and_sums(lista)}")