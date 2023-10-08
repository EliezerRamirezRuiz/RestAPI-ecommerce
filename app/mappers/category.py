from entities import CategoryEntity
from models import CategoryModel


class CategoryMapper:
    def create_entity(category: CategoryModel) -> CategoryEntity:
        return CategoryEntity(
            id=category.id,
            name=category.name
        )
    
    
    def create_model(category: CategoryEntity) -> CategoryModel:
        return CategoryModel(
            id=category.id,
            name=category.name
        )