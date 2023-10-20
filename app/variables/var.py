from typing import Union

from ..models import (
    AddressModel,
    BrandModel,
    CategoryModel,
    CityModel,
    CountryModel,
    OrderModel,
    ProductModel,
    StateModel
)

from ..entities import (
    AddressEntity,
    BrandEntity,
    CategoryEntity,
    CityEntity,
    CountryEntity,
    OrderEntity,
    ProductEntity,
    StateEntity,
    UserEntity
)

from ..repositories import (
    AddressRepository,
    BrandRepository,
    CategoryRepository,
    CityRepository,
    CountryRepository,
    OrderRepository,
    ProductRepository,
    StateRepository,
    UserRepository
)

from ..mappers import (
    AddressMapper,
    BrandMapper,
    CategoryMapper,
    CityMapper,
    CountryMapper,
    OrderMapper,
    ProductMapper,
    StateMapper,
    UserMapper    
)


Model = Union[
    AddressModel,
    BrandModel, 
    CategoryModel,
    CityModel,
    CountryModel,
    OrderModel,
    ProductModel,
    StateModel
]

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

Repository = Union[
    AddressRepository,
    BrandRepository,
    CategoryRepository,
    CityRepository,
    CountryRepository,
    OrderRepository,
    ProductRepository,
    StateRepository,
    UserRepository
]

Mapper = Union[
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
