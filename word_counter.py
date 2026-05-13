# Project 11: Word Counter
# Count words in a sentence

print("=" * 40)
print("WORD COUNTER")
print("=" * 40)

# Get sentence from user
sentence = input("\nEnter a sentence: ")

# Method 1: Using split() - simplest way
words_list = sentence.split()
word_count = len(words_list)

print("\n" + "=" * 40)
print("RESULTS:")
print("=" * 40)
print(f"Original sentence: {sentence}")
print(f"Word count: {word_count}")