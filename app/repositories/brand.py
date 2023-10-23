from .base import BaseRepository
from ..models import BrandModel


class BrandRepository(BaseRepository):
    def __init__(self, model=BrandModel) -> None:
        super().__init__(model)
    