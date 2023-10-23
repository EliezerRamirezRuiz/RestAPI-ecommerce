from .address import AddressRepository
from .brand import BrandRepository
from .category import CategoryRepository
from .city import CityRepository
from .country import CountryRepository
from .order import OrderRepository
from .product import ProductRepository
from .state import StateRepository
from .user import UserRepository


Repository = AddressRepository | BrandRepository | CategoryRepository | CityRepository | CountryRepository | OrderRepository | ProductRepository | StateRepository | UserRepository


__all__ = [
    "Repository",
    "AddressRepository",
    "BrandRepository",
    "CategoryRepository",
    "CityRepository",
    "CountryRepository",
    "OrderRepository",
    "ProductRepository",
    "StateRepository",
    "UserRepository"
]