from ..entities import AddressEntity
from ..models import AddressModel


class AddressMapper:
    def create_entity(address: AddressModel) -> AddressEntity:
        return AddressEntity(
            id=address.id,
            name=address.name,
            number=address.number,
            city_id=address.city_id,
            state_id=address.state_id,
            country_id=address.country_id
        )

    def create_model(address: AddressEntity) -> AddressModel:
        return AddressModel(
            id=address.id,
            name=address.name,
            number=address.number,
            city_id=address.city_id,
            state_id=address.state_id,
            country_id=address.country_id
        )
