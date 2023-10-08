from entities import UserEntity
from models import UserModel


class UserMapper:
    def create_entity(user: UserModel) -> UserEntity:
        return UserEntity(
            id=user.id,
            username=user.username,
            password=user.password,
            email=user.email,
            create_date=user.create_date
        )
    
    
    def create_model(user: UserEntity) -> UserModel:
        return UserModel(
            id=user.id,
            username=user.username,
            password=user.password,
            email=user.email,
            create_date=user.create_date
        )