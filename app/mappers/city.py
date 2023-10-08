from entities import CityEntity
from models import CityModel


class CityMapper:
    def create_entity(city: CityModel) -> CityEntity:
        return CityEntity(
            id=city.id,
            name=city.name
        )
    
    def create_model(city: CityEntity) -> CityModel:
        return CityModel(
            id=city.id,
            name=city.name
        )