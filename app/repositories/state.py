from ..models import StateModel
from .base import BaseRepository


class StateRepository(BaseRepository):
    def __init__(self, model=StateModel) -> None:
        super().__init__(model)