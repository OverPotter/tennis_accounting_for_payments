class UserException(Exception):
    def __init__(self, details: str):
        self.details = details


class UserAlreadyExist(UserException):
    pass


class UserDoesntExist(UserException):
    pass
