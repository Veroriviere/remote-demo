import json
import sys

def load_contacts():
    try:
        with open('contacts.json', 'r') as f:
            content = f.read()
            return json.loads(content) if content else []
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f, indent=2)

def add_contact(contacts, name, email, phone):
    contact = {
        "name": name,
        "email": email,
        "phone": phone
    }
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Added contact: {name}")

def list_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['email']} - {contact['phone']}")

def main():
    contacts = load_contacts()
    if len(sys.argv) < 2:
        print("Usage: python contacts.py [add|list]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "add" and len(sys.argv) == 5:
        add_contact(contacts, sys.argv[2], sys.argv[3], sys.argv[4])
    elif command == "list":
        list_contacts(contacts)
    else:
        print("Invalid command or arguments")

if __name__ == "__main__":
    main()
