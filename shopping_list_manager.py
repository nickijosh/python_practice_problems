# shopping_list_manager.py

# This function displays the menu options
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# This is the main function where the logic runs
def main():
    shopping_list = []  # Initialize an empty list to hold shopping items

    while True:
        display_menu()  # Show the menu
        choice = input("Enter your choice: ")  # Get user input

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)  # Add item to the list
            print(f"'{item}' has been added to your shopping list.")

        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove item if it exists
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")

        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("Your shopping list:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")

        elif choice == '4':
            print("Goodbye!")
            break  # Exit the loop and program

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# This line ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
