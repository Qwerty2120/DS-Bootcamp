# Program to count vowels in a word

# Take input from the user
word = input("Enter a word: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize count
count = 0

# Loop through each character in the word
for char in word:
    if char in vowels:
        count += 1

# Print the result
print("Number of vowels:", count)
