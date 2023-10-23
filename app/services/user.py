from ..repositories import UserRepository
from ..mappers import UserMapper
from .base import BaseService


class UserService(BaseService):
    def __init__(
        self, 
        repository=UserRepository(), 
        mapper=UserMapper()
        ) -> None:
        super().__init__(repository, mapper)