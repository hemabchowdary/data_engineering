def letter_histogram(word):
    out = {}
    for letter in word:
        if letter in out:
            out[letter]+=1
        else:
            out[letter] = 1
    return out

word = "banana"
print(f"The Result of letter histogram  for a given word is {letter_histogram(word)}")