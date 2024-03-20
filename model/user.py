from __future__ import annotations
from functools import total_ordering


@total_ordering
class User:
    def __init__(self, username: str, password:str):
        self.username: str = username
        if not User.validate_pass(password):
            raise ValueError("Invalid password supplied")
        self.__password:str = password

    def __eq__(self, other: User) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return self.username == other.username

    def __lt__(self, other: User) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return self.username < other.username

    def authenticate(self, password: str) -> bool:
        return self.__password == password

    @classmethod
    def validate_pass(cls, password: str) -> bool:
        if len(password) < 8:
            return False
        return True
