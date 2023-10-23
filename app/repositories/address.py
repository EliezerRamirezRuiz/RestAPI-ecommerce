from .base import BaseRepository
from ..models import AddressModel


class AddressRepository(BaseRepository):
    def __init__(self, model=AddressModel) -> None:
        super().__init__(model)