from .address import AddressModel
from .brand import BrandModel
from .category import CategoryModel
from .city import CityModel
from .country import CountryModel
from .order import OrderModel
from .product import ProductModel
from .state import StateModel
from .user import UserModel


Model = AddressModel | BrandModel | CategoryModel | CityModel | CountryModel | OrderModel | ProductModel | StateModel | UserModel


__all__ = [
    "Model",
    "AddressModel",
    "BrandModel",
    "CategoryModel",
    "CityModel",
    "CountryModel",
    "OrderModel",
    "ProductModel",
    "StateModel",
    "UserModel",
]
