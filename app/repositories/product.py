from ..models import ProductModel
from .base import BaseRepository


class ProductRepository(BaseRepository):
    def __init__(self, model=ProductModel) -> None:
        super().__init__(model)