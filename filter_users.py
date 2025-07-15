import json

def load_users():
    '''
    Loads user data from the JSON file and returns it as a list of users.
    '''
    with open("users.json", "r") as file:
        return json.load(file)

def filter_users_by_name(users):
    name_to_search = input("Enter a name to filter users: ").strip()
    filtered_users = [user for user in users if user["name"].lower() == name_to_search.lower()]
    for user in filtered_users:
        print(user)

def filter_users_by_age(users):
    try:
        age_to_search = int(input("Enter an age to filter users: "))
    except ValueError:
        print("Invalid input. Please enter a numeric age.")
        return
    filtered_users = [user for user in users if user["age"] == age_to_search]
    for user in filtered_users:
        print(user)

def filter_users_by_email(users):
    mail_to_search = input("Enter an email to filter users: ").strip()
    filtered_users = [user for user in users if user["email"] == mail_to_search]
    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, 'name', 'email' or 'age' is supported): ").strip().lower()
    users = load_users()

    if filter_option == "name":
        filter_users_by_name(users)
    elif filter_option == "age":
        filter_users_by_age(users)
    elif filter_option == "email":
        filter_users_by_email(users)
    else:
        print("Filtering by that option is not yet supported.")
