contacts = {}

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Show all contacts")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print(f"Contact {name} added.")

    elif choice == '2':
        name = input("Enter name to search: ")
        phone = contacts.get(name)
        if phone:
            print(f"{name}: {phone}")
        else:
            print("Contact not found.")

    elif choice == '3':
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} deleted.")
        else:
            print("Not found.")

    elif choice == '4':
        if not contacts:
            print("No contacts.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")