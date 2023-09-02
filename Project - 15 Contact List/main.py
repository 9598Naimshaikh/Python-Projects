# Question: Contact List
# Create a Python program that simulates a simple contact list. The program should allow users to perform the following actions:

# 1.Add a new contact with a name and phone number.
# 2.Search for a contact by name and display their phone number.
# 3.Display all contacts in the list.
# 4.Your program should utilize a dictionary to represent the contacts, where names are keys and phone numbers are values.


def add_contact(Contacts):
    user_name = input("Enter contact name: ").capitalize()
    user_number = int(input("Enter contact number: "))
    Contacts[user_name] = user_number
    print(f"Contact '{user_name}' added.")


def search_contacts(Contacts):
    name = input("Enter contacts name to search: ").capitalize()
    if name in Contacts:
        print(f"Phone number for {name!r}: {Contacts[name]}")
    else:
        print(f"Contacts {name!r} not found.!")


def display_contact(Contacts):
    print("Contacts Lists: ")
    for name, phone in Contacts.items():
        print(f"Name: {name}, Phone: {phone}")


def main():
    Contacts = {}
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact(Contacts)
        elif choice == 2:
            search_contacts(Contacts)
        elif choice == 3:
            display_contact(Contacts)
        elif choice == 4:
            print("Thanks for exit program..!")
            break
        else:
            print("Invalid choice please enter valid choice...")


main()
