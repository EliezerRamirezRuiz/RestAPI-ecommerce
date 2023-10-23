from ..models import OrderModel
from .base import BaseRepository


class OrderRepository(BaseRepository):
    def __init__(self, model=OrderModel) -> None:
        super().__init__(model)