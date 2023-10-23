from typing import Optional

from ..mappers import Mapper
from ..entities import Entity
from ..repositories import Repository
from ..models import Model


class BaseService:
    """Class base focused in create `entity | model`"""
    def __init__(self, repository: Repository, mapper: Mapper) -> None:
        self.repository = repository
        self.mapper = mapper

    def get_by_id(self, id: int) -> Optional[Entity]:
        """ Get model by id """
        model = self.repository.find_by_id(id)

        if model is None:
            return None

        return self.mapper.create_entity(model)

    def get_by_name(self, name: str) -> Optional[Entity]:
        """ Get model by name """
        model = self.repository.find_by_name(name)

        if model is None:
            return None

        return self.mapper.create_entity(model)

    def create_model(self, model: Model) -> Optional[Entity]:
        """ Create model """
        model_created = self.repository.create_one(model)

        if model_created is None:
            return None

        return self.mapper.create_entity(model)

    def update_model(self, id: int, model: dict) -> Optional[Entity]:
        """ Update model"""
        model = self.repository.update_one(id, model)

        if model is None:
            return None

        return "model updated"
