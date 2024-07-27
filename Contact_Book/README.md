<h2>Explanation</h2>

    Class Definitions:
        Contact: Represents an individual contact with attributes for name, phone, email, and address. The __str__ method is overridden to provide a formatted string representation of the contact.
        ContactBook: Manages a list of Contact objects with methods to add, view, search, update, and delete contacts.

    Methods:
        add_contact(contact): Adds a new contact to the contact list.
        view_contacts(): Displays all contacts. If no contacts are available, it prints a message.
        search_contact(search_term): Searches for contacts by name or phone number and prints the found contacts.
        update_contact(search_term): Searches for a contact to update by name or phone number and prompts the user to enter new details.
        delete_contact(search_term): Searches for a contact to delete by name or phone number and removes it from the contact list if found.

    Main Function:
        Provides a menu-driven interface to interact with the contact book.
        Continuously prompts the user for input until they choose to exit.
        Calls appropriate methods of ContactBook based on user input.

<h2>Running the Application</h2>

To run the application, save the code to a file (e.g., contact_book.py) and execute it with Python:

python3 contact_book.py

<h2>This will start the contact book application, allowing you to add, view, search, update, and delete contacts interactively through a user-friendly command-line interface.</h2>
