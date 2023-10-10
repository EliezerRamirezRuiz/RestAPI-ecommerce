from ..entities import AdressEntity
from ..models import AddressModel


class AdressMapper:
    def create_entity(adress: AddressModel) -> AdressEntity:
        return AdressEntity(
            id=adress.id,
            name=adress.name,
            number=adress.number,
            city_id=adress.city_id,
            state_id=adress.state_id,
            country_id=adress.country_id
        )

    def create_model(adress: AdressEntity) -> AddressModel:
        return AddressModel(
            id=adress.id,
            name=adress.name,
            number=adress.number,
            city_id=adress.city_id,
            state_id=adress.state_id,
            country_id=adress.country_id
        )
