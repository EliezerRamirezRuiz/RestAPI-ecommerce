from ..models import UserModel
from .base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, model=UserModel) -> None:
        super().__init__(model)