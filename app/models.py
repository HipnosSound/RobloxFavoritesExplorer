from dataclasses import dataclass


@dataclass(slots=True)
class FavoriteItem:
    id: int
    name: str
    category: str
    thumbnail: str
    url: str


@dataclass(slots=True)
class RobloxUser:
    id: int
    username: str
