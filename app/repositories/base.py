from typing import Optional, Tuple

from sqlalchemy import Result
from sqlalchemy import select, update

from ..models import (
    Model,
    db as database
)


class BaseRepository:
    """ Class Focused """
    def __init__(self, model: Model) -> None:
        self.db = database
        self.model = model


    def find_by_id(self, id: int) -> Optional[Model]:
        """  """
        try:
            address = self.db.session.execute(
                select(self.model).filter_by(id=id)).scalar_one()

            return address

        except Exception as ex:
            print(ex)
            return None

    def find_by_name(self, name: str) -> Optional[Model]:
        """ Find AddressModel by name """
        try:
            address = self.db.session.execute(
                select(self.model).filter_by(name=name)).scalar_one()
            return address

        except Exception as ex:
            print(ex)
            return None

    def find_all(self) -> Optional[Result[Tuple[Model]]]:
        """ Find all AddressModel """
        try:
            addresses = self.db.session.execute(
                select(self.model).order_by(self.model.id))
            return addresses

        except Exception as ex:
            print(ex)
            return None

    def create_one(self, model: Model):
        """ Create AddressModel """
        try:
            self.db.session.add(model)

            if model is None:
                self.db.session.rollback()
                return None

            self.db.session.commit()
            return model

        except Exception as ex:
            print(ex)
            return None

    def update_one(self, id: int, model: dict):
        try:
            model_updated = self.db.session.execute(
                update(self.model)
                .where(self.model.id == id)
                .values(model)
            )
            self.db.session.commit()
            
            return model_updated

        except Exception as ex:
            print(ex)
            return None
