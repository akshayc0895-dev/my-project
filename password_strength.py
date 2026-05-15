# Password Strength Checker

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make password at least 8 characters long.")
    
    # Digit check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include at least one digit.")
    
    # Uppercase check
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    # Lowercase check
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    # Special character check
    special = "!@#$%^&*()_+-=[]{};':,./<>?\\|`~"
    if any(char in special for char in password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$% etc.).")
    
    return score, feedback

# Main program
print("=" * 40)
print("PASSWORD STRENGTH CHECKER")
print("=" * 40)

password = input("Enter a password: ")

score, feedback = check_password_strength(password)

print("\n" + "=" * 40)
print("RESULT")
print("=" * 40)
print(f"Password: {password}")
print(f"Score: {score}/5")

if score == 5:
    print("Strength: Very Strong")
elif score == 4:
    print("Strength: Strong")
elif score == 3:
    print("Strength: Medium")
elif score == 2:
    print("Strength: Weak")
else:
    print("Strength: Very Weak")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print(f" - {item}")

print("=" * 40)