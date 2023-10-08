from entities import OrderEntity
from models import OrderModel


class OrderMapper:
    def create_entity(order: OrderModel) -> OrderEntity:
        return OrderEntity(
            id=order.id,
            name=order.name,
            user_id=order.user_id
        )
    
    
    def create_model(order: OrderEntity) -> OrderModel:
        return OrderModel(
            id=order.id,
            name=order.name,
            user_id=order.user_id
        )
    