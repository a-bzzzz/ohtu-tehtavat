from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        cre = re.compile('^[a-zA-Z]{3,}$')
        pwd = re.compile('^(([a-zA-Z]+[0-9]+)|([0-9]+[a-zA-Z]+))[0-9a-zA-Z]*$')
        if not cre.match(username):
            raise UserInputError("Username is in wrong format!")
        if not pwd.match(password):
            raise UserInputError("Password is in wrong format!")
