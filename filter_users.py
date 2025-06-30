import json

def filter_users_by_name():
    name_to_search = input("Enter a name to filter users: ").strip()

    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name_to_search.lower()]
    for user in filtered_users:
        print(user)


def filter_users_by_age():
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
    try:
        mail_to_search = input("Enter an email to filter users: ").strip()
    except ValueError:
        print("Invalid input. Please enter an email.")
        return

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
