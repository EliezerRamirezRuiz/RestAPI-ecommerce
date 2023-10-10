from ..entities import ProductEntity
from ..models import ProductModel


class ProductMapper:
    def create_entity(product: ProductModel) -> ProductEntity:
        return ProductEntity(
            id=product.id,
            name=product.name,
            description=product.description,
            stock=product.stock
        )
    
    
    def create_model(product: ProductEntity) -> ProductModel:
        return ProductModel(
            id=product.id,
            name=product.name,
            description=product.description,
            stock=product.stock
        )