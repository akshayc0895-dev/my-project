# Project 14: Palindrome Checker
# Check if a word reads the same backwards

print("=" * 40)
print("PALINDROME CHECKER")
print("=" * 40)

word = input("Enter a word or phrase: ")

# Remove spaces and convert to lowercase
clean_word = word.replace(" ", "").lower()

# Reverse the string
reversed_word = clean_word[::-1]

print("\n" + "=" * 40)
print("RESULTS")
print("=" * 40)
print(f"Original: {word}")
print(f"Reversed: {reversed_word}")

if clean_word == reversed_word:
    print("Result: This IS a palindrome.")
else:
    print("Result: This is NOT a palindrome.")

print("=" * 40)