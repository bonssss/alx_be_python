def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            
            # Prompt for and add an item
            item_add = input("Enter the item to add: ")
            shopping_list.append(item_add)
            
            # pass
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Enter the item to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
            else:
                print(f"Item '{remove_item}' not found in the list.")
            # pass
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()