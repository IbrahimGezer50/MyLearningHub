# Project: Simple Contact Book

contacts = []

def add_contact(name, number, contact_list):
    contact_list.append({"name": name, "number": number})


def search_contact(name, contact_list):
    for contact in contact_list:
        if contact["name"].lower() == name.lower():  # case-insensitive match
            print(f"Found: {contact['name']} - {contact['number']}")
            return
    print("Contact not found.")

def show_contacts(contact_list):
    if not contact_list:
        print("No contacts to show.")
    else:
        print("Contact List:")
        for contact in contact_list:
            print(f"- {contact['name']}: {contact['number']}")

def delete_contact(contact_list):
    to_delete = input("Contact name to delete:")
    for contact in contact_list:
        if contact["name"].lower() == to_delete.lower():
            contact_list.remove(contact)
            print("Successfully deleted contact.")
            return
    print("Contact not found.")

# --- Example Usage ---
add_contact("Alice", 123, contacts)
add_contact("Bob", 456, contacts)

search_contact("Alice", contacts)
search_contact("bob", contacts)  # works because of case-insensitive match
search_contact("Charlie", contacts)
show_contacts(contacts)
delete_contact(contacts)
