contacts = {}  # Dictionary to store contact information

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }

    print(f"\nContact '{name}' added successfully.")

def view_contact_list():
    print("\n********** Contact List **********")
    for name, contact_info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone Number: {contact_info['phone_number']}")
        print(f"Email: {contact_info['email']}")
        print(f"Address: {contact_info['address']}")
        print("------------------------")

def search_contact():
    query = input("Enter name or phone number to search: ").lower()
    found_contacts = []

    for name, contact_info in contacts.items():
        if query in name.lower() or query in contact_info['phone_number']:
            found_contacts.append((name, contact_info))

    if found_contacts:
        print("\n********** Search Results **********")
        for name, contact_info in found_contacts:
            print(f"Name: {name}")
            print(f"Phone Number: {contact_info['phone_number']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            print("------------------------")
    else:
        print("No matching contacts found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    
    if name in contacts:
        print(f"\nUpdate Contact '{name}':")
        phone_number = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email address (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")

        if phone_number:
            contacts[name]['phone_number'] = phone_number
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address

        print(f"\nContact '{name}' updated successfully.")
    else:
        print(f"No contact found with the name '{name}'.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
