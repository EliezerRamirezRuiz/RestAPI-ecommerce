from entities import AdressEntity
from models import AdressModel


class AdressMapper:
    def create_entity(adress: AdressModel) -> AdressEntity:
        return AdressEntity(
            id=adress.id,
            name=adress.name,
            number=adress.number,
            city_id=adress.city_id,
            state_id=adress.state_id,
            country_id=adress.country_id
        )

    def create_model(adress: AdressEntity) -> AdressModel:
        return AdressModel(
            id=adress.id,
            name=adress.name,
            number=adress.number,
            city_id=adress.city_id,
            state_id=adress.state_id,
            country_id=adress.country_id
        )
