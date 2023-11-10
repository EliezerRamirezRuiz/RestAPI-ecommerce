from ..repositories import CategoryRepository
from ..mappers import CategoryMapper
from .base import BaseService


class CategoryService(BaseService):
    def __init__(
        self,
        repository=CategoryRepository(),
        mapper=CategoryMapper()
    ) -> None:
        super().__init__(repository, mapper)