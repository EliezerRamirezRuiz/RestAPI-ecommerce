from ..models import CountryModel
from .base import BaseRepository


class CountryRepository(BaseRepository):
    def __init__(self, model=CountryModel) -> None:
        super().__init__(model)