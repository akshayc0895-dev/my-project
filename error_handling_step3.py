# Step 4: TypeError handling

def add_numbers(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        return f"Error: Cannot add {type(a).__name__} and {type(b).__name__}"

# Test cases
print(add_numbers(10, 5))        # Works: 15
print(add_numbers(10, "5"))      # Error: different types
print(add_numbers("hello", "world"))  # Works: helloworld