def register_user(username, password):
    """
    Register a new user by adding their username and password to the user database.
    """
    users[username] = password


def login_user(username, password):
    """
    Check if the provided username and password match a registered user.
    """
    return users.get(username) == password


# Example user database (replace this with a database in a real application)
users = {}

# Example usage
while True:
    print("1. Register")
    print("2. Login")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        register_user(username, password)
        print("User registered successfully!")

    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login_user(username, password):
            print("Login successful!")
        else:
            print("Incorrect username or password. Please try again.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
