def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 150:
        raise ValueError("Age cannot be more than 150.")
    print(f"Age set to {age}")

try:
    user_age = int(input("Enter age: "))
    set_age(user_age)
except ValueError as e:
    print(f"Validation error: {e}")