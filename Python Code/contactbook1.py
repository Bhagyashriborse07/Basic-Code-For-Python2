contact = {}

def display_contact():
    print("Name\t\tContact number")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))

while True:
    choice = int(input("\n1. Add new contact \n2. Search contact \n3. Display contacts \n4. Edit contact \n5. Delete contact \n6. Exit \nEnter your choice: "))

    if choice == 1:
        name = input("Enter contact name: ")
        phone = input("Enter the mobile number: ")
        contact[name] = phone
        print("Contact added successfully!")

    elif choice == 2:
        search_name = input("Enter the contact name to search: ")
        if search_name in contact:
            print(search_name, "'s contact number is", contact[search_name])
        else:
            print("Name not found in contact book.")

    elif choice == 3:
        if not contact:
            print("Empty contact book.")
        else:
            display_contact()

    elif choice == 4:
        edit_contact = input("Enter the contact name to edit: ")
        if edit_contact in contact:
            phone = input("Enter new mobile number: ")
            contact[edit_contact] = phone
            print("Contact updated successfully!")
            display_contact()
        else:
            print("Name not found in contact book.")

    elif choice == 5:
        del_contact = input("Enter the contact name to delete: ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact? (Y/N): ")
            if confirm.upper() == 'Y':
                contact.pop(del_contact)
                print("Contact deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("Name not found in contact book.")

    elif choice == 6:
        print("Exiting contact book. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")