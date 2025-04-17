
from load_data import load_data

def filter_users_by_email(users):
    email = input("Enter an email to filter users: ").strip()

    for user in users:
        if user["email"] == email:
            print(user)
            return
    print("User not found!")


def filter_users_by_age(users):
    age = int(input("Enter an age to filter users: ").strip())
    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_name(users):
    name = input("Enter a name to filter users: ").strip()

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    for user in filtered_users:
        print(user)


def main():
    func_dict = {
        "name": filter_users_by_name,
        "age": filter_users_by_email,
        "emai": filter_users_by_email,
    }

    while True:
        user_input = input(
        "What would you like to filter by? 'name', 'age' and 'email' is supported): ").strip().lower()
        users_info = load_data()
        func_dict[user_input](users_info)



if __name__ == "__main__":
    main()


