# Project 6: Reverse a String
# Flip any input string backwards

print("=" * 35)
print("STRING REVERSER")
print("=" * 35)

# Get input from user
text = input("\nEnter any text to reverse: ")

# Method 1: Using slicing (simplest way)
reversed_text = text[::-1]

# Display results
print("\n" + "=" * 35)
print("RESULT:")
print("=" * 35)
print(f"Original: {text}")
print(f"Reversed: {reversed_text}")

# Check if it's a palindrome (reads same backwards)
if text.lower() == reversed_text.lower() and len(text) > 1:
    print(f"\n Palindrome detected! '{text}' reads the same backwards!")

# Bonus: Show different reversal methods
print("\n" + "=" * 35)
print("BONUS - Different Ways to Reverse:")
print("=" * 35)

# Method 2: Using a loop
loop_reversed = ""
for char in text:
    loop_reversed = char + loop_reversed
print(f"Using loop: {loop_reversed}")

# Method 3: Using reversed() function
function_reversed = ''.join(reversed(text))
print(f"Using reversed(): {function_reversed}")

# Method 4: Show character by character
print(f"\nCharacter by character:")
for i in range(len(text) - 1, -1, -1):
    print(f"Index {i}: {text[i]}")

# Bonus: Reverse words in a sentence
if ' ' in text:
    words = text.split()
    reversed_words = ' '.join(words[::-1])
    print(f"\nWords reversed: {reversed_words}")

print("\n" + "=" * 35)