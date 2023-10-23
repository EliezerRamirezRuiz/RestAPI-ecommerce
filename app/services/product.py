from ..repositories import ProductRepository
from ..mappers import ProductMapper
from .base import BaseService


class ProductService(BaseService):
    def __init__(
        self, 
        repository=ProductRepository(), 
        mapper=ProductMapper()
        ) -> None:
        super().__init__(repository, mapper)