from flask import Blueprint


state_blueprint = Blueprint('state', __name__, url_prefix="/state")


@state_blueprint.route('/get')
def get_state():
    pass