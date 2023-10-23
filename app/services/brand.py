from ..repositories import BrandRepository
from ..mappers import BrandMapper
from .base import BaseService


class BrandService(BaseService):
    def __init__(
        self, 
        repository=BrandRepository(), 
        mapper=BrandMapper()
        ) -> None:
        super().__init__(repository, mapper)