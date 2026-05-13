# Project 7: Count Vowels
# Count vowels in a sentence

print("=" * 35)
print("VOWEL COUNTER")
print("=" * 35)

# Get input from user
text = input("\nEnter a sentence or word: ")

# Convert to lowercase so we count both uppercase and lowercase vowels
text_lower = text.lower()

# Define vowels
vowels = 'aeiou'

# Method 1: Count using a loop
vowel_count = 0
for char in text_lower:
    if char in vowels:
        vowel_count += 1

# Display result
print("\n" + "=" * 35)
print("RESULTS:")
print("=" * 35)
print(f"Original text: {text}")
print(f"Total vowels: {vowel_count}")

# Bonus: Show count for each vowel
print("\n" + "-" * 35)
print("BREAKDOWN BY VOWEL:")
print("-" * 35)

count_a = text_lower.count('a')
count_e = text_lower.count('e')
count_i = text_lower.count('i')
count_o = text_lower.count('o')
count_u = text_lower.count('u')

print(f"A / a : {count_a}")
print(f"E / e : {count_e}")
print(f"I / i : {count_i}")
print(f"O / o : {count_o}")
print(f"U / u : {count_u}")

# Bonus 2: Count consonants
consonants = 0
for char in text_lower:
    if char.isalpha() and char not in vowels:
        consonants += 1

print("\n" + "-" * 35)
print(f"Consonants: {consonants}")
print(f"Total letters: {vowel_count + consonants}")

# Bonus 3: Show positions of vowels
print("\n" + "-" * 35)
print("VOWEL POSITIONS:")
print("-" * 35)

for i, char in enumerate(text):
    if char.lower() in vowels:
        print(f"Position {i}: '{char}'")

# Bonus 4: Percentage of vowels
if len(text.replace(" ", "")) > 0:
    total_letters = vowel_count + consonants
    vowel_percentage = (vowel_count / total_letters) * 100
    print(f"\nVowels make up {vowel_percentage:.1f}% of the letters")

print("\n" + "=" * 35)
