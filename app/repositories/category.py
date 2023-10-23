from dataclasses import dataclass

from .base import BaseRepository
from ..models import CategoryModel


@dataclass
class CategoryRepository(BaseRepository):
    def __init__(self, model=CategoryModel) -> None:
        super().__init__(model)