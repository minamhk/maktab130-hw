from auth import Authenticator
from exceptions import UsernameAlreadyExists, PasswordTooShort, InvalidUsername, InvalidPassword

def main():
    auth = Authenticator()

    try:
        auth.add_user("ali", "password123")
    except Exception as e:
        print("error", e)

    try:
        auth.add_user("ali", "anotherpass")
    except UsernameAlreadyExists as e:
        print("error", e)

    try:
        auth.add_user("reza", "123")
    except PasswordTooShort as e:
        print("error", e)

    try:
        auth.login("ali", "password123")
    except Exception as e:
        print("error", e)

    try:
        auth.login("hasan", "password123")
    except InvalidUsername as e:
        print("error", e)

    try:
        auth.login("ali", "wrongpass")
    except InvalidPassword as e:
        print("error", e)

        

if __name__ == "__main__":
    main()