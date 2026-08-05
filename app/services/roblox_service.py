from __future__ import annotations

from app.api import RobloxAPI

class RobloxService:

    def __init__(self):
        self.api = RobloxAPI()

    def resolve_user(self, username: str):
        if username.isdigit():
            return int(username)

        body = {
            "usernames": [username],
            "excludeBannedUsers": False
        }

        data = self.api.post(
            "https://users.roblox.com/v1/usernames/users",
            json=body
        )

        users = data.get("data", [])

        if not users:
            raise ValueError("Usuário não encontrado.")

        return users[0]["id"]
