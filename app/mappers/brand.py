from ..entities import BrandEntity
from ..models import BrandModel


class BrandMapper:
    def create_entity(brand: BrandModel) -> BrandEntity:
        return BrandEntity(
            id=brand.id,
            name=brand.name
        )

    def create_model(brand: BrandEntity) -> BrandModel:
        return BrandModel(
            id=brand.id,
            name=brand.name
        )
