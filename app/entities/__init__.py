from typing import Union

from .adress import AddressEntity
from .brand import BrandEntity
from .category import CategoryEntity
from .city import CityEntity
from .country import CountryEntity
from .order import OrderEntity
from .product import ProductEntity
from .state import StateEntity
from .user import UserEntity


Entity = Union[
    AddressEntity,
    BrandEntity,
    CategoryEntity,
    CityEntity,
    CountryEntity,
    OrderEntity,
    ProductEntity,
    StateEntity,
    UserEntity
]


__all__ = [
    "AddressEntity",
    "BrandEntity",
    "CategoryEntity",
    "CityEntity",
    "CountryEntity",
    "OrderEntity",
    "ProductEntity",
    "StateEntity",
    "UserEntity"
]
