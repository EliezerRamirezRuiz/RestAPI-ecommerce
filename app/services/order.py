from ..repositories import OrderRepository
from ..mappers import OrderMapper
from .base import BaseService


class OrderService(BaseService):
    def __init__(
        self, 
        repository=OrderRepository(), 
        mapper=OrderMapper()
        ) -> None:
        super().__init__(repository, mapper)