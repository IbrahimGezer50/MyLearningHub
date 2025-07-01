phonebook = {
    "alice": {"number": "123"},
    "bob": {"number": "456"}
}



while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter Name:")
        number = input("Enter Number")
        phonebook[name.lower()] = {"number":number}
        print(f"Successfully added {name} with number {number}")

    if choice == "2":
        search_name = input("Search name:").lower()
        if search_name in phonebook:
            print(f"{search_name.lower()}: {phonebook[search_name]['number']}")
        else:
            print("Contact not found.")
    
    if choice == "3":
        for key, value in phonebook.items():
            print(f"{key.title()}: {value['number']}")
    
    if choice == "4":
        delete_contact = input("Delete:").lower()
        if delete_contact in phonebook:
            del phonebook[delete_contact]
            print("Successfully deleted.")
        else:
            print("Contact not found.")


    if choice == "5":
        print("Goodbye!")
        break
