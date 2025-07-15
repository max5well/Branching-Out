import json

def filter_users_by_name():
    '''
    Asking for input (name) from user to search for this name.
    If name is found, print the user(s) with this name.
    '''
    name_to_search = input("Enter a name to filter users: ").strip()

    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name_to_search.lower()]
    for user in filtered_users:
        print(user)


def filter_users_by_age():
    '''
    Asking for input (age) from user to search for this age.
    If age is found, print the user(s) with this age.
    '''
    try:
        age_to_search = int(input("Enter an age to filter users: "))
    except ValueError:
        print("Invalid input. Please enter a numeric age.")
        return

    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age_to_search]
    for user in filtered_users:
        print(user)

def filter_users_by_email():
    '''
    Asking for input (email) from user to search for this email.
    If email is found, print the user(s) with this email.
    '''
    mail_to_search = input("Enter an email to filter users: ").strip()

    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == mail_to_search]
    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, 'name', 'email' or 'age' is supported): ").strip().lower()

    if filter_option == "name":
        filter_users_by_name()
    elif filter_option == "age":
        filter_users_by_age()
    elif filter_option == "email":
        filter_users_by_email()
    else:
        print("Filtering by that option is not yet supported.")
