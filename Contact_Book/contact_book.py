class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.\n")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"Contact {i}:\n{contact}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found.\n")
        else:
            for i, contact in enumerate(found_contacts, start=1):
                print(f"Found Contact {i}:\n{contact}")

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print("Contact found. Enter new details:")
                contact.name = input("Name: ")
                contact.phone = input("Phone: ")
                contact.email = input("Email: ")
                contact.address = input("Address: ")
                print("Contact updated successfully.\n")
                return
        print("Contact not found.\n")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully.\n")
                return
        print("Contact not found.\n")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            contact_book.update_contact(search_term)
        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
