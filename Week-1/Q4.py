# Program to check if a string is a palindrome

# Take input from the user
text = input("Enter a word or phrase: ")

# Remove spaces and convert to lowercase
cleaned_text = text.replace(" ", "").lower()

# Check if it reads the same backward
if cleaned_text == cleaned_text[::-1]:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")

