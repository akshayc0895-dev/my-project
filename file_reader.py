filename = input("Enter filename to read: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("\nFile content:")
        print(content)
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    create = input("Create it with default content? (y/n): ").lower()
    if create == 'y':
        with open(filename, "w") as f:
            f.write("Default content.\nThis file was created automatically.")
        print(f"'{filename}' created. Run again to read.")
    else:
        print("Exiting.")
except PermissionError:
    print("Permission denied to read the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File reader finished.")