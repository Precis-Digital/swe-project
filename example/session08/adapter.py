import dataclasses
from typing import Iterator

import requests


class OldRestAPIClient:
    @staticmethod
    def get_all_users():
        response = requests.get("https://api.example.com/users")
        return response.json()

    @staticmethod
    def get_user_details(user_id):
        response = requests.get(f"https://api.example.com/users/{user_id}")
        return response.json()


@dataclasses.dataclass
class User:
    id: int
    name: str
    email: str


class NewUserAPI:
    def __init__(self) -> None:
        self.old_api_client = OldRestAPIClient()

    def _fetch_users(self) -> list[User]:
        users_data = self.old_api_client.get_all_users()
        return [User(**user) for user in users_data]

    def __getitem__(self, index: int) -> User:
        users = self._fetch_users()
        return users[index]

    def __iter__(self) -> Iterator[User]:
        users = self._fetch_users()
        return iter(users)

    def __len__(self) -> int:
        users = self._fetch_users()
        return len(users)

    def __call__(self, user_id: int) -> User:
        user_data = self.old_api_client.get_user_details(user_id)
        return User(**user_data)

    def __str__(self) -> str:
        return f"UserAPIAdapter with {len(self._fetch_users())} users"

    def __repr__(self) -> str:
        return f"<UserAPIAdapter(users={self._fetch_users()})>"


if __name__ == "__main__":
    user_api_adapter = NewUserAPI()

    # Using the adapter to iterate over users
    print("Iterating over users:")
    for user in user_api_adapter:
        print(user)

    # Accessing a specific user by index
    print("\nAccessing a user by index:")
    print(user_api_adapter[0])

    # Using the adapter to get user details by calling it
    print("\nGetting user details by user ID:")
    print(user_api_adapter(1))

    # Demonstrating the use of dunder methods
    print("\nUsing dunder methods:")
    print(str(user_api_adapter))
    print(repr(user_api_adapter))
