# Mad Libs Game
# Fill in the blanks to create a funny story

print("=" * 40)
print("MAD LIBS GAME")
print("=" * 40)

print("\nPlease provide the following words:")

# Get user inputs
noun1 = input("Enter a noun (person, place, or thing): ")
adjective1 = input("Enter an adjective (describing word): ")
verb1 = input("Enter a verb (action word): ")
noun2 = input("Enter another noun: ")
adjective2 = input("Enter another adjective: ")
verb2 = input("Enter another verb: ")
animal = input("Enter an animal: ")
color = input("Enter a color: ")
number = input("Enter a number: ")

# The story template
story = f"""
========================================
YOUR MAD LIBS STORY
========================================

One day, a {adjective1} {noun1} decided to {verb1} to the park.
When they arrived, they saw a {color} {animal} sitting on a bench.

The {animal} said, "I have {number} {noun2} with me. Would you like to {verb2}?"

So the {adjective1} {noun1} and the {color} {animal} spent the whole day playing together.
It was the most {adjective2} day ever!

The end.
========================================
"""

print(story)