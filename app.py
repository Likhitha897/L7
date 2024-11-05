# app.py
from models import add_flavor, get_all_flavors

def main():
    print("Chocolate House Management")
    print("1. Add Flavor")
    print("2. List Flavors")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter flavor name: ")
        season = input("Enter season (e.g., Winter, Summer): ")
        add_flavor(name, season)
        print("Flavor added successfully!")
    elif choice == "2":
        flavors = get_all_flavors()
        for flavor in flavors:
            print(f"{flavor[1]} - {flavor[2]}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
