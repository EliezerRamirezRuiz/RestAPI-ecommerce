from ..models import CityModel
from .base import BaseRepository


class CityRepository(BaseRepository):
    def __init__(self, model=CityModel) -> None:
        super().__init__(model)