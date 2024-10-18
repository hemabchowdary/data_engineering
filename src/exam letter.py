def letter_histogram(word):

histogram = {}

for letter in word:
    if letter in histogram:
        histogram[letter] += 1
    else:
        histogram[letter] = 1
    return histogram
word = input("banana")
result = letter_histogram(word)
print(result)