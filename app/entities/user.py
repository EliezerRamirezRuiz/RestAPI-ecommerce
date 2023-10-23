from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserEntity:
    id: int
    username: str
    password: str
    email: str
    create_date: datetime