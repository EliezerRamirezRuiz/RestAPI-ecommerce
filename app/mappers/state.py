from ..entities import StateEntity
from ..models import StateModel


class StateMapper:
    def create_entity(state: StateModel) -> StateEntity:
        return StateEntity(
            id=state.id,
            name=state.name
        )
    
    
    def create_model(state: StateEntity) -> StateModel:
        return StateModel(
            id=state.id,
            name=state.name
        )