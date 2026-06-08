# Step 5: FileNotFoundError handling

filename = input("Enter filename to read: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print(f"Content:\n{content}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    create = input("Create it? (y/n): ").lower()
    if create == 'y':
        with open(filename, "w") as f:
            f.write("This file was created automatically.\n")
        print(f"'{filename}' created. Run again to read.")