from ..entities import CountryEntity
from ..models import CountryModel


class CountryMapper:
    def create_entity(country: CountryModel) -> CountryEntity:
        return CountryEntity(
            id=country.id,
            name=country.name
        )
    
    
    def create_model(country: CountryEntity) -> CountryModel:
        return CountryModel(
            id=country.id,
            name=country.name
        )