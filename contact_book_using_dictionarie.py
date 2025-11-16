import sys

def display_menu():
    """Prints the main menu options to the console."""
    print("\n--- Contact Book Menu ---")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. List all contacts")
    print("4. Exit")
    print("-------------------------")

def add_contact(book):
    """
    Prompts the user for contact details and adds them to the book.
    Performs input validation.
    """
    print("\n[Add New Contact]")
    
    # --- Input Validation for Name ---
    while True:
        name = input("Enter name: ").strip()
        if not name:
            print("Error: Name cannot be empty. Please try again.")
        elif name in book:
            print(f"Error: Contact '{name}' already exists.")
        else:
            break
            
    # --- Input Validation for Phone ---
    while True:
        phone = input("Enter phone number: ").strip()
        if not phone:
            print("Error: Phone number cannot be empty. Please try again.")
        else:
            break

    # --- Input Validation for Email ---
    while True:
        email = input("Enter email: ").strip()
        if "@" not in email or "." not in email:
            print("Error: Invalid email format. Must include '@' and '.'.")
        else:
            break

    # Add the new contact (a nested dictionary) to the main book
    book[name] = {"phone": phone, "email": email}
    print(f"\nSuccess: Contact '{name}' added.")

def search_contact(book):
    """Searches for a contact by name and displays details if found."""
    print("\n[Search Contact]")
    name = input("Enter name to search for: ").strip()

    if name in book:
        # Retrieve the nested dictionary of details
        details = book[name]
        print("\n--- Contact Found ---")
        print(f"Name:  {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print("---------------------")
    else:
        print(f"\nError: Contact '{name}' not found.")

def list_all_contacts(book):
    """Displays all contacts currently in the book."""
    print("\n[All Contacts]")
    
    # --- Validation for Empty Book ---
    if not book:
        print("Your contact book is empty.")
        return

    # Loop through the .items() of the dictionary
    for name, details in book.items():
        print("---------------------")
        print(f"Name:  {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    print("---------------------")

def main():
    """The main function to run the contact book application."""
    
    # The main data structure: a dictionary
    contact_book = {}

    while True:
        display_menu()
        
        # --- Input Validation for Menu Choice ---
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            search_contact(contact_book)
        elif choice == '3':
            list_all_contacts(contact_book)
        elif choice == '4':
            print("\nExiting contact book. Goodbye!")
            sys.exit() # Cleanly exits the program
        else:
            print("\nError: Invalid choice. Please enter a number from 1 to 4.")

# Standard Python boilerplate to run the main() function
if __name__ == "__main__":
    main()