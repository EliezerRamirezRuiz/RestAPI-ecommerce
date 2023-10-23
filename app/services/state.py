from ..repositories import StateRepository
from ..mappers import StateMapper
from .base import BaseService


class StateService(BaseService):
    def __init__(
        self, 
        repository=StateRepository(), 
        mapper=StateMapper()
        ) -> None:
        super().__init__(repository, mapper)