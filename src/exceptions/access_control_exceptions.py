class AccessControlError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class UserNotRegisteredError(AccessControlError):
    def __init__(
        self, user_id: int, username: str, first_name: str, last_name: str
    ):
        message = (
            f"User with ID: {user_id}, username: {username}, first_name: {first_name}, last_name: {last_name} "
            f"is not registered in the system."
        )
        super().__init__(message)
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name


class RolePermissionError(AccessControlError):
    def __init__(
        self,
        user_id: int,
        username: str,
        first_name: str,
        last_name: str,
        role: str | None,
    ):
        message = (
            f"Access denied for user_id: {user_id}, username: {username}, first_name: {first_name}, last_name: "
            f"{last_name}. Required role(s) not met. Current role: {role or 'None'}"
        )
        super().__init__(message)
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
