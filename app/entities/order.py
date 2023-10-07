from dataclasses import dataclass


@dataclass
class OrderEntity():
    id: int
    name: str
    user_id: int