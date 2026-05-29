shopping_list = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Display list")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"'{item}' added.")

    elif choice == '2':
        if len(shopping_list) == 0:
            print("Nothing to remove.")
        else:
            print("\nCurrent list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
            try:
                num = int(input("Enter number to remove: "))
                removed = shopping_list.pop(num - 1)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Invalid number.")

    elif choice == '3':
        if len(shopping_list) == 0:
            print("Shopping list is empty.")
        else:
            print("\nShopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")