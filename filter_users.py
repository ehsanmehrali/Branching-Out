
from load_data import load_data

def filter_users_by_email(users):
    """
    :param users: A list of dict
    """
    email = input("Enter an email to filter users: ").strip()

    for user in users:
        if user["email"] == email:
            for key, value in user.items():
                print(f"{f"{key}":{'-'}<20}", f"{value}")
            return
    print("User not found!")


def filter_users_by_age(users):
    """
    :param users: A list of dict
    """
    while True:
        try:
            age = int(input("Enter an age to filter users: ").strip())
            filtered_users = [user for user in users if user["age"] == age]
            for user in filtered_users:
                for key, value in user.items():
                    print(f"{f"{key}":{'-'}<20}", f"{value}")
            break

        except ValueError:
            print("Invalid Input!")


def filter_users_by_name(users):
    """
    :param users: A list of dict
    """
    name = input("Enter a name to filter users: ").strip()

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    for user in filtered_users:
        for key, value in user.items():
            print(f"{f"{key}":{'-'}<20}", f"{value}")


def main():
    """
    It takes an input from the user and based on that, it calls the user's desired filter through a dispatcher.
    """
    func_dict = {
        "name": filter_users_by_name,
        "age": filter_users_by_age,
        "email": filter_users_by_email,
    }

    while True:
        try:
            user_input = input("What would you like to filter by? 'name', 'age' and 'email' is supported: ").strip().lower()
            users_info = load_data()
            func_dict[user_input](users_info)
            break
        except KeyError:
            print("This filter does not exist!")



if __name__ == "__main__":
    main()


