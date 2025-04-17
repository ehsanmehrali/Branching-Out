
from load_data import load_data

def filter_users_by_email(users, email):

    for user in users:
        if user["email"] == email:
            print(user)
            return
    print("User not found!")


def filter_users_by_age(users, age):

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_name(users, name):

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def main():
    filter_option = input(
        "What would you like to filter by? 'name', 'age' and 'email' is supported): ").strip().lower()
    users_info = load_data()
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(users_info, name_to_search)
    elif filter_option == "age":
        while True:
            try:
                age_to_search = int(input("Enter an age to filter users: ").strip())
                filter_users_by_age(users_info, age_to_search)
                break
            except ValueError:
                print("Invalid Input!")
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(users_info, email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()


