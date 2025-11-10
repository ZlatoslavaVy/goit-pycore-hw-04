def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."
    

def show_phone(args, contacts):
    if len(args) !=1:
        raise ValueError("You must enter exactly one name.")
    
    name = args[0]

    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."
    

def show_all(contacts):
    if not contacts:
        return "No contacts saved yet."
    output_lines = []
    for name, phone in contacts.items():
        output_lines.append(f"{name}: {phone}")
    return "\n".join(output_lines)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter  a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            try:
                print(add_contact(args, contacts))
            except ValueError:
                print("Please provide both name and phone number.")

        elif command == "change":
            try:
                print(change_contact(args, contacts))
            except ValueError:
                print("Please provide both name and new phone number.")

        elif command == "phone":
            try:
                print(show_phone(args, contacts))
            except ValueError:
                print("Please provide a name to look up.")

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


    