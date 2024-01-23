# pseudocode

# Enter word
word = input("Please enter your chosen word: ")

# Print word
print("The word you've chosen is:", word)

# Get the lenght of the string
size = len(word)

# Print even index characters
for i in range(0, size, 2):
    print(word[i])