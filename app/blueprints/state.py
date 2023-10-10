from flask import Blueprint


state_blueprint = Blueprint('state', __name__)


@state_blueprint.route('/')
def get_state():
    pass