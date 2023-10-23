from typing import Union

from .address import AddressMapper
from .brand import BrandMapper
from .category import CategoryMapper
from .city import CityMapper
from .country import CountryMapper
from .order import OrderMapper
from .product import ProductMapper
from .state import StateMapper
from .user import UserMapper


Mapper = type[
    Union[
        AddressMapper,
        BrandMapper,
        CategoryMapper,
        CityMapper,
        CountryMapper,
        OrderMapper,
        ProductMapper,
        StateMapper,
        UserMapper
    ]
]


__all__ = [
    "AddressMapper",
    "BrandMapper",
    "CategoryMapper",
    "CityMapper",
    "CountryMapper",
    "OrderMapper",
    "ProductMapper",
    "StateMapper",
    "UserMapper"
]