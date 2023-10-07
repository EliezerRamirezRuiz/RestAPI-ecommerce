from dataclasses import dataclass


@dataclass
class AdressEntity():
    id: int
    name: str
    number: int
    city_id: int
    state_id: int
    country_id: int
