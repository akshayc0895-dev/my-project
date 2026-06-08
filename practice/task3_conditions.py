age = int(input("Enter your age: "))
has_license = input("Do you have a license? (yes/no)")

if age >=18 and has_license == "yes":
    print("you can drive")
else:
    print("you cannot drive")