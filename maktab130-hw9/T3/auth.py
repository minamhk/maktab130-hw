import hashlib
from exceptions import UsernameAlreadyExists, PasswordTooShort, InvalidUsername, InvalidPassword

class Authenticator:
    def __init__(self):
        self.users = {}  
        self.is_logged_in = False 

    def hash_password(self, password: str) -> str:
        """Hashes the password"""
        return hashlib.sha256(password.encode()).hexdigest()

    def add_user(self, username: str, password: str):
        """New User Registration"""
        if username in self.users:
            raise UsernameAlreadyExists("Username is already registered.")
        
        if len(password) < 8:
            raise PasswordTooShort("The password must be at least 8 characters.")
        
        hashed_password = self.hash_password(password)
        self.users[username] = hashed_password
        print(f"user {username} Successfully registered.")

    def login(self, username: str, password: str) -> bool:
        """User login"""
        if username not in self.users:
            raise InvalidUsername("The username is incorrect.")
        
        if self.users[username] != self.hash_password(password):
            raise InvalidPassword("The password is incorrect.")
        
        self.is_logged_in = True
        print(f"Login successfully completed -->{username}.")
        return True
    



    